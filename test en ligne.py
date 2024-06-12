#fonction sum_length
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

#NE MODIFIEZ PAS LE CODE EN DESSOUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION

class Personne():
    def __init__(self, nom):
        self.nom = nom

    def vous_faites_quoi(self):
        return f"{self.nom} ne fait rien."

    def comment_vous_vous_appelez(self):
        return f"Je m'appelle {self.nom}."
    
class Etudiant(Personne):
    def __init__(self,nom):
        super().__init__(nom)
    def vous_faites_quoi(self):
        return f"{self.nom} fait son devoir."

    def comment_vous_vous_appelez(self):
        return f"Je m'appelle {self.nom}."
    
#----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------

#class Etudiant    

# Classe de base
#definition classe vehicule
class Vehicule():
    
    counter=0
    def __init__(self,marque, color,immatriculation,position):
        self.nom = marque 
        self.couleur = color
        self.id = immatriculation
        self.position = position
    
    def deplacement(self):
        self.position +=10
        
    def __repr__(self):
        return f"classe Vehicule(marque={self.nom}, color={self.couleur}, immatriculation={self.id}, position={self.position})"
    
    
    def __str__(self):
        return f"Objet de la classe Vehicule(marque={self.nom}, color={self.couleur}, immatriculation={self.id}, position={self.position})"
    
      
        
    @staticmethod
    def vol(x,y):
        print('je suis une methode static')
        
        
        
        
        
        
        
class Velo(Vehicule):
    def __init__(self, marque, color, immatriculation, position, style):
        super().__init__(marque, color, immatriculation, position)
        self.style = style



#Écrire une fonction Python qui affiche les éléments d'une liste.
def func_liste():
    liste = []
    type(liste)



#Écrire une fonction Python qui affiche les éléments d'une liste.
def fL(liste):
    n=len(liste)
    for i in range(0,n):
        #afficher tous les elements de la liste
        l=liste[i]
        #end" " permet de separer les elements par le caracrtere espace
        print(l, end=" ")

 
def f(l):
	for element in l:
		print(element, end=";")
	else:
		print("\nOops, something went wrong...")

#f(list())
#f([x for x in range(3)])
#fL(range(3))



def test_print():

    # voiture = Vehicule("mercedes", "noir", 112, 0)
    #print(voiture.position)
    #voiture.deplacement()
    #print(voiture.position)
    try : 
        
        mary = Personne("Mary")
        f=mary.comment_vous_vous_appelez()
        g=mary.vous_faites_quoi()
        print(f)

        print(g)
       
    
        tata = Etudiant("betty")
        f=tata.comment_vous_vous_appelez()
        g=tata.vous_faites_quoi()
        print(f)
        print(g)
        
    except Exception as e:
        print ( 'error happens : ', e)
        
    except ZeroDivisionError:
        # Code block to handle a specific exception (in this case, division by zero)
        print("Error: Cannot divide by zero!")

    except ValueError:
        # Code block to handle a specific exception (in this case, invalid input)
        print("Error: Invalid input! Please enter a valid number.")
        
    finally:
        print ( 'finally ')
        
        
        

if __name__ == "__main__" : 
   #Yaris = Vehicule("Toyota", "blanche", "0782" , 0)
   #VTT= Velo.Vehicule("honda","rouge")

    # Utilisation de __repr__() et __str__()
    #print(repr(Yaris))
    #print(str(Yaris))
    
    aub = -5
    
    if (aub) : 
        print ( "on est true")
    else : 
        print ("on est false")
    
    
 
   
    
    
