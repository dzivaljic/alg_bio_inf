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

def LinearSpectrum(peptide):
    subPeptides=['',peptide]
    
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subPeptides.append(peptide[j:j+i])
    
    spectrum=[]
    for x in subPeptides:
        spectrum.append(Mass(x))
    
    return sorted(spectrum)
    
def Score(peptide,Spectrum):
    kopija=Spectrum
    for i in range(0,len(Spectrum)):
        kopija[i]=int(Spectrum[i])
    br=0
    for value in LinearSpectrum(peptide):
        if value in kopija:
            br+=1
            kopija.remove(value)
    return br

def Trim(leaderboard, spectrum,N):
    LinearScores=[]
    for j in range(0,len(leaderboard)):
        peptide=leaderboard[j]
        LinearScores.append(Score(peptide, spectrum))
    print("stari leaderboard")
    print(leaderboard)
        ############ ovaj sad dio neznam #############
    LinearScores, leaderboard = (list(t) for t in zip(*sorted(zip(LinearScores, leaderboard),reverse=True)))
    
    print("novi leaderboard")
    print(leaderboard)
    print("novi linearscores")
    print(LinearScores)
    
    for j in range(N, len(leaderboard)):
        if LinearScores[j]<LinearScores[N-1]:
            leaderboard.remove(leaderboard[j])
        break
        
            
    return leaderboard[0:N]
    
        
    
if __name__ == "__main__":

    
    unos=input().split("\n")
    leaderboard=unos[0].split(" ")
    spectrum=unos[1].split(" ")
    N=int(unos[2])
    res=Trim(leaderboard, spectrum,N)
    
    print(" ".join(res))