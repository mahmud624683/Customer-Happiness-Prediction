import json
import csv
import pandas as pd 

header=["overall","verified", "reviewTime","reviewerID","asin","Size","Color","reviewerName","reviewText","summary","unixReviewTime","vote"]
csv_data=[]
with open('AMAZON_FASHION_5.json', 'rb') as f:
    data = f.readlines()
for idata in data:
    idata=idata.decode("utf-8")
    idata=idata.replace("}","")
    idata=idata.replace("\n","")
    temp_list=[]
    for x in header:
        entry=""
        if (len(idata.split(x))>1):
            sdata=idata.split(x)[-1]
            if (x=="overall") | (x=="verified") | (x=="unixReviewTime"):
                sdata=sdata.split(",")[0]
            else: 
                sdata=sdata.split("\",")[0]
            sdata=sdata.split(":")[-1]
            entry=sdata.replace('\"',"")
            #print(x+"="+entry)
        temp_list.append(entry)
    csv_data.append(temp_list)
print(csv_data)
print(len(csv_data))
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(csv_data)