from tkinter import *
import os
from collections import OrderedDict
import pickle
from random import randint
os.chdir("image")






def interface_menu() :

    class Interface(Frame):
    

        """Notre fenetre principale.
        Tous les widgets sont stockes comme attributs de cette fenetre."""

        def __init__(self, fenetre, **kwargs):
            Frame.__init__(self, fenetre, width=580, height=400,background='white',**kwargs)
            self.pack()

            #On init nos liste et variable global dans la class
            liste_nom = []
            liste_valeur = []


            #On place nos widgets
            canvas = Canvas(self,width=580, height=500, borderwidth=0)
            canvas.create_image(0, 0, anchor=NW, image=image_fond)
            canvas.place(x=0,y=0)

            boutons_jouer = Button(self,image=image_jouer,command=lambda a=0 :self.bouton_jouer())
            boutons_jouer.place(x=10, y=130)

            boutons_top = Button(self,image=image_top,command=lambda a=0 :self.quitter())
            boutons_top.place(x=10, y=260)

            with open('score.txt', 'rb') as fichier :
                depickler = pickle.Unpickler(fichier)
                dictionnaire = depickler.load()

            dicti = OrderedDict(sorted(dictionnaire.items(), key=lambda t: t[1]))

            for nom,valeur in dicti.items() :
                liste_nom.append(nom)
                liste_valeur.append(valeur)


            
            self.message = "{0} : {1}".format(liste_nom[0],liste_valeur[0])
            self.texte = Label(fenetre, text=self.message, font=(None, 15), height=1,background="white")
            self.texte.place(x=415,y=180)



            
            self.message = "{0} : {1}".format(liste_nom[1],liste_valeur[1])
            self.texte = Label(fenetre, text=self.message, font=(None, 15), height=1,background="white")
            self.texte.place(x=415,y=220)                   


            self.message = "{0} : {1}".format(liste_nom[2],liste_valeur[2])
            self.texte = Label(fenetre, text=self.message, font=(None, 15), height=1,background="white")
            self.texte.place(x=415,y=260)       



            self.message = "{0} : {1}".format(liste_nom[3],liste_valeur[3])
            self.texte = Label(fenetre, text=self.message, font=(None, 15), height=1,background="white")
            self.texte.place(x=415,y=300)       



            self.message = "{0} : {1}".format(liste_nom[4],liste_valeur[4])
            self.texte = Label(fenetre, text=self.message, font=(None, 15), height=1,background="white")
            self.texte.place(x=415,y=340)       


        def quitter(self) : 
            fenetre.destroy()

        def bouton_jouer (self) :
            fenetre.destroy()
            interface_enregistrement()


    fenetre = Tk()
    fenetre.title("Memory Menu")

    #On recupere les images
    

    image_fond = PhotoImage(file="Menu.png",master=fenetre)
    image_jouer = PhotoImage(file="Jouer.png",master=fenetre)
    image_top = PhotoImage(file="Quitter2.png",master=fenetre)



    Memory = Interface(fenetre)

    Memory.mainloop()


