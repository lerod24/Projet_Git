import argparse
contact_list =list()

def ajout(nom, tel, email):
        element1 =[nom, tel, email]
        contact_list.append(element1)

def recherche(element):
    if element in contact_list:
        i=contact_list.index(element)
        return i 

def suppression(nom, tel, email):
    ellement_a_supprimer  = [nom, tel, email]
    index = recherche(ellement_a_supprimer)
    contact_list.pop(index)
    #contact_list.remove(ellement_a_supprimer)


def affichage(nom, tel, email):
    
    valeur_a_afficher =  f"{nom}, {tel}, {email}"
    print (valeur_a_afficher)




# Créer le parser
parser = argparse.ArgumentParser(description="Gestionnaire de contact en ligne de commande")

# Ajouter les arguments
parser.add_argument("operation", type=str, choices=["ajout", "suppression", "recherche", "affichage"], help="Opération à effectuer: ajout, suppression, recherche, affichage")
parser.add_argument("parametres", type=str, nargs=3, help="3 param representant le nom, le telephone et email du contact")

# Analyser les arguments
args = parser.parse_args()

# Récupérer les arguments
operation = args.operation
nom, telephone, email = args.parametres

# Effectuer l'opération
if operation == "ajout":
    ajout(nom, telephone, email)
    ajout("dalya", "060606", "dal@yahoo.cm")
    print(contact_list)
    
if operation == "suppression":
    # charger notre liste de contact
    ajout("dalya", "060606", "dal@yahoo.cm")
    ajout("dalya1", "060606", "dal@yahoo.cm")
    ajout("dalya2", "060606", "dal@yahoo.cm")
    ajout(nom, telephone, email)
    print(contact_list)
    
    #suppremer un contact de la liste
    suppression(nom, telephone, email)
    print(contact_list)

if operation == "affichage":
    affichage(nom, telephone, email)
    affichage("dalya2", "060606", "dal@yahoo.cm")
    

'''

elif operation == "affichage":
    resultat = AfficherContact(nom, numero, email)
elif operation == "recherche":
    resultat = RechercheContact(nom)
'''
        




