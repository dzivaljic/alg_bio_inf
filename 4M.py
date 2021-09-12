import itertools

def all_diferences(a):
    res=[]
    for x in a:
        for y in a:
            res.append(int(x)-int(y))
            
    return sorted(res)

        

def turnpike(ulaz,n):
    temp=list(itertools.combinations(ulaz,n-2))
    kopija=[]
    for x in ulaz:
        kopija.append(int(x))
    for x in temp:
        new_set=[]
        new_set.append(kopija[-1])
        new_set.append(0)
        for y in x:
            new_set.append(int(y))
        new_set.sort()
        if(all_diferences(new_set)==kopija):
            return new_set
    return None
    

if __name__ == "__main__":
    ulaz=input().split(" ")
    br=0
    for x in ulaz:
        if int(x)==0:
            br+=1
    file1 = open('myfile.txt', 'w')
    file1.write(str(turnpike(ulaz, br)))
    file1.close()
    
   
   
       
   
 
    
    
           

   
   