def fja(money,coins):
    br=0
    i=0
    while money>0:
        while money-coins[i]>=0:
            br+=1
            money=money-coins[i]
        else:
            i=i+1
    return br
    
    
def Change(money, coins):
    coins=sorted(coins,reverse=True)
    rez=[]
    for i in range(0,len(coins)):
        kopija=coins[i:]
        rez.append(fja(money,kopija))
        
            
        
    return min(rez)
    
if __name__ == "__main__":

    
    unos=input().split("\n")
    money=int(unos[0])
    coins=unos[1].split(",")
    new=[]
    for x in coins:
        new.append(int(x))
        
    
    print(Change(money, new))
    
    
    