from tkinter import *

class Interface(Frame):

    """Notre fenetre principale.
    Tous les widgets sont stockes comme attributs de cette fenetre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=580, height=500, **kwargs)
        self.pack()

        #On init nos liste et variable global dans la class
        etage = 0
        self.joueur_num = 0
        self.liste_colonnes = [etage,etage,etage,etage,etage,etage,etage]
        self.liste_image =[image_jaune,image_rouge]



        #Para permettant la verif de la victoire
        etage_0 = 0
        etage_1 = 0
        etage_2 = 0
        etage_3 = 0
        etage_4 = 0
        etage_5 = 0
        etage_6 = 0
        colonne_0 = [" ", " ", " ", " ", " ", " "]
        colonne_1 = [" ", " ", " ", " ", " ", " "]
        colonne_2 = [" ", " ", " ", " ", " ", " "]
        colonne_3 = [" ", " ", " ", " ", " ", " "]
        colonne_4 = [" ", " ", " ", " ", " ", " "]
        colonne_5 = [" ", " ", " ", " ", " ", " "]
        colonne_6 = [" ", " ", " ", " ", " ", " "]
        list_colonne = [colonne_0, colonne_1 , colonne_2 , colonne_3, colonne_4, colonne_5, colonne_6]
        list_etage = [etage_0,etage_1,etage_2,etage_3,etage_4,etage_5,etage_6]

        #On place nos widgets

        message = "C'est le tour du joueur {0}".format(self.joueur_num+1)
        self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
        self.texte.place(x=140,y=0)

        boutons_1 = Button(self,image=image_blanc, command=lambda  num=0,coord_x=30:  event(num,coord_x))
        boutons_1.place(x=30, y=400)

        boutons_2 = Button(self,image=image_blanc, command=lambda  num=1,coord_x=105:  event(num,coord_x))
        boutons_2.place(x=105, y=400)

        boutons_3 = Button(self,image=image_blanc, command=lambda  num=2,coord_x=180:  event(num,coord_x))
        boutons_3.place(x=180, y=400)

        boutons_4 = Button(self,image=image_blanc, command=lambda  num=3,coord_x=255:  event(num,coord_x))
        boutons_4.place(x=255, y=400)

        boutons_5 = Button(self,image=image_blanc, command=lambda  num=4,coord_x=330:  event(num,coord_x))
        boutons_5.place(x=330, y=400)

        boutons_6 = Button(self,image=image_blanc, command=lambda  num=5,coord_x=405:  event(num,coord_x))
        boutons_6.place(x=405, y=400)

        boutons_7 = Button(self,image=image_blanc, command=lambda  num=6,coord_x=480:  event(num,coord_x))
        boutons_7.place(x=480, y=400)

        list_boutons = [boutons_1,boutons_2,boutons_3,boutons_4,boutons_5,boutons_6,boutons_7]

        #Fonctions
        def event(num,coord_x) :
            aff_jetons(num,coord_x)

            print("etage",self.liste_colonnes[num])
            list_colonne[num][self.liste_colonnes[num]] = self.liste_image[self.joueur_num]
            print("list_colonne[num][self.liste_colonnes[num]]",list_colonne[num][self.liste_colonnes[num]])
            print("self.liste_image[self.joueur_num]",self.liste_image[self.joueur_num])
    
            #On monte d'un etage
            self.liste_colonnes[num] += 1

            #On verifie si on a atteint la limite
            if self.liste_colonnes[num] == 5 :
                list_boutons[num].destroy()


            victoire = verif_victoire(num)
            print(victoire)
            if victoire == 1 :
                victoire_aff()
            else :
                joueur()
                text()


        def aff_jetons(num,coord_x) :
            #On recupere l'etage au quel on affiche le jetons
            etage = self.liste_colonnes[num]

            #On calcule la valeur de y
            coord_y = 400-(60*etage + 10*(etage+1)+70)

            #Creation de l'image
            canvas = Canvas(self,width=60, height=60)
            canvas.create_image(0, 0, anchor=NW, image=self.liste_image[self.joueur_num])
            canvas.place(x=coord_x,y=coord_y)

        def verif_victoire(num) :
            #On verifie la victoire sur le bas
            etage = self.liste_colonnes[num]
            etage -= 1
            nb_symbole = 1
            while list_colonne[num][etage] == self.liste_image[self.joueur_num] :
                etage -= 1
                if etage < 0 :
                    break
                nb_symbole += 1

            if nb_symbole >= 4 :
                return(1)



        	#On verifie la victoire sur la gauche
            emplacement_save = num
            nb_symbole = 1
            emplacement_save-=1
            etage = list_etage[num]
            etage -= 2
            while list_colonne[emplacement_save][etage] == self.liste_image[self.joueur_num] :
                emplacement_save -=1
                nb_symbole += 1
                if etage < 0 :
                    break

            if nb_symbole >= 4 :
                return(1)


            #On verifie la victoire sur la droite
            emplacement_save = num
            emplacement_save += 1
            etage = self.liste_colonnes[num]
            etage -=1
            if emplacement_save  < 7:
                while list_colonne[emplacement_save][etage] == self.liste_image[self.joueur_num] :
                    emplacement_save +=1
                    nb_symbole += 1
                    if etage < 0 :
                        break
                    if emplacement_save > 6:
                        break
            if nb_symbole >= 4 :
                return(1)


        	#On verifie la victoire sur la diagonale haut droite
            nb_symbole = 1
            emplacement_save = num
            emplacement_save += 1
            etage = self.liste_colonnes[num]
            if emplacement_save  < 7:
                while list_colonne[emplacement_save][etage] == self.liste_image[self.joueur_num] :
                    emplacement_save +=1
                    etage +=1
                    nb_symbole += 1
                    if emplacement_save > 6:
                        break

            if nb_symbole >= 4 :
                return(1)


        	#On verifie la victoire sur la diagonale bas gauche
            emplacement_save = num
            emplacement_save -= 1
            etage = self.liste_colonnes[num]
            etage -=2
            while list_colonne[emplacement_save][etage] == self.liste_image[self.joueur_num] :
                emplacement_save -=1
                etage -=1
                nb_symbole += 1
                if etage < 0 :
                    break
            if nb_symbole >= 4 :
                return(1)


        	#On verifie la victoire sur la diagonale haut gauche
            nb_symbole = 1
            emplacement_save = num
            emplacement_save -= 1
            etage = self.liste_colonnes[num]
            while list_colonne[emplacement_save][etage] == self.liste_image[self.joueur_num] :
                emplacement_save -=1
                etage +=1
                nb_symbole += 1
                if etage > 5 :
                    break

            if nb_symbole >= 4 :
                return(1)




        	#On verifie la victoire sur la diagonale bas droite
            emplacement_save = num
            emplacement_save += 1
            etage = self.liste_colonnes[num]
            etage -= 2
            if emplacement_save  < 7:
                while list_colonne[emplacement_save][etage] == self.liste_image[self.joueur_num] :
                    emplacement_save +=1
                    etage -=1
                    nb_symbole += 1
                    if etage < 0 :
                        break
                    if emplacement_save > 6:
                        break

                if nb_symbole >= 4 :
                    return(1)

            return(0)

        def victoire_aff() :
            for i in list_boutons :
                i.destroy()
            message = "Le joueur {0} a gagné !".format(self.joueur_num+1)
            self.texte.place(x=1000,y=1000)
            self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
            self.texte.place(x=140,y=0)

        def joueur() :
            if self.joueur_num == 0 :
                self.joueur_num += 1
            else :
                self.joueur_num -= 1
            return(self.joueur_num)

        def text() :
            self.texte.place(x=1000,y=1000)
            message = "C'est le tour du joueur {0}".format(self.joueur_num+1)
            self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
            self.texte.place(x=140,y=0)


fenetre = Tk()
fenetre.title("Puissance 4")

image_blanc = PhotoImage(file="blanc.png")
image_rouge = PhotoImage(file="Rouge.png")
image_jaune = PhotoImage(file="Jaune.png")


Morpion = Interface(fenetre)

Morpion.mainloop()
