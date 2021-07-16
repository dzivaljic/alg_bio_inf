def ChromosomeToCycle(chromosome):
    nodes=[]
    for j in range(0,len(chromosome)):
        i=int(chromosome[j])
        if i>0:
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)
            nodes.append(-2*i-1)
    return nodes

if __name__ == "__main__":

    
    
    chromosome =input()[1:-1].split(" ")
    res=ChromosomeToCycle(chromosome)

    for i in range (len(res)):
        res[i]=str(res[i])
    res=" ".join(res)
    res="("+res+")"
    print(res)