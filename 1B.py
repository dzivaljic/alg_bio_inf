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


if __name__ == "__main__":

    text = "abababasujhdasudhe"
    pattern = 5
    res = mostfrequentkmers(text, pattern)
    print(res)










