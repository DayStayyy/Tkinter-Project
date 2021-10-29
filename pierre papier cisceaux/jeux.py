from tkinter import *
from random import randint

fenetre = Tk()
fenetre.title("Pierre Papier Cisceaux")
#Taille de la fenetre
fenetre.geometry("490x400")

#Init images boutons
image_pierre = PhotoImage(file="Pierre.png")
image_papier = PhotoImage(file="Papier.png")
image_cisceaux = PhotoImage(file="Cisceaux.png")

texte_1 = Label(fenetre, text="Faites votre choix", font=(None, 20), height=4)
boutton_pierre = Button(fenetre, image=image_pierre,command= lambda j=0 : play(j))
boutton_papier = Button(fenetre, image=image_papier,command= lambda j=1 : play(j))
boutton_cisceaux = Button(fenetre, image=image_cisceaux,command= lambda j=2 : play(j))

boutton_pierre.pack()
boutton_papier.pack()
boutton_cisceaux.pack()

u=0

#Init class elements
class elements() :
    def __init__(self, image):
            self.image = image


#Crea des elements        
Pierre = elements(image_pierre)
Papier = elements(image_papier)     
Cisceaux = elements(image_cisceaux)

liste = [Pierre,Papier,Cisceaux]


bouton_joueur = Button(fenetre)
bouton_bot = Button(fenetre)
texte_2 = Label(fenetre)



#Init classe joueurs
class Joueur(object):

    def __init__(self):
        self.score = 0
        self.choix = 0

#Crea des 2 joueurs        
joueur = Joueur()
bot = Joueur()

def bot_choix():
    resultats = randint(0,2)
    return(resultats)

def test_resultat(bot, joueur) :
    if joueur == bot :
        texte = "Egalité"
        return(texte,0, 210)
    elif joueur > bot :
        if joueur == 2 and bot == 0 :
            texte = "Le bot a gagner"
            return(texte,2,150)
        else :
            texte= "Le joueur a gagner"
            return(texte,1,145)
    else :
        if joueur == 0 and bot == 2 :
            texte = "Le joueur a gagner"
            return(texte,1,145)
        else :
            texte = "Le bot a gagner"
            return(texte,2,150)

def supprimer():
    boutton_pierre.place(x=5000, y=570)
    boutton_papier.place(x=5000, y=570)
    boutton_cisceaux.place(x=500, y=570)
    texte_1.place(x=500, y=570)

def aff_resultats(joueur, bot, texte, u):
    global bouton_joueur
    bouton_joueur = Button(fenetre, image=liste[joueur].image)
    bouton_joueur.pack()
    bouton_joueur.place(x=90, y=270)

    global bouton_bot
    bouton_bot = Button(fenetre, image=liste[bot].image)
    bouton_bot.pack()
    bouton_bot.place(x=290, y=270)

    global texte_2
    texte_2 = Label(fenetre, text=texte, font=(None, 20), height=4)
    texte_2.pack()
    texte_2.place(x=u, y=10)


def recommencer() :
    bouton_bot.place(x=500, y=570)
    bouton_joueur.place(x=500, y=570)
    texte_2.place(x=500, y=570)
    aff_menu()
    boutton_reco.place(x=500, y=500)

def play (j):
    resultat = bot_choix()
    text, score_i, u = test_resultat(resultat,j)
    if score_i == 1 :
        joueur.score += 1
    elif score_i == 2 :
        bot.score += 1
    supprimer()
    aff_resultats(j, resultat, text, u)
    score()
    boutton_reco.place(x=154, y=200)


def score():
    texte_score = (" Score \n{0} : {1}").format(joueur.score,bot.score)
    #Aff du score
    affichage_score = Label(fenetre, text=texte_score, font=(None, 20))
    affichage_score.pack()
    affichage_score.place(x=205, y=100)

score()


def aff_menu() :
    #Texte 1
    texte_1.place(x=145, y=10)

    #Init des boutons
    boutton_pierre.place(x=30, y=270)
    boutton_papier.place(x=190, y=270)
    boutton_cisceaux.place(x=350, y=270)


boutton_reco = Button(fenetre, text="Cliquez ici\npour lancer une nouvelle manche", command=lambda  g=4: recommencer())
boutton_reco.pack()
boutton_reco.place(x=900, y=900)

score()
aff_menu()




fenetre.mainloop()
