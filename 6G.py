def CycleToChromosome(nodes):
    chromosome=[]
    for j in range(0,int(len(nodes)/2)):
        
        if int(nodes[2*j])<int(nodes[2*j+1]):
            chromosome.append(int(nodes[2*j+1]/2))
        else:
            chromosome.append(int(-nodes[2*j]/2))
    return chromosome
    

if __name__ == "__main__":

    
    
    chromosome =input()[1:-1].split(" ")
    kop=[]
    for x in chromosome:
        kop.append(int(x))
    res=CycleToChromosome(kop)

    for i in range (len(res)):
        res[i]=str(res[i])
    res=" ".join(res)
    res="("+res+")"
    print(res)