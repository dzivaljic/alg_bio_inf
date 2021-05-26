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
        
        
        
def Neighborhood(pattern,d):
    rez={""}
    if (d==0):
        return {pattern}
    all_kmers=generate_all_kmer(len(pattern))
    rez={k for k in all_kmers if hamming_distance(k, pattern)<=d}
   
    return rez

#print(Neighborhood("ACG", 1))
print("\n".join(Neighborhood("CGCGGGTCG", 2)))
            

        
        

