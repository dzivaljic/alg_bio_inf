import random
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
    return[a for a in rez.keys() if rez[a]==max(rez.values())][0]

def Motifs(dna,profile,k):
    
    motifs=[]
    for i in range (0,len(dna)):
        motifs.append(profile_most_probable(dna[i], k, profile))
    return motifs
       

def profile_pseudocounts(motifs,k):
    matrix=list()
    for i in range(0,k):
        for nucl in range(0,4):
            matrix.append(list())
            matrix[nucl].append((count(motifs,nucl,i)+1) / (len(motifs)+4))
    return  matrix
        
def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def count(motifs,nucl,i):
    # compute count for each nucleotide of i-th column
    col=[motif[i] for motif in motifs]
    num=0
    if nucl==0:
        num=len([n for n in col if n=='A'])
    if nucl==1:
        num=len([n for n in col if n=='C'])
    if nucl==2:
        num=len([n for n in col if n=='G'])
    if nucl==3:
        num=len([n for n in col if n=='T'])
    return num

def capitalLetter(motifs,i):
    # find a capital letter of i-th column
    counts=[count(motifs,nucl,i) for nucl in range (0,4)]
    return [nucl for nucl in range (0,4) if counts[nucl]==max(counts)][0]

def score(motifs):
    sc=0
    for i in range(0,len(motifs[0])):
        sc=sc+(len(motifs)-count(motifs,capitalLetter(motifs,i),i))
    return  sc

def RandomizedMotifSearch(dna, k):
    rand_position=[random.randint(0, len(dna[0])-k) for i in range(0,len(dna))]
    
    best_motifs=[]
    motifs=[]
    for i in range(0,len(dna)):
        motifs.append(dna[i][rand_position[i]:rand_position[i]+k])
    best_motifs=motifs
    while True:
        profile=profile_pseudocounts(motifs, k)
        motifs=Motifs(dna, profile, k)
        if score(motifs)<score(best_motifs):
            best_motifs=motifs
        else:
            return best_motifs
        
def RandomizedMotifSearch2(dna, k,N):
    best_motifs=RandomizedMotifSearch(dna,k)
    for i in range ( 1,N):
        motifs=RandomizedMotifSearch(dna,k)
        if score(motifs)<score(best_motifs):
            best_motifs=motifs
    return best_motifs

def patternprob(pattern, profile):
    """return the probability of observing the pattern with the profile matrix"""
    D={"A":0,"C":1,"G":2,"T":3}
    p = 1
    for i,x in enumerate(pattern):
        p = p * profile[D[x]][i]
    
    return p


def ProfileRandomlyGeneratedKmer(text, profile, k):
    import random

    L = []

    for i in range(0, len(text) - k + 1):
        L.append(patternprob(text[i : i + k], profile))
    
    C = sum(L)
    L = [x / C for x in L]

    r = random.uniform(0, 1)
    s = 0
    for ind, x in enumerate(L):
        s = s + x
        if r < s:
            return text[ind : ind + k]
        
def GibbsSampler(dna,k,t,N):
    rand_position=[random.randint(0, len(dna[0])-k) for i in range(0,len(dna))]
    best_motifs=[]
    motifs=[]
    for i in range(0,len(dna)):
        motifs.append(dna[i][rand_position[i]:rand_position[i]+k])
    best_motifs=motifs
    for j in range(1,N):
        i=random.randint(0, len(dna)-1)
        temp=list(motifs)
        temp.pop(i)
        profile=profile_pseudocounts(temp, k)
        
        motifs[i] = ProfileRandomlyGeneratedKmer(dna[i], profile, k)

        if score(motifs) < score(best_motifs):
            best_motifs = list(motifs)
    return best_motifs
    
    

if __name__ == "__main__":
    
    unos=input()
    dna=unos.split("\n")       
    k=15
    t=5
    
    
    
    res = GibbsSampler(dna,k,t,2000)
    
    print("\n".join(res))
    
    
    
    
    
    