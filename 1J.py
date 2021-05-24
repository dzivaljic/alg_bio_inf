def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def reversecomplement(text):
    a=""
    for i in text:
        if(i == "A"):
            a=a+"T"
        if (i == "T"):
            a=a+"A"
        if (i == "G"):
            a=a+"C"
        if (i == "C"):
            a=a+"G"

    return a[::-1]

def frequency_compl(text,k,d1):
    d_compl=dict()
    d_rez_compl=dict()

    for i in range(0,len(text)-k):
        try:
            d_compl[reversecomplement(text[i:i+k])]+=1
        except:
            d_compl[reversecomplement(text[i:i+k])]=1

    for i in d_compl.keys():
        for j in d_compl.keys():
            if(hamming_distance(i, j)<=d1):
                try:
                    d_rez_compl[i]+=d_compl[j]
                except:
                    d_rez_compl[i]=d_compl[j]    
                    
    return d_rez_compl

def frequency_with_mismatches(text,k,d1):
    d=dict()
    d_rez=dict()

    for i in range(0,len(text)-k):
        try:
            d[text[i:i+k]]+=1
        except:
            d[text[i:i+k]]=1

    for i in d.keys():
        for j in d.keys():
            if(hamming_distance(i, j)<=d1):
                try:
                    d_rez[i]+=d[j]
                except:
                    d_rez[i]=d[j]

    return d


if __name__ == "__main__":

    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k=4
    d1=1

    res1 = frequency_with_mismatches(text,k,d1)
    res2 = frequency_compl(text,k,d1)
    
    print(res1.values())
    print(res2.values())

    
    
    
    
    
    
    
    
    
    
    