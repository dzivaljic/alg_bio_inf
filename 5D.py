
def rek(tree,start,kraj,put,tank):
    
    if kraj==start:
        tank.append(put)
        return 
    
    if start not in tree.keys():
        return
    
    for x in tree[start]:
        new=put.copy()
        
        if start not in new:
            new.append(start)
        new.append(x)
        rek(tree,x,kraj,new,tank)
        
    return tank
        
    
    
    
if __name__ == "__main__":
    unos=input().split("\n")
    start=unos[0]
    kraj=unos[1]
    
    tree={}
    for i in range(2,len(unos)):
        x=unos[i].split("->")[0]
        y=unos[i].split("->")[1][0]
       
        if x not in tree.keys():
            tree[x]=[]
            tree[x].append(y)
        else:
            tree[x].append(y)
            
    putevi=[]
    for el in rek(tree, start, kraj, [], []):
        putevi.append("->".join(el))
        
    tezine=dict()
    tez_value=[]
    for i in range(2,len(unos)):
        tezine[unos[i].split(":")[0]]=unos[i].split(":")[1]
    
    for put in putevi:
        s=0
        for i in range(0,len(put)-1,3):
            s+=int(tezine[put[i:i+4]])
        tez_value.append(s)
    maksimum=max(tez_value)
    
    i=tez_value.index(maksimum)
    
    print(maksimum)
    print(putevi[i])
    
        
    
    
        
        
    
        
   