def jouer(nom):

    class Interface(Frame):

        """Notre fenetre principale.
        Tous les widgets sont stockes comme attributs de cette fenetre."""

        def __init__(self, fenetre, **kwargs):
            Frame.__init__(self, fenetre, width=500, height=500, background='white', **kwargs)
            self.pack()

            #On init nos liste et variable global dans la class
            self.trouver = 0
            self.nb_choix = 0
            self.choix_1 = 0
            self.choix_2 = 0
            self.image_1 = 0
            self.image_2 = 0
            self.essaie = 0
            self.ok = 0
            self.message = "Nombre d'essai = {0}".format(self.essaie)
            coord_x = -22
            coord_y = -22
            num = 1
            liste_bouton = []
            liste_image = [image_Bowser,image_DK,image_Mario,image_Peache,image_Maskass,image_Skellerex,image_Toad,image_Yoshi,image_Bowser_O,image_DK_O,image_Mario_O,image_Peache_O,image_Maskass_O,image_Skellerex_O,image_Toad_O,image_Yoshi_O]
            liste_image_2 = [image_Bowser,image_DK,image_Mario,image_Peache,image_Maskass,image_Skellerex,image_Toad,image_Yoshi,image_Bowser_O,image_DK_O,image_Mario_O,image_Peache_O,image_Maskass_O,image_Skellerex_O,image_Toad_O,image_Yoshi_O]
            
            def suppr():
                try :
                    self.image_2.destroy()
                    self.image_1.destroy()
                except :
                    self.image_1.destroy()
                for i in liste_bouton :
                    i.config(state=NORMAL)



            def bouton_img () :
                num_ra = randint(0,len(liste_image)-1)
                image = liste_image[num_ra]
                del liste_image[num_ra]
                return image

            def action_bouton(image_aff,coord_x,coord_y,num_bou) :


                self.nb_choix += 1
                canvas = Canvas(self,width=100, height=100)
                canvas.create_image(0, 0, anchor=NW, image=image_aff)
                canvas.place(x=coord_x,y=coord_y)


                if self.nb_choix == 1 :
                    self.image_1 = canvas
                    for i in liste_image_2 :
                        if i == image_aff :

                            if liste_image_2.index(i) < 8 :

                                self.choix_1 = image_aff
                            else :

                                self.choix_1 = liste_image_2[liste_image_2.index(i)-8]


                elif self.nb_choix == 2 :
                    self.nb_choix = 0
                    self.image_2 = canvas
                    for i in liste_image_2 :
                        if i == image_aff :
                            if liste_image_2.index(i) < 8 :
                                self.choix_2 = image_aff

                            else :
                                self.choix_2 = liste_image_2[liste_image_2.index(i)-8]


                    if self.choix_2 == self.choix_1 :
                        self.essaie += 1
                        self.message = "Nombre d'essai = {0}".format(self.essaie)
                        self.texte = Label(fenetre, text=self.message, font=(None, 10), height=1,background="white")
                        self.texte.place(x=30,y=470)
                        self.trouver += 1
                        if self.trouver == 8 :
                            enregistrer_score(nom.upper(),self.essaie)
                            fenetre.after(1000)
                            fenetre.destroy()
                            victoire(nom,self.essaie)
                            


                    else :
                        self.essaie += 1
                        self.message = "Nombre d'essai = {0}".format(self.essaie)
                        self.texte = Label(fenetre, text=self.message, font=(None, 10), height=1,background="white")
                        self.texte.place(x=30,y=470)

                        for i in liste_bouton :
                            i.config(state=DISABLED)
                        fenetre.after(1000,suppr)






            def bouton(coord_y,coord_x,num,num_bou) :
                #num_ra = randint(0,len(liste_image)-1)
                #image = liste_image[num_ra]

                if num == 1 :
                    coord_x += 50
                    coord_y += 50
                if num == 2 :
                    coord_x += 160
                    coord_y += 50
                if num == 3 :
                    coord_x += 270
                    coord_y += 50
                if num == 4 :
                    coord_x += 380
                    coord_y += 50
                if num == 5 :
                    coord_x += 50
                    coord_y += 160
                if num == 6 :
                    coord_x += 160
                    coord_y += 160
                if num == 7 :
                    coord_x += 270
                    coord_y += 160
                if num == 8 :
                    coord_x += 380
                    coord_y += 160
                if num == 9 :
                    coord_x += 50
                    coord_y += 270
                if num == 10 :
                    coord_x += 160
                    coord_y += 270
                if num == 11 :
                    coord_x += 270
                    coord_y += 270
                if num == 12 :
                    coord_x += 380
                    coord_y += 270
                if num == 13 :
                    coord_x += 50
                    coord_y += 380
                if num == 14 :
                    coord_x += 160
                    coord_y += 380
                if num == 15 :
                    coord_x += 270
                    coord_y += 380
                if num == 16 :
                    coord_x += 380
                    coord_y += 380


                image_aff = bouton_img()
                image = Button(self,command=lambda x=1: action_bouton(image_aff,coord_x,coord_y,num_bou),image=image_blanc)
                image.place(x=coord_x, y=coord_y)
                num+=1
                return(image,num)


            #On place nos widgets
            self.texte = Label(fenetre, text=self.message, font=(None, 10), height=0,background="white")
            self.texte.place(x=30,y=470)
            
            bouton_1,num = bouton(coord_y,coord_x,num,1)
            bouton_2,num = bouton(coord_y,coord_x,num,2)
            bouton_3,num = bouton(coord_y,coord_x,num,3)
            bouton_4,num = bouton(coord_y,coord_x,num,4)
            bouton_5,num = bouton(coord_y,coord_x,num,5)
            bouton_6,num = bouton(coord_y,coord_x,num,6)
            bouton_7,num = bouton(coord_y,coord_x,num,7)
            bouton_8,num = bouton(coord_y,coord_x,num,8)
            bouton_9,num = bouton(coord_y,coord_x,num,9)
            bouton_10,num = bouton(coord_y,coord_x,num,10)
            bouton_11,num = bouton(coord_y,coord_x,num,11)
            bouton_12,num = bouton(coord_y,coord_x,num,12)
            bouton_13,num = bouton(coord_y,coord_x,num,13)
            bouton_14,num = bouton(coord_y,coord_x,num,14)
            bouton_15,num = bouton(coord_y,coord_x,num,15)
            bouton_16,num = bouton(coord_y,coord_x,num,16)

            liste_bouton = [bouton_1,bouton_2,bouton_3,bouton_4,bouton_5,bouton_6,bouton_7,bouton_8,bouton_9,bouton_10,bouton_11,bouton_12,bouton_13,bouton_14,bouton_15,bouton_16]


    fenetre = Tk()
    fenetre.title("Memory")


    image_blanc = PhotoImage(file="Blanc.png",master=fenetre)


    image_Bowser = PhotoImage(file="Bowser.png",master=fenetre)
    image_DK = PhotoImage(file="DK.png",master=fenetre)
    image_Mario = PhotoImage(file="Mario.png",master=fenetre)
    image_Peache = PhotoImage(file="Peach.png",master=fenetre)
    image_Maskass = PhotoImage(file="Maskass.png",master=fenetre)
    image_Skellerex = PhotoImage(file="Skellerex.png",master=fenetre)
    image_Toad = PhotoImage(file="Toad.png",master=fenetre)
    image_Yoshi = PhotoImage(file="Yoshi.png",master=fenetre)

    image_Bowser_O = PhotoImage(file="Bowser_O.png",master=fenetre)
    image_DK_O = PhotoImage(file="DK_O.png",master=fenetre)
    image_Mario_O = PhotoImage(file="Mario_O.png",master=fenetre)
    image_Peache_O = PhotoImage(file="Peach_O.png",master=fenetre)
    image_Maskass_O = PhotoImage(file="Maskass_O.png",master=fenetre)
    image_Skellerex_O = PhotoImage(file="Skellerex_O.png",master=fenetre)
    image_Toad_O = PhotoImage(file="Toad_O.png",master=fenetre)
    image_Yoshi_O = PhotoImage(file="Yoshi_O.png",master=fenetre)


    Jeux = Interface(fenetre)

    def bouton_img () :
        num = randint(0,len(liste_image))
        image = liste_image[num]
        del liste_image[num]
        return image


    Jeux.mainloop()




