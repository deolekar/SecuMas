# Credit https://github.com/dorklein/py-gics/
from SecuMas.definitions import d_20180929, d_20230318

DEFINITIONS = {
    "20180929": d_20180929,
    "20230318": d_20230318,
}

DEFAULT_VERSION = '20230318'


class gics:

    def __init__(self, code: str = None, version: str = DEFAULT_VERSION):
        """Represents a GICS code. You can instantiate GICS codes using a string representing a code.
        The string has to be a valid GICS. If it's not, that is_valid method will return false.

        Note:
            that creating an empty GICS will mark it as invalid but can still be used to query the definitions
            (although that object itself will not be a definition)

        Args:
         code (str): GICS code to parse. Valid GICS codes are strings 2 to 8 characters long, with even length.
         version (str):

        Raises:
            ValueError: When given an invalid version
        """
        self._definition_version = version
        _definition = DEFINITIONS.get(self._definition_version)

        if not _definition:
            raise ValueError(f'Unsupported GICS version: {version}. Available versions are {list(DEFINITIONS.keys())}')

        self._definition = Map.create_recursively(_definition)

        self._code = code

        if self.is_valid:
            self._levels = [
                self._get_definition(code[:2]),
                self._get_definition(code[:4]) if len(code) >= 4 else None,
                self._get_definition(code[:6]) if len(code) >= 6 else None,
                self._get_definition(code[:8]) if len(code) == 8 else None
            ]
        else:
            self._code = None

    @property
    def definition(self):
        return self._definition

    @property
    def is_valid(self) -> bool:
        return self.code and isinstance(self.code, str) and len(self.code) >= 2 and len(self.code) <= 8 and len(
            self.code) % 2 == 0 and self._definition.get(self.code)

    @property
    def code(self):
        return self._code

    @property
    def sector(self):
        """Gets the definition for the sector of this GICS object (GICS level 1)

        Returns:
            Definition of the GICS level. It has 3 properties: name, description and code.
            Keep in mind that only level 4 usually has a description.
        """
        return self.level(1)

    @property
    def industry_group(self):
        """Gets the definition for the industry group of this GICS object (GICS level 2)

        Returns:
            Definition of the GICS level. It has 3 properties: name, description and code.
            Keep in mind that only level 4 usually has a description.
        """
        return self.level(2)

    @property
    def industry(self):
        """Gets the definition for the industry of this GICS object (GICS level 3)

        Returns:
            Definition of the GICS level. It has 3 properties: name, description and code.
            Keep in mind that only level 4 usually has a description.
        """
        return self.level(3)

    @property
    def sub_industry(self):
        """Gets the definition for the sub-industry of this GICS object (GICS level 4)

        Returns:
            Definition of the GICS level. It has 3 properties: name, description and code.
            Keep in mind that only level 4 usually has a description.
        """
        return self.level(4)

    @property
    def children(self):
        """Gets all the child level elements from this GICS level.
        For example, for a Sector level GICS, it will return all Industry Groups in that Sector.
        If the GICS is invalid (or empty, as with a null code), it will return all Sectors.
        A Sub-industry level GICS will return an empty array.

        Returns:
            List containing objects with properties code (the GICS code), name (the name of this GICS),
            and description (where applicable)
        """
        if self.is_valid:
            keys = filter(lambda k: k.startswith(self._code) and len(k) == len(self._code) + 2, self._definition.keys())
        else:
            keys = filter(lambda k: len(k) == 2, self._definition.keys())

        return list(map(lambda k: Map({
            'code': k,
            'name': self._definition[k].name,
            'description': self._definition[k].description
        }), keys))

    def _get_definition(self, gics_code):
        definition = self._definition[gics_code]
        definition.code = gics_code

        return definition

    def level(self, gics_level: int):
        """Gets the definition of the given level for this GICS object.

        Args:
            gics_level: Level of GICS to get.
                Valid levels are: 1 (Sector), 2 (Industry Group), 3 (Industry), 4 (Sub-Industry)

        Returns:

        """
        if not self.is_valid or not gics_level or not isinstance(gics_level,int) or gics_level < 1 or gics_level > 4:
            return None

        return self._levels[gics_level - 1]
    
class Map(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    @staticmethod
    def create_recursively(data: dict) -> 'Map':
        data = Map(data)

        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = Map.create_recursively(value)

        return data