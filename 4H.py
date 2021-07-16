def spectralConvolution(spectrum):
    rez=[]
    for x in spectrum:
        for y in spectrum:
            if int(x)>int(y):
                rez.append(int(x)-int(y))
    res=[]
    for i in range(0,len(rez)):
        res.append(str(rez[i]))
        
    return sorted(res)


if __name__ == "__main__":

    
    unos=input().split(" ")
   
    res=spectralConvolution(unos)
    file1 = open("MyFile.txt", "w") 
    file1.write(" ".join(res))
    file1.close()
    