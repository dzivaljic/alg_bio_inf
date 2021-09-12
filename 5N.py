
def topologicalOrdering(graph):
    
    lista = []
    outgoing = []
    for v in graph.values():
        outgoing=outgoing+v
    outgoing=set(outgoing)
    candidates=[]
    for k in graph.keys():
        if k not in outgoing:
            candidates.append(k)
    
    while len(candidates)>0:
        a=candidates[0]
        lista.append(a)
        candidates.remove(a)
        if a in graph.keys():
            d=len(graph[a])
            for i in range (d):
                b=graph[a][0]
                graph[a].pop(0)
                outgoing=[]
                for v in graph.values():
                    outgoing = outgoing + v
                outgoing = set(outgoing)
                if b not in outgoing:
                    candidates.append(b)
                        
                    
                
                
    for k in graph.keys():
        if len(graph[k])>0:
            return "the input graph is not a DAG"
    return ", ".join(lista)
            
    
    


if __name__ == "__main__":
    unos=input().split("\n")
    graph={}
    for el in unos:
        graph[el.split(" -> ")[0]]=el.split(" -> ")[1].split(",")
    
    print(topologicalOrdering(graph))
    
    