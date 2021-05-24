
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
        


if __name__ == "__main__":

    pattern="TGGGTTTGTCCTGTGTCTTATC"
    

    res = PatternToNumber(pattern)
    print(res)