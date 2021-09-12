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

    
    unos=input().split("\n")
    M=int(unos[0])
    N=int(unos[1])
    spectrum=unos[2].split(" ")
   
    convolution=spectralConvolution(spectrum)
    br=0
    Leaderboard=[]
    while br<M:
        if int(convolution[br])>=57 and int(convolution[br])<=200:
            Leaderboard.append(int(convolution[br]))
            br+=1
        
    br2=0
    res=[]
    while br2<N:
        if int(Leaderboard[br2])>=57 and int(Leaderboard[br2])<=200:
            res.append(int(Leaderboard[br2]))
            br2+=1
        
    file1 = open("MyFile.txt", "w") 
    file1.write("-".join(res))
    file1.close()
    