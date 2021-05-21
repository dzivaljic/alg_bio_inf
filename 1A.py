def kmer(text, i, k):

    return text[i : (i + k)]


def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return D


def mostfrequentkmers(text, k):
    D = kmersfrequency(text, k)
    maxcount = max(D.values())
    return dict.fromkeys([x[0] for x in D.items() if x[1] == maxcount], maxcount)

def reversecomplement(text):
    a=""
    for i in text:
        if(i == "A"):
            a=a+"T"
        if (i == "T"):
            a=a+"A"
        if (i == "G"):
            a=a+"C"
        if (i == "C"):
            a=a+"G"

    return a
if __name__ == "__main__":

    text = "ATAG"

    res = mostfrequentkmers(text)
    print("res")


