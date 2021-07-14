def prefix(pattern):
    return pattern[:len(pattern)-1]

def suffix(pattern):
    return pattern[1:]

def overlapGraph(dna):
    rez=dict()
    dna.sort()
    for row in dna:
        rez[row]=[x for x in dna if suffix(row)==prefix(x)]
    return rez

def adj_print(rez):
    for x in rez.keys():
        if(len(rez[x])>0):
            for i in range (0,len(rez[x])):
                print(x, "->",rez[x][i])
    
if __name__ == "__main__":
    
   unos=input()
   dna=unos.split("\n")       
    
   adj_print(overlapGraph(dna))