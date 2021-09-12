def kmer(text, i, k):

    return text[i : (i + k)]

def reverse_complement(text):
    rez=""
    for x in text:
        if x=="A":
            rez+="T"
        if x=="T":
            rez+="A"
        if x=="G":
            rez+="C"
        if x=="C":
            rez+="G"
            
    return rez[::-1]

def shared(dna1,dna2,k):
    br=[]
    
    for i in range (0,len(dna1)-k+1):
        for j in range (0,len(dna2)-k+1):
            if kmer(dna1, i, k) == kmer(dna2, j, k) or kmer(dna1, i, k) == reverse_complement(kmer(dna2, j, k)):
                br.append([i,j])
    return br


if __name__ == "__main__":
    
   ulaz=input().split("\n")
   k=int(ulaz[0])
   dna1=ulaz[1]
   dna2=ulaz[2]
   res=shared(dna1, dna2, k)
   file1 = open('myfile.txt', 'w')
   red=""
   for x in res:
       red+="("+str(x[0])+","+str(x[1])+")"+"\n"
   file1.write(red)
   file1.close()
   
   