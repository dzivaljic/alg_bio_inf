def k_mer(text,i,k):
    return text[i:i+k]

def hamming_distance(text1,text2):
    br=0
    for i in range(0,len(text1)):
        if(text1[i]!=text2[i]):
            br=br+1
    return br

def distance_between_pattern_and_dna(dna,pattern):
    k=len(pattern)
    distance=0
    for row in dna:
        HD=100000000
        for i in range(0,len(row)-k+1):
            if HD>hamming_distance(k_mer(row,i,k), pattern):
                HD=hamming_distance(k_mer(row,i,k), pattern)
        distance+=HD
    return distance
    
if __name__ == "__main__":
    
    unos=input()
    dna=unos.split(" ")       
    pattern="TGCCGG"
    print(distance_between_pattern_and_dna(dna, pattern))
    
    
    
    
    