def interface_enregistrement() :

    class Interface(Frame):

        """Notre fenetre principale.
        Tous les widgets sont stockes comme attributs de cette fenetre."""

        def __init__(self, fenetre, **kwargs):
            Frame.__init__(self, fenetre, width=305, height=150, background='white', **kwargs)
            self.pack()

            def entrer_nom(nom) :
                if len(nom.get()) <= 8 :
                    fenetre.destroy()
                    jouer(nom.get())

            #On init nos liste et variable global dans la class
            
            #On place nos widgets
            message = "Veuillez choisir un nom"
            self.texte = Label(fenetre, text=message, font=(None, 20), height=1, background='white')
            self.texte.place(x=10,y=0)

            message = "8 caractere max"
            self.texte = Label(fenetre, text=message, font=(None, 10), height=1, background='white')
            self.texte.place(x=10,y=70)

            nom = StringVar()
            entree = Entry(fenetre, width=15, textvariable=nom)
            entree.pack()
            entree.place(x=10,y=100)

            fenetre.bind('<Return>',lambda a=1:entrer_nom(nom))




    fenetre = Tk()
    fenetre.title("Memory")




    Memory = Interface(fenetre)

    Memory.mainloop()



def enregistrer_score(nom,score) :
    a=0
    with open('score.txt', 'rb') as fichier :
        depickler = pickle.Unpickler(fichier)
        dictionnaire = depickler.load()

    for i,values in dictionnaire.items() :
        dictionnaire[i] = int(values)
        if i == nom.upper() :
            if values > score :
                dictionnaire[nom.upper()] = int(score)
        else : 
            a = 1

    if a == 1 :
        dictionnaire[nom.upper()] = score
    
    with open("score.txt", "wb") as fichier :
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(dictionnaire)

def victoire(nom,score) :

    class Interface(Frame):


        """Notre fenetre principale.
        Tous les widgets sont stockes comme attributs de cette fenetre."""

        def __init__(self, fenetre, **kwargs):
            Frame.__init__(self, fenetre, width=580, height=240,background='white',**kwargs)
            self.pack()

            #On init nos liste et variable global dans la class


            #On place nos widgets
            canvas = Canvas(self,width=580, height=500, borderwidth=0)
            canvas.create_image(0, 0, anchor=NW, image=image_fond)
            canvas.place(x=0,y=0)

            boutons_jouer = Button(self,image=image_jouer,command=lambda a=0 :self.bouton_jouer())
            boutons_jouer.place(x=90, y=170)

            boutons_top = Button(self,image=image_quitter,command=lambda a=0 :self.quitter())
            boutons_top.place(x=350, y=170)


            self.message = "Bravo {0} ton score est de {1} essai".format(nom,score)
            self.texte = Label(fenetre, text=self.message, font=(None, 25), height=1,background="white")
            self.texte.place(x=20,y=100)

         

        def bouton_jouer (self) :
            fenetre.destroy()
            interface_menu()

        def quitter (self) :
            fenetre.destroy()

    fenetre = Tk()
    fenetre.title("Victoire")

    #On recupere les images
    

    image_fond = PhotoImage(file="Victoire.png",master=fenetre)
    image_jouer = PhotoImage(file="Rejouer.png",master=fenetre)
    image_quitter = PhotoImage(file="Quitter.png",master=fenetre)



    Memory = Interface(fenetre)

    Memory.mainloop()    



interface_menu()