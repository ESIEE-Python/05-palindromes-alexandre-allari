#### Fonction secondaire
def ispalindrome(p):
    """
    Vérifie si une chaine est un palindrome
    """
    p = p.lower()
    remplacements = {
         "é": "e", ":": "", "-": "", "ê": "e", "à": "a", "ç": "c",
        "ô": "o", "ï": "i", "î": "i", " ": "", ",": "", "è": "e",
        ".": "", "!": "", "?": "", "'": "", "ë": "e"
        }
    a = str.maketrans(remplacements)
    p = p.translate(a)
    return p == p[::-1]

def main():
    """
    Teste la fonction ispalindrome avec une liste de mots
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
