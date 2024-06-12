import argparse

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("La division par zéro n'est pas permise.")
    return a / b

# Créer le parser
parser = argparse.ArgumentParser(description="Une simple calculatrice en ligne de commande.")

# Ajouter les arguments
parser.add_argument("operation", type=str, choices=["add", "sub", "mul", "div"], help="Opération à effectuer: add, sub, mul, div")
parser.add_argument("nombres", type=float, nargs=2, help="Deux nombres sur lesquels effectuer l'opération")

# Analyser les arguments
args = parser.parse_args()

# Récupérer les arguments
operation = args.operation
nombre1, nombre2 = args.nombres

# Effectuer l'opération
if operation == "add":
    resultat = addition(nombre1, nombre2)
elif operation == "sub":
    resultat = soustraction(nombre1, nombre2)
elif operation == "mul":
    resultat = multiplication(nombre1, nombre2)
elif operation == "div":
    try:
        resultat = division(nombre1, nombre2)
    except ValueError as e:
        print(e)
        exit(1)

# Afficher le résultat
print(f"Le resultat de {operation} entre {nombre1} et {nombre2} est: {resultat}")
