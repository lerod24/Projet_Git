# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 00:08:25 2024

@author: Mekmotech_admin
"""

#definition des fonctions

#fonction somme

def somme(a, b) : 
    temp = a +b
    return temp

#fonction factorielle


def facto(n):
    if n < 0:
        print ("Le factoriel n'est défini que pour les entiers naturels.")
    elif n == 0:
        print("Par convention factoriel de '0' égal à '1' ")
        return 1
    elif n !=0:
        resultat = 1
        for i in range(1, n + 1):
            resultat = resultat*i
            
        return resultat

  





def liste(a,b):
    
    # inverser a et b quand b < a
    if a > b : 
        a,b=b,a

    # Creer la liste des paire et des impaires en fonction de la parite de a  
    if a% 2==0:
        liste_pair = range(a,b+1,2)
        liste_impair = range(a+1,b+1,2)
    elif a% 2!=0:
        liste_impair = range(a,b+1,2)
        liste_pair = range(a+1,b+1,2)
        
    # affichage
    print('impair =', list(liste_impair))
    print('pair', list(liste_pair))
    
    
def liste_aubin(a,b):
    liste_pair = []
    liste_impair = []
    
    if a > b : 
        a,b=b,a
    
    init = range(a,b+1)
    
    for i in init :
        if (i %2 == 0) : 
           liste_pair.append(i)
        else : 
            liste_impair.append(i)
            
    print('impair =', list(liste_impair))
    
    print('pair', list(liste_pair))
        
    
    
    # debut execution
    
    
if __name__ == "__main__" :
 
    liste(11,11)
    print(" autres")
    liste_aubin(11,11)



