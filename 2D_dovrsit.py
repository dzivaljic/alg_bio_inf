
import numpy

def single(text,slovo):
    rez=[]
    for i in range(0,len(text)):
        rez.append(0)
    for i in range(0,len(text)):
        if(text[i]==slovo):
            rez[i]+=1
        
                     
    return rez
        
def profile_most_probable(text,k,matrica):
    rez={}
    D={"A":0,"C":1,"G":2,"T":3}
    for i in range (0,len(text)-k+1):
        k_mer=text[i:i+k]
        br=0
        for j in k_mer:
            try:
                rez[k_mer]*=matrica[D[str(j)]][br]
            except:
                rez[k_mer]=matrica[D[str(j)]][br]
            br+=1
    return[k for k in rez.keys() if rez[k]==max(rez.values())][0]
       

def profile_matrix(text,k):
    rez=[[0]*k]*4
    D={"A":0,"C":1,"G":2,"T":3}
    suma=0
    for row in text:
        for x in D.keys():
            rez[D[x]]=[i+j for i,j in zip(rez[D[x]],single(row, x))]
            
    for el in rez:
        suma=suma+sum(el)
    for x in D.keys():
        rez[D[x]]=[i/suma for i in rez[D[x]]]
    
    return rez

def greedy_motif_search(dna, k, t):
    best_motifs=[""]*t
    for i in range (0,t):
        best_motifs[i]=dna[i][0:k]
    for i in range(0,len(dna[0])-k+1):
        motif_1=dna[0][i:i+k]
        motifs=[]
        motifs.append(motif_1)
        for j in range(1,t):
            profile_matrix_now=profile_matrix(motifs, k)
            motif_new=profile_most_probable(dna[j], k, profile_matrix_now)
            motifs.append(motif_new)
        if(score(dna, motifs, t, k)<=score(dna, best_motifs, t, k)):
            best_motifs=motifs
    return best_motifs
        
def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def score(dna,motifs,t,k):
    rez=0
    pom=[]
    for i in range(0,t):
        for j in range(0,len(dna[i])-k+1):
            pom.append(hamming_distance(dna[i][j], motifs[i]))
        rez=rez+min(pom)
    return rez

if __name__ == "__main__":
    
    unos=input()
    dna=unos.split("\n")       
    k=3
    t=5
    
    
    res = greedy_motif_search(dna, k,t)
    
    print("\n".join(res))
    
    
    
    
    
    