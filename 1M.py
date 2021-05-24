
def NumberToPattern(number,k):
    rez=""
    D={0:"A",1:"C",2:"G",3:"T"}
    for i in range(0,k):
        rez+=str(D[number%4])
        number=number//4
    return rez[::-1]
        
        


if __name__ == "__main__":

    

    res = NumberToPattern(8894,8)
    print(res)