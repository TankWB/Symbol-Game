#William Breton et Alexandre Orsoni
#08/08/2022

#IFT1015 - Programmation I

#TP2

import random

#On crée l'enregistrement de nos images et dimensions.

class image:
    cercleIm='<img src= "symboles/circle.svg">'
    triangleIm='<img src="symboles/pyramide.svg">'
    cubeIm='<img src= "symboles/cube.svg">'
    etoileIm='<img src= "symboles/star.svg">'
    pentaIm='<img src= "symboles/penta.svg">' 
                    
class tailleGrille:
    x = 6
    y = 6

#Les choix de l'usager

reponse = ''

#Avant de faire son choix initial.

hasClicked = False

#Fonctions qui produit des tableau «vides».

def creerTableau(tailleGrille):
    
    grille = [False] * tailleGrille.y
    
    for i in range(tailleGrille.y):
        
        grille[i] = [False] * tailleGrille.x
        
    return grille

def creerTableauReponse(tailleGrille):
    
    tab = [''] * tailleGrille.y
    
    for i in range(tailleGrille.y):
        
        tab[i] = [''] * tailleGrille.x
        
    return tab

#On postionne aléaoirement un chiffre de 0 à 4, qui est associé à un item.

def tableauAleatoire(tailleGrille,grille):
    
    for i in range(tailleGrille.x-1):
        
        for j in range(tailleGrille.y-1):
            
            grille[i][j] = round(random.random()*4)
    
    return grille


#Fonction qui place les valeurs de chaque item et les insères
#dans la grille. De plus, la somme des lignes est placée
#sur une grille de valeurs.

def tableauVariables(tailleGrille, grilleValeur, grille):
    
    cercle = round(random.random()*19+1)
    
    triangle = round(random.random()*19+1)
    
    cube = round(random.random()*19+1)
    
    etoile = round(random.random()*19+1)
    
    penta = round(random.random()*19+1)
    
    
      
    for i in range(tailleGrille.x-1):
      
        for j in range(tailleGrille.y-1):
            
            if grille[i][j] == 0:
                
                grilleValeur[i][j] = cercle
                
            elif grille[i][j] == 1:
                
                grilleValeur[i][j] = triangle
                
            elif grille[i][j] == 2:
                
                grilleValeur[i][j] = cube
                
            elif grille[i][j]==3:
                
                grilleValeur[i][j] = etoile
                
            elif grille[i][j]==4:
                
                grilleValeur[i][j] = penta

        #On ajoute la somme des lignes au dernier élément de chaque ligne.
                
    for _ in range (tailleGrille.y-1):

        for s in range(tailleGrille.x-1):
            
            #On additionne les valeurs chaque ligne.
            
            grilleValeur[_][tailleGrille.x-1] =\
            grilleValeur[_][tailleGrille.x-1] + grilleValeur[_][s]

    for t in range(tailleGrille.x-1):

        for i in range(tailleGrille.y-1):

            grilleValeur[tailleGrille.y-1][t] =\
            grilleValeur[tailleGrille.y-1][t] + grilleValeur[i][t]


    return grilleValeur    


#Le recalcul de la somme à la suite d'un choix.

def somme(tailleGrille, grilleValeur):

    for _ in range (tailleGrille.y-1):
        
        grilleValeur[_][tailleGrille.x-1]= 0

    for t in range(tailleGrille.x-1):
         
        grilleValeur[tailleGrille.y-1][t] = 0


    for _ in range (tailleGrille.y-1):
        

        for s in range(tailleGrille.x-1):
            
            #On additionne les valeurs chaque ligne.
               
            grilleValeur[_][tailleGrille.x-1] =\
            grilleValeur[_][tailleGrille.x-1] + grilleValeur[_][s]

    for t in range(tailleGrille.x-1):
         

        for i in range(tailleGrille.y-1):

            #On additionne les valeurs chaque colonne.
            
            grilleValeur[tailleGrille.y-1][t] =\
            grilleValeur[tailleGrille.y-1][t] + grilleValeur[i][t]


    return grilleValeur    

    
#Tableau qui sera affiché contenant les images appropriées.

def tableauImage(tailleGrille, grilleImage, grille):
    
    for i in range(tailleGrille.x-1):
        
        for j in range(tailleGrille.y-1):
            
            if grille[i][j] == 0:
                
                grilleImage[i][j] = image.cercleIm
                
            if grille[i][j] == 1:
                
                grilleImage[i][j] = image.triangleIm
                
            if grille[i][j] == 2:
                
                grilleImage[i][j] = image.cubeIm
                
            if grille[i][j]==3:
                
                grilleImage[i][j] = image.etoileIm
                
            if grille[i][j]==4:
                
                grilleImage[i][j] = image.pentaIm

    #Déclaration de la fonction qui
    #sera utilisé à la suite d'un choix
                
    victoire(tailleGrille, grilleValeur)
    
    return grilleImage


  
# Fonction qui vérifie si l'usager a perdu ou gagné
#et qui affiche le message approprié.

def victoire (tailleGrille, grilleValeur):

    global message

    bool = True

    for l in range (tailleGrille.y-1):

        if bool:

            for k in range (tailleGrille.x-1):
        
                
                if grilleValeur[l][tailleGrille.x-1]< 0\
                or grilleValeur[tailleGrille.y-1][k] < 0:
            
                    message = "Vous avez perdu"

                    #booléen qui termine la boucle.

                    bool = False

                    break
                
                elif grilleValeur[l][tailleGrille.x-1] == 0\
                and grilleValeur[tailleGrille.y-1][k] == 0:
            
                    message = "Vous avez gagné!"
            
                else:
            
                    message = "Jouer!"

    return message

#On déclare notre tableau des choix de l'usager.

tab=creerTableauReponse(tailleGrille)

#Procédure qui gère les actions à la suite
#d'un click par l'usager. Soit si son choix
#est acceptable ainsi que l'ajout de ses choix
#dans le tableau tab.

def click(y,x):

    global tab, hasClicked, message
    
    if message == "Vous avez perdu" or message == "Vous avez gagné!":
        
        return

    
    entree = prompt("Veuillez entrer un nombre entre 1 et 20")

    #Si l'usager sélectionne «Annuler»
    
    if entree== None :
        
        return
    
    #On vérifie que le choix est un nombre entier et
    #entre 1 et 20 inclusivement.
    
    elif entree.isdecimal() and int(entree)>= 1 and int(entree) <= 20:

        reponse = int(entree)

    else:

        #Sinon on le relance.
        
        while entree== None or (entree.isdecimal() == False) or\
        (int(entree) < 1) or (int(entree) > 20):

            entree = prompt('Veuillez entrer un nombre valide '\
                            "dans l'intervalle spécifié")

        reponse = int(entree)

    #On ajuste chaque élément du tableau qui contient l'image
    #sur laquelle l'usager a clické.
    #Ainsi que le tableau qui contient les valeurs et
    #celui qui enregistre le choix.
        
    for i in range(tailleGrille.x-1):
        
        for j in range(tailleGrille.y-1):

            if grilleImage[i][j]==image.cercleIm and\
            grilleImage[y][x]==image.cercleIm :
                    
                grilleValeur[i][j]= grilleValeur[i][j]-reponse

                if tab[i][j]!='':

                    grilleValeur[i][j]+= tab[i][j]

                tab[i][j]= reponse

            if grilleImage[i][j]==image.triangleIm and\
            grilleImage[y][x]==image.triangleIm:
                    
                grilleValeur[i][j]=grilleValeur[i][j]-reponse

                if tab[i][j]!='':

                    grilleValeur[i][j]+= tab[i][j]

                tab[i][j]= reponse
               

            if grilleImage[i][j]==image.cubeIm and\
            grilleImage[y][x]==image.cubeIm:
                    
                grilleValeur[i][j]=grilleValeur[i][j]-reponse

                if tab[i][j]!='':

                    grilleValeur[i][j]+= tab[i][j]

                tab[i][j]= reponse
               

            if grilleImage[i][j]==image.etoileIm and\
            grilleImage[y][x]==image.etoileIm:
                    
                grilleValeur[i][j]=grilleValeur[i][j]-reponse

                if tab[i][j]!='':

                    grilleValeur[i][j]+= tab[i][j]

                tab[i][j]= reponse

            if grilleImage[i][j]==image.pentaIm and\
            grilleImage[y][x]==image.pentaIm:
                    
                grilleValeur[i][j]=grilleValeur[i][j]-reponse

                if tab[i][j]!='':

                    grilleValeur[i][j]+= tab[i][j]

                tab[i][j]= reponse
    #On recalcul la somme des éléments des rangés et des colonnes.
                
    somme(tailleGrille, grilleValeur)
    
    #On vérifie si le choix fait est un choix gagant.
    
    victoire(tailleGrille, grilleValeur)

#    print(grilleValeur)

    reponse = str(reponse)
   
    init()

#Afin d'offrir la possbiilté de recommancer le jeu,
#la fonction nouvellePartie re-reroule le code avec des
#tableaux vides. Ensuite elle à la même fonction
#que la fonction jeu(tailleGrille).

def nouvellePartie():
    
    global grille, grilleValeur, grilleImage, hasClicked, tab

    grille=creerTableau(tailleGrille)
    
    grilleValeur = creerTableau(tailleGrille)
    
    grilleImage = creerTableau(tailleGrille)
        
    tableauAleatoire(tailleGrille,grille)

    tableauVariables(tailleGrille,grilleValeur, grille)

    grilleInput = grilleValeur

    tableauImage(tailleGrille,grilleImage, grille)

    tab=creerTableauReponse(tailleGrille)

    init()

#Fonction qui initialise le jeu.
    
def jeu(tailleGrille):  
    
    global grilleValeur, grilleImage, grilleInput, hasClicked

    grille = creerTableau(tailleGrille)
    
    grilleValeur = creerTableau(tailleGrille)
    
    grilleImage = creerTableau(tailleGrille)

    grilleInput = grilleValeur
    
    tableauAleatoire(tailleGrille,grille)
        
    tableauVariables(tailleGrille,grilleValeur, grille)

    grilleInput = grilleValeur

    tableauImage(tailleGrille,grilleImage, grille)

    
    
    return grilleImage, grilleInput

    init()

jeu(tailleGrille)

#Procédure qui contient le code HTML afin d'afficher
#le jeu.

def init():
    
    global tab
 
    main = document.querySelector("#main")
    
    body = """<!DOCTYPE html>
              <meta charset="UFT-8">
              <html>
              
              <style>
              #jeu table { float: none; }
              #jeu table td {
              border: 1px solid black;
              padding: 1px 2px;
              width: 80px;
              height: 80px;
              font-family: Helvetica;
              font-size: 20px;
              text-align: center;
              }
              #jeu table td img {
              display: block;
              margin-left: auto;
              margin-right: auto;
              object-fit: contain;
              width: 80%;
              height: 80%;
              }
              .centered {
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%,-50%);
              }
              .container {
              position: relative;
              width:100%;
              height: 100%;
              }
              </style>             
              <div><button onclick="nouvellePartie()">Nouvelle partie
              </button></div>
              <div><h1 style="color : red">""" + message + """
              </h1>
              </div><div><table>"""
    
    for i in range(tailleGrille.y):
        
        if i != (tailleGrille.y - 1):
        
            body += "<tr>"
        
            for j in range(tailleGrille.x):
            
                if j != (tailleGrille.x - 1):
                    
                    body += "<td><div class='container'><button class='btn'"\
                    "onclick='click("+ str(i) + ',' + str(j) +")' >"\
                    + grilleImage[i][j] +"<div class='centered'>"\
                    +str(tab[i][j])+"</div></div></button></td>"
                
                else:
                    
                    body += "<td>"+ str(grilleValeur[i][j]) + "</td></tr>"
                    
        else:
            
            body += "<tr>"
            
            for k in range(tailleGrille.x):
                
                if k != (tailleGrille.x - 1):
                    
                    body += "<td>"+ str(grilleValeur[i][k])+"</td>"
                    
                else:
                    
                    body += "<td></td></tr></table></div></html>"
            
    
    main.innerHTML = body



    
