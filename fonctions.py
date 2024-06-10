#fonction factorielle


def facto(n):
    #if n < 0:
        #print ("Le factoriel n'est défini que pour les entiers naturels.")
    if n == 0:
        #print("Par convention factoriel de '0' égal à '1' ")
        return 1
    elif n !=0:
        resultat = 1
        for i in range(1, n + 1):
            resultat *=i
            
        return resultat

        
#Fonction la moyenne d'un intervalle de nombres

def moy(a,b):
    liste= range(a,b+1)
    somme = 0
    for i in range(a,b+1):
        somme += i
    moy = somme/(b-a+1)          
    return moy   

#Fonction palindrome
def supprimer_espaces(phrase):
    return phrase.replace(" ", "")

# Exemple d'utilisation
#phrase = "Bonjour le monde"
#phrase_sans_espaces = supprimer_espaces(phrase)
#print(phrase_sans_espaces)  # Sortie: Bonjourlemonde

#☺fonction sum_length
def sum_length(LL):
    n=len(LL)
    T=0
    for i in range(0,n):
        T+=len(LL[i])
    return T
#

def autre(LL):
    T=0
    for i in LL:
        T+=len(i)
    return T


    
# debut execution

    
if __name__ == "__main__" :
 
    #liste(2,2)
    #print(" autres")
    #♠liste_aubin(2,11)
    #a =3
    #b=4
    #moyenne = moy(a,b)
    #print('la Moyenne des nombres entiers compris entre ',a,'et',b, 'est',moyenne)
  
    s=sum_length([[1], [1, 5, 4], []])
    print(s)
    
    au=autre([[1], [1, 5, 4], []])
    print(au)
    s=sum_length([[0, 1], [2, 3, 4], [5, 6, 7]]) 
    print(s)
