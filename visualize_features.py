import matplotlib.pyplot as plt
import csv

id=[]
overall=[]
RPM=[]
RPA=[]
RNM=[]
RNA=[]
RNP=[]
RNN=[]
SPM=[]
SPA=[]
SNM=[]
SNA=[]
SNP=[]
SNN=[]

with open('feature.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id.append(row["id"])
        overall.append(row["overall"])
        RPM.append(row["RPM"])
        RPA.append(row["RPA"])
        RNM.append(row["RNM"])
        RNA.append(row["RNA"])
        RNP.append(row["RNP"])
        RNN.append(row["RNN"])
        SPM.append(row["SPM"])
        SPA.append(row["SPA"])
        SNM.append(row["SNM"])
        SNA.append(row["SNA"])
        SNP.append(row["SNP"])
        SNN.append(row["SNN"])

            

plt.scatter(id,RNA, label='RNA')
plt.plot(id,overall, label='overall')
plt.scatter(id,RPA, label='RPA')
plt.scatter(id,SPA, label='SPA')
plt.scatter(id,SNA, label='SNA')
plt.legend()
plt.show()