from tkinter import *


class Joueur :
    def __init__(self,signe):
        self.signe = signe

class Interface(Frame):

    """Notre fenetre principale.
    Tous les widgets sont stockes comme attributs de cette fenetre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=300, height=310, **kwargs)
        self.pack()
        self.num= 0
        coord = " "
        self.liste_coord = [coord,coord,coord,coord,coord,coord,coord,coord,coord]

        self.victoire = 0

        liste_image = [image_croix,image_rond]

        # Creation de nos widgets
        message = "Tour du joueur {0}".format(self.num+1)
        self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
        self.texte.place(x=55,y=0)

        boutons_1 = Button(self,image=image_blanc, command=lambda  num=0,coord_x=30,coord_y=50:  event(num,coord_x,coord_y,self.num))
        boutons_1.place(x=30, y=50)

        boutons_2 = Button(self,image=image_blanc, command=lambda  num=1,coord_x=115,coord_y=50:  event(num,coord_x,coord_y,self.num))
        boutons_2.place(x=115, y=50)

        boutons_3 = Button(self,image=image_blanc, command=lambda  num=2,coord_x=200,coord_y=50:  event(num,coord_x,coord_y,self.num))
        boutons_3.place(x=200, y=50)

        boutons_4 = Button(self,image=image_blanc, command=lambda  num=3,coord_x=30,coord_y=130:  event(num,coord_x,coord_y,self.num))
        boutons_4.place(x=30, y=130)

        boutons_5 = Button(self,image=image_blanc, command=lambda  num=4,coord_x=115,coord_y=130:  event(num,coord_x,coord_y,self.num))
        boutons_5.place(x=115, y=130)

        boutons_6 = Button(self,image=image_blanc, command=lambda  num=5,coord_x=200,coord_y=130:  event(num,coord_x,coord_y,self.num))
        boutons_6.place(x=200, y=130)

        boutons_7 = Button(self,image=image_blanc, command=lambda  num=6,coord_x=30,coord_y=210:  event(num,coord_x,coord_y,self.num))
        boutons_7.place(x=30, y=210)

        boutons_8 = Button(self,image=image_blanc, command=lambda  num=7,coord_x=115,coord_y=210:  event(num,coord_x,coord_y,self.num))
        boutons_8.place(x=115, y=210)

        boutons_9 = Button(self,image=image_blanc, command=lambda  num=8,coord_x=200,coord_y=210:  event(num,coord_x,coord_y,self.num))
        boutons_9.place(x=200, y=210)

        list_boutons = [boutons_1,boutons_2,boutons_3,boutons_4,boutons_5,boutons_6,boutons_7,boutons_8,boutons_9]
        def event(num,coord_x,coord_y,joueur_num) :
            aff_image(num,coord_x,coord_y,joueur_num)
            avant_verif(num)
            verif()

            if self.victoire == 0 :
                self.num = joueur(joueur_num)
                message()



        def aff_image(num,coord_x,coord_y,joueur_num) :
            list_boutons[num].destroy()
            canvas = Canvas(self,width=60, height=60)
            canvas.create_image(0, 0, anchor=NW, image=liste_image[joueur_num])
            canvas.place(x=coord_x,y=coord_y)

        def joueur(joueur_num) :
            if joueur_num == 0 :
                joueur_num += 1
            else :
                joueur_num -= 1
            return(joueur_num)

        def message() :
            message = "Tour du joueur {0}".format(self.num+1)
            self.texte.place(x=1000,y=1000)
            self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
            self.texte.place(x=55,y=0)

        def avant_verif(num):
            if self.num == 0:
                self.liste_coord[num] = "X"
            else :
                self.liste_coord[num] = "O"

        def verif() :
            compteur = 0
            for i in self.liste_coord:
                if i != " " :
                    compteur+=1

            if compteur == 9 :
                egaliter()


            if self.liste_coord[0] != " " :
                if self.liste_coord[1] == self.liste_coord[0] and self.liste_coord[2] == self.liste_coord[0]:
                    victoire()
                elif self.liste_coord[3] == self.liste_coord[6] and self.liste_coord[0] == self.liste_coord[6] :
                    victoire()
                elif self.liste_coord[4] == self.liste_coord[8] and self.liste_coord[0] == self.liste_coord[8] :
                    victoire()
            if self.liste_coord[4] != " " :
                if self.liste_coord[1] == self.liste_coord[7] and self.liste_coord[4] == self.liste_coord[7] :
                    victoire()
                elif self.liste_coord[3] == self.liste_coord[5] and self.liste_coord[4] == self.liste_coord[5] :
                    victoire()
                elif self.liste_coord[6] == self.liste_coord[2] and self.liste_coord[4] == self.liste_coord[2] :
                    victoire()
            if self.liste_coord[8] != " " :
                if self.liste_coord[5] == self.liste_coord[2] and self.liste_coord[8] == self.liste_coord[2] :
                    victoire()
                elif self.liste_coord[6] == self.liste_coord[7] and self.liste_coord[8] == self.liste_coord[7] :
                    victoire()



        def victoire():
            message = "Le joueur {0} a gagner !".format(self.num+1)
            self.texte.place(x=1000,y=1000)
            self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
            self.texte.place(x=25,y=0)
            self.victoire = 1

            for i in list_boutons :
                i.destroy()

        def egaliter():
            message = "Egalité"
            self.texte.place(x=1000,y=1000)
            self.texte = Label(fenetre, text=message, font=(None, 20), height=1)
            self.texte.place(x=105,y=0)
            self.victoire = 1



joueur_1 = Joueur("croix")
joueur_2 = Joueur("Rond")

fenetre = Tk()
fenetre.title("Morpion")

image_blanc = PhotoImage(file="blanc.png")
image_croix = PhotoImage(file="Croix.png")
image_rond = PhotoImage(file="Rond.png")
Morpion = Interface(fenetre)

Morpion.mainloop()
