def deBrujinGraph(text,k):
    rez={}
    for i in range(0,len(text)-k+1):
        first=text[i:i+k-1]
        second=text[i+1:i+k]
        if first not in rez:
            rez[first]=[second]
        else:
            rez[first].append(second)
    return rez

def print_graph(adj):
    for key in sorted(adj.keys()):
        #print(key,'->',",".join(sorted(adj[key])))
        file1.writelines(key+'->'+",".join(sorted(adj[key]))+"\n")
            
if __name__ == "__main__":
    
    file1 = open('myfile.txt', 'w')
    text=input()
    k=12
    print_graph(deBrujinGraph(text, k))
    file1.close()
    