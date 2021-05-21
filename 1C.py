def pocetna_mjesta(text,pattern):
    rez=""
    for i in range(0,len(text)-len(pattern),1):
        if(text[i:(len(pattern)+i)]==pattern):
            rez=rez + str(i)+" "
        
        
    return rez




if __name__ == "__main__":

    text = "abababasujhbabadbabaasudhe"
    pattern = "baba"
    res = pocetna_mjesta(text, pattern)
    print(res)