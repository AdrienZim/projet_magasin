# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:22:14 2023

@author: michelra
"""
# Import du module Tkinter
import tkinter as tk
from tkinter import ttk
import sys

# Imports des fichiers de Classe
from classes.class_stock import *

# Fonction de chargement du CSV
assert importer(csv_import) == True, "L'importation du stock contient une erreur de chargement."

# Fonctions :
def action(event):
	# Obtenir l'élément sélectionné
    select = menu_choix_interface.get()
    
    if select == "Client":
        print(None)
    
    if select == "Gestionnaire du stock":
        print(None)
    
    if select == "Fermeture" :
        app.destroy()
        sys.exit("Fermeture de l'interface")


# Création de la page Tkinter et définition de sa taille
app = tk.Tk()
app.geometry('900x600')

# Choix de l'interface et définition du menu sur "Client" par défault
labelChoix = tk.Label(app, text = "Veuillez choisir votre interface !")
interfaces_possibles = ["Client", "Gestionnaire du stock", "Fermeture"]
menu_choix_interface = ttk.Combobox(app, values = interfaces_possibles)
# menu_choix_interface.current(0)



# Affichages dans l'interface
labelChoix.pack()
menu_choix_interface.pack()
# Détection du choix
menu_choix_interface.bind("<<ComboboxSelected>>", action)

# Lancement de l'interface
app.mainloop()