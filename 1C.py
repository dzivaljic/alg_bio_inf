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

    return a[::-1]


if __name__ == "__main__":

    text = "AAAACCCGGT"

    res = reversecomplement(text)
    print(res)
