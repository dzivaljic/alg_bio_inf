def string_spelled(dna):
    rez=""
    rez=dna[0]+"".join([x[-1] for x in dna[1:]])
    return rez
if __name__ == "__main__":
    
    unos=input()
    dna=unos.split("\n")       
    
    print(string_spelled(dna))