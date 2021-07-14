def GappedPatterns(patterns):
    rez=[]
    for x in patterns:
        rez.append([x.split('|')[0],x.split('|')[1]])
    #print(rez)
    return rez

def stringSpelledByPatterns(patterns):
    string=patterns[0]
    for x in patterns[1:]:
        string=string+x[-1]
    return string

def stringSpelledByGappedPatterns(GappedPatterns,k,d):
    first=[x[0] for x in GappedPatterns]
    second=[x[1] for x in GappedPatterns]
    
    prefix=stringSpelledByPatterns(first)
    suffix=stringSpelledByPatterns(second)
    
    for i in range(k+d+1,len(prefix)):
        if prefix[i]!=suffix[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return prefix+suffix[(len(suffix)-k-d):]
        
    
if __name__ == "__main__":

    

    inlines=input()
    inlines=inlines.split("\n")
    k=50
    d=200
    
    res = stringSpelledByGappedPatterns(GappedPatterns(inlines),k,d)
    
    print(res)