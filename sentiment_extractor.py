from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from feature import *
import csv
import math

def penn_to_wn_adj(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('R'):
        return wn.ADV
    return None

def penn_to_wn_noun(tag):
    if tag.startswith('N'):
        return wn.NOUN
    return None

def get_sentiment(word,tag,mode):

    if mode==1:
        wn_tag = penn_to_wn_adj(tag)
        if wn_tag not in (wn.ADJ, wn.ADV):
            return []
    else:
        wn_tag = penn_to_wn_noun(tag)
        if wn_tag not in (wn.ADJ, wn.ADV):
            return []

    lemma = lemmatizer.lemmatize(word, pos=wn_tag)
    if not lemma:
        return []

    synsets = wn.synsets(word, pos=wn_tag)
    if not synsets:
        return []

    synset = synsets[0]
    swn_synset = swn.senti_synset(synset.name())

    return [swn_synset.pos_score(),swn_synset.neg_score(),swn_synset.obj_score()]

def enquiry(lis): 
    for x in lis:
        if len(x)>0:
            return 1
    return 0 

def find_star(pos_val):
    for i in range(0,len(pos_val)):
        if(pos_val[i][0]=="star"):
            return i 
    return -1

def get_features(senti_val,pos_val):
    feature_data=feature_value()
    i=0
    lenth=len(senti_val)
    while(i<lenth):
        x=senti_val[i]
        if(len(x)>0):
            tag=pos_val[i][1]
            if tag.startswith('R'):
                val=[0,0]
                while(tag.startswith('R') & len(x)>0):
                    val[0]+=x[0]
                    val[1]+=x[1]
                    i+=1
                    if(i<lenth): 
                        x=senti_val[i]
                        tag=pos_val[i][1]
                    else: 
                        break
                if(len(x)>0) & (i<lenth): 
                    x[2]=math.sqrt(x[0]*val[0]) +math.sqrt(x[1]*val[1]) 
                    x[1]=math.sqrt(x[1]*val[0]) +math.sqrt(x[0]*val[1]) 
                    x[0]=x[2]
                else: 
                    x=val

            if(x[0]>0):
                feature_data.NP+=1
                feature_data.PA+=x[0]
                if(x[0]>feature_data.PM):
                    feature_data.PM=x[0]
                #print(feature_data.PA,x[0], feature_data.NP)
            if(x[1]>0):
                feature_data.NN+=1
                feature_data.NA+=x[1]
                if(x[1]>feature_data.NM):
                    feature_data.NM=x[1] 
        i+=1
        
    if (feature_data.NP>0):
        feature_data.PA/=feature_data.NP
    if (feature_data.NN>0):
        feature_data.NA/=feature_data.NN
    return feature_data

def feature_extractor(data):
    #print(".", end ="") 
    raw_sentences = sent_tokenize(data)
    for sen in raw_sentences:
        sen=sen.lower()
        pos_val = pos_tag(word_tokenize(sen))
        #print(pos_val)
        senti_val = [get_sentiment(x,y,1) for (x,y) in pos_val]
        #print(senti_val)
        adj_enq=enquiry(senti_val)
        #print(adj_enq)
        star_index=find_star(pos_val)
        if(star_index>=0):
            #print(star_index)
            #print('star found')
            feature_data=feature_value()
            star=pos_val[star_index-1][0]
            if star=="one":
                feature_data.NA=1
                feature_data.NM=1
                feature_data.NN=1
            elif star=="two":
                feature_data.NA=0.5
                feature_data.NM=0.5
                feature_data.NN=1
            elif star=="three":
                feature_data.NA=0.5
                feature_data.NM=0.5
                feature_data.NN=1
                feature_data.PA=0.5
                feature_data.PM=0.5
                feature_data.NP=1
            elif star=="four":
                feature_data.PA=0.5
                feature_data.PM=0.5
                feature_data.NP=1
            else:
                print("gaint")
                feature_data.PA=1
                feature_data.PM=1
                feature_data.NP=1
            return feature_data

        elif(adj_enq):
            return get_features(senti_val,pos_val)
            
        else: 
            senti_val = [get_sentiment(x,y,0) for (x,y) in pos_val]
            return get_features(senti_val,pos_val)
    
    return feature_value()


def main():
    csv_data=[]
    i=1
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp={}
            temp["overall"]=row["overall"]
            review_feature=feature_extractor(row["reviewText"])
            temp["RPM"]=review_feature.PM
            temp["RPA"]=review_feature.PA
            temp["RNM"]=review_feature.NM
            temp["RNA"]=review_feature.NA
            temp["RNP"]=review_feature.NP
            temp["RNN"]=review_feature.NN
            
            review_feature=feature_extractor(row["summary"])
            temp["SPM"]=review_feature.PM
            temp["SPA"]=review_feature.PA
            temp["SNM"]=review_feature.NM
            temp["SNA"]=review_feature.NA
            temp["SNP"]=review_feature.NP
            temp["SNN"]=review_feature.NN
            csv_data.append(temp)
            #break
            print('Row-'+str(i)+" reading is done....", flush=True) 
            i+=1
            
    #print(csv_data[0])
    with open('feature.csv', 'w') as csvfile:
        csv_columns = ['overall','RPM','RPA','RNM','RNA','RNP','RNN','SPM','SPA','SNM','SNA','SNP','SNN']
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in csv_data:
            writer.writerow(data)
        


if __name__=='__main__':
    main()