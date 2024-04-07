import csv

def fromcsv(csvFile,bbgFile):
    rowCount =0

    bbg = open(bbgFile,'w')

    #results = []
    with open(csvFile, newline='') as inputfile:
        xs = csv.reader(inputfile)
        for idx, x in enumerate(xs):
            if (idx == 0):
                bbg.write("START-OF-FILE\n")
                bbg.write("PROGRAMNAME=getdata\n")
                bbg.write("DATEFORMAT=yyyymmdd\n")
                bbg.write("\n")        
                bbg.write("START-OF-FILE\n")

                x=x[0]
                headers = x.split("|")
                for i, header in enumerate(headers):
                    if(i>2):
                        field = header + "\n"
                        bbg.write(field)
                bbg.write("END-OF-FIELDS\n")
                bbg.write("\n")
                bbg.write("TIMESTARTED=Tue Jul 13 14:17:17 EDT 2004\n")        
                bbg.write("START-OF-DATA\n")

            else:
                row = x[0] + "\n"
                bbg.write(row)
                rowCount+=1
            
        if (rowCount>0):
            bbg.write("END-OF-DATA\n")
            rowCountRecord = "DATARECORDS="+str(rowCount)+"\n"
            bbg.write(rowCountRecord)
            bbg.write("TIMEFINISHED=Tue Jul 13 14:17:17 EDT 2004\n")        
            bbg.write("END-OF-FILE\n")        

        bbg.close()