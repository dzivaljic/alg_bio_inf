def k_mer(text,i,k):
    return text[i:i+k]

def composition_k(text,k):
    rez = [text[i:i+k] for i in range(0,len(text)-k+1)]
    return sorted(rez)

    
if __name__ == "__main__":
    
    text=input()
          
    k=50
    print("\n".join(composition_k(text, k)))
    