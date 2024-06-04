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
    
# debut execution

    
if __name__ == "__main__" :
 
    #liste(2,2)
    #print(" autres")
    #♠liste_aubin(2,11)
    a =3
    b=4
    moyenne = moy(a,b)
    print('la Moyenne des nombres entiers compris entre ',a,'et',b, 'est',moyenne)
  
        
#