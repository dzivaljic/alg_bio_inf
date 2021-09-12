def breakPoints(P):
    n=0
    for i in range (len(P)-1):
        if (P[i+1]-P[i])!=1:
            n=n+1
    return n

if __name__ == "__main__":
    
    P = [0]
    S = input()[1:-1].split(" ")
    P=P+S
   
    for i in range(0, len(P)):
        P[i] = int(P[i])
    P.append(len(P))
    res = breakPoints(P)
    print(res)