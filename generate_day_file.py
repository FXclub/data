import sys
from os import listdir
from os.path import isfile, join

currency_name = sys.argv[1]
print("handling currency ["+currency_name+"]")

cur_path = "./"
suffix = ".csv"
#files = [f for f in listdir(cur_path) if isfile(join(cur_path, f))]
files = []
for f in listdir(cur_path):
    if isfile(join(cur_path, f)) and f.find(suffix)!=-1:
        files.append(f)

print("ready to load these files:")
for f in files:
    print(f)

################################
# Date counting
################################
count = 0
count_date = ""
for f in files:
    with open(cur_path+f,"r") as data_file:
        for line in data_file:
            datalist=line.split(" ")
            date = datalist[0]
            if(date!=count_date):
                count_date=date
                count+=1

print("["+str(count)+"] dates in total")

################################
# Processing
################################
prefix=currency_name + "_"
outpath = "./out/"
outfile_name = ""
process_count = 0
for f in files:
    with open(cur_path+f,"r") as data_file:
        for line in data_file:
            #replace ; with ,
            line=line.replace(";",",")
            #print(line.strip(), end="["+f+"]\n")

            #get date
            datalist=line.split(" ")
            date=datalist[0]

            #update filename
            if(date!=outfile_name):
                outfile_name=date
                process_count+=1
                print("processing ["+date+"] ("+str(process_count)+"/"+str(count)+")")

            #write to file
            with open(outpath+prefix+outfile_name+suffix, "a") as outfile:
                outfile.write(line)
