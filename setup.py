from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="SecuMas",
    version="0.0.1.5",
    author="A Deolekar",
    author_email="sher.buk@gmail.com",
    url="https://secumas.dev",
    description="An application build for Securities Master platform",
    readme = "README.md",
    packages=find_packages(),
    classifiers=[
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Development Status :: 2 - Pre-Alpha',
    ],
    install_requires=[],
    long_description=description,
    long_description_content_type='text/markdown',
    license='MIT License',
    platforms=['any'],
    project_urls={
        'Documentation': 'https://secumas.dev/',
        'Source': 'https://github.com/deolekar/SecuMas'},
)