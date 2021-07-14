def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }
    return mass

def Mass(peptide):
    sum=0
    mase=get_amino_acid_mass()
    for x in peptide:
        sum+=mase[x]
    return sum

def CycloSpectrumlist(peptide):
    subPeptides=['',peptide]
    var=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subPeptides.append(var[j:j+i])
    
    spectrum=[]
    for x in subPeptides:
        spectrum.append(Mass(x))
    
    return sorted(spectrum)
    
def Score(peptide,Spectrum):
    kopija=Spectrum
    for i in range(0,len(Spectrum)):
        kopija[i]=int(Spectrum[i])
    br=0
    for value in CycloSpectrumlist(peptide):
        if value in kopija:
            br+=1
            kopija.remove(value)
    return br
    
if __name__ == "__main__":

    
    unos=input().split("\n")
    peptide=unos[0]
    Spectrum=unos[1].split(" ")
    res=Score(peptide, Spectrum)
    
    print(res)