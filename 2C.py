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
       
                       


if __name__ == "__main__":
    
    unos=input()
    redak=unos.split("\n")
    matrica=[redak[0].split(" "),redak[1].split(" "),redak[2].split(" "),redak[3].split(" ")]
    text="ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"              
    k=5
    
    
    res = profile_most_probable(text, k,matrica)
    
    print(res)