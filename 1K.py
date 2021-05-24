def PatternToNumber(pattern):
    rez=0
    if(pattern=="A"):
        return 0
    if(pattern=="C"):
        return 1
    if(pattern=="G"):
        return 2
    if(pattern=="T"):
        return 3
    rez +=4*PatternToNumber(pattern[0:len(pattern)-1]) + PatternToNumber(pattern[len(pattern)-1])
        
    return rez
        
def kmer(text, i, k):

    return text[i : (i + k)]

def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return D

def computing_freq(text,k):
    rez=[]
    D=kmersfrequency(text, k)
    for i in range(0,4**k):
        rez.append(0)
    for i in D.keys():
        rez[PatternToNumber(i)]=D[i]
    return rez
        

if __name__ == "__main__":

    text="AAA"
    k=2

    res = computing_freq(text,k)
    print(res)