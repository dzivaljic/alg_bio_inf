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

def exist_d(x,text,d,k):    
    for obj in text:
        br=0                            ###################################################################
        for i in range(0,len(obj)-k+1): ##### ovo ovde dobro pogledat jer sam izgubija dosta zivaca ######
            if(hamming_distance(obj[i:i+k], x)<=d): #######################################################
                br=1
        if(br==0):
            return False
    return True
        
 
        
def MotifEnumeration(text,k,d):
    rez=set()
    svi_kandidati=set()
    text=text.split(" ")
    for a in text:
        for i in range(0,len(a)-k):
            pattern=a[i:i+k]
            neighbor_pattern=Neighborhood(pattern, d)
            svi_kandidati=svi_kandidati.union(neighbor_pattern)
            
    
    for x in svi_kandidati:
        if(exist_d(x, text, d,k)==True):
            #if(duplicate_rejact(x,rez,d)==True):
            rez.add(x)
    
                
            
    
    return rez

#ova funkcija nije potribna al mozda ce nekad bit##
def duplicate_rejact(x,rez,d):
    for i in rez:
        if(hamming_distance(i, x)<=d):
            return False
    return True
        
if __name__ == "__main__":
    
    text="AGGCATGAAGCAACAACCAATCCAC ACGCACAGTCCAGCCGATTTACCAA ATCCGAAAGGATACAGAATTGCCAT GTGGTTGATGTAGCGGCCAACCTAC CACACCACGACATTGGCCATGTAGT TTATCACTGCTCAGCGCCATTGATA ATGTCCCCACTACATCGAGGGTCTC GCATGAAACTTCCAGGCCGCAGCGC TCCACCCGGGCGGCAAAATGCACGC ACCATCGTTAGTTGGTCCTAACAAA"                  


    k=5
    d=2
    
    res = MotifEnumeration(text, k, d)
    
    print("\n".join(res))
    
    



            

        
        

