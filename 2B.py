def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def generate_all_kmer(k):
    rez={"A","C","G","T"}
    D={0:"A",1:"C",2:"G",3:"T"}
    while len(rez)<4**k:
        rez={i+j for i in rez for j in D.values()}
    return rez

def min_h_distance(pattern,text):
    rez=[]
    for i in range(0,len(text)-len(pattern)+1):
        rez.append(hamming_distance(text[i:i+len(pattern)], pattern))
    return min(rez)

def median_string(text,k):
    D=dict()
    all_kmers=generate_all_kmer(k)
    for x in all_kmers:
        for y in text:
            try:
                D[x]+=min_h_distance(x, y)
            except:
                D[x]=min_h_distance(x, y)
    return[x for x in D.keys() if D[x]==min(D.values())]
    
if __name__ == "__main__":
    
    text=input()
    text=text.split("\n")              
    k=6
    
    
    res = median_string(text, k)
    
    print("\n".join(res))