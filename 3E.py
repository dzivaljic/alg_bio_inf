def prefix(pattern):
    return pattern[:len(pattern)-1]

def suffix(pattern):
    return pattern[1:]

def deBrujin(patterns):
    rez=dict()
    sort_patterns=sorted(patterns)
    for row in sort_patterns:
        rez[prefix(row)]=[]
    for row in sort_patterns:
        rez[prefix(row)].append(suffix(row))
    return rez
        
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
        file1.writelines(key+'->'+",".join(sorted(adj[key]))+"\n")
            
if __name__ == "__main__":
    
    file1 = open('myfile.txt', 'w')
    patterns=input()
    patterns=patterns.split("\n")
    k=12
    print_graph(deBrujin(patterns))
    file1.close()
    