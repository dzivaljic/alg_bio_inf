def LCSBactrack(v,w):
    s=[]
    for i in range(0,len(v)+1):
        s.append([0])
    for j in range(1,len(w)+1):
        s[0].append(0)
        
    Backtrack=[]
    for i in range(0,len(v)):
        Backtrack.append([])
    
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            if v[i-1]==w[j-1]:
                s[i].append(max([s[i-1][j],s[i][j-1],s[i-1][j-1]+1]))
            else:
                s[i].append(max([s[i - 1][j], s[i][j - 1],s[i-1][j-1]]))
            if s[i][j]==s[i-1][j]:
                Backtrack[i-1].append("D")
            else:
                if s[i][j] == s[i][j-1]:
                    Backtrack[i-1].append("R")
                else:
                    Backtrack[i-1].append("Diag")
    return Backtrack

def outputLCS(Backtrack, v,i,j,path):
    if i==-1 or j==-1:
        print(path[::-1])
        return
    if Backtrack[i][j]=="D":
        outputLCS(Backtrack, v,i-1,j,path)
    elif Backtrack[i][j]=="R":
        outputLCS(Backtrack, v,i,j-1,path)
    else:
        path=path+v[i]
        outputLCS(Backtrack, v,i-1,j-1,path)
        
        


if __name__ == "__main__":
    unos=input().split("\n")
    v=unos[0]
    w=unos[1]
    outputLCS(LCSBactrack(v, w), v, len(v)-1, len(w)-1, "")
    
    