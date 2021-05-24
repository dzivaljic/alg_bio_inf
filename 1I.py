def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def freq_max(text,k,d1):
    d=dict()
    for i in range(0,len(text)-k):
        br=0
        for j in range(0,len(text)-k):
            if(hamming_distance(text[i:i+k], text[j:j+k])<=d1):
                br=br+1
        d[text[i:i+k]]=br
    return d
    
    
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
    return d_rez
                

if __name__ == "__main__":

    text = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC"
    k=10
    d1=2

    res = freq_max(text,k,d1)
    res2=frequency_with_mismatches(text, k, d1)
    print([k for k in res.keys() if res[k]==max(res.values())])
    print([k for k in res2.keys() if res2[k]==max(res2.values())])



