# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:29:37 2023

@author: douchinap
"""

"""
--------------------------------------------------------------------
début de l'éctualisation de l'historique
import de la bibliotheque csv
mise en place des variables nécessaires et d'une nouvelle commande fictive c
"""
import csv

c = {'17_3': [[[1, 3.5, 2], [2, 2, 2],[1,1,1],[3,2,1],[8,8,8],[9,9,9]], 11]}
inter_c = []
inter_historique = {}
inter_dico = {}
V = []
n = 0

"""
Premiere ouverture du csv, récupération de l'historique de commande et stockage de celui-ci dans un dictionnaire inter_historique
décompte par n du nombre de commande de l'historique à sa récupération
"""
with open('historique.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        for e in row:
            if e not in inter_historique : 
                inter_historique[e] = []
            inter_historique[e].append(row[e])
        n+=1

"""
Ouverture du csv pour l'écriture
mise en place des colonnes 'identifiant_de_commande' et 'prix_total', ainsi que décision du nombre de colonnes articles (sous la forme a1, a2, etc) à ajouter en fonction de la plus longues commande de l'historique et de la commande à ajouter
"""        
with open('historique.csv', 'w', newline='') as csvfile:
    fieldnames = ['identifiant_de_commande', 'prix_total']    
    if len(inter_historique)-2 > len(c[list(c.keys())[0]][0]):
        for i in range(len(inter_historique)-2):
            fieldnames.append('a' + str(i+1))
    else:
        for i in range(len(c[list(c.keys())[0]][0])):
            fieldnames.append('a' + str(i+1))
        x = -1
        while len(inter_historique)-2 < len(c[list(c.keys())[0]][0]):
            inter_historique[fieldnames[x]] = []
            for com in range(len(inter_historique[fieldnames[0]])+1):
                inter_historique[fieldnames[x]].append('')
            x-=1
            
    """
ajout des valeurs de la nouvelle commande dans un dictionnaire intermédiaire facilitant son ajout au dictionnaire de commande intermédiaire
    """            
    inter_c.append(list(c.keys())[0]) 
    inter_c.append(list(c.values())[0][-1])
    for a in c[inter_c[0]][0]:
        inter_c.append(a)
    print(inter_c)

    """
ajout des éléments du dicitonnaire intermédiaire de la commande au dictionnaire représentant l'historique
(possibilité de fusion du traitement et du précédent)
    """
    i = 0
    for e in fieldnames :
        if i > len(inter_c)-1:    
            break
        else :
            inter_historique[e].append(inter_c[i])
            i+=1
        
    """
écriture ligne par ligne de chacunes des commandes originallement présentes et de la nouvelle qui s'ajoute à l'historique dans le csv
    """
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for i in range(n+1) :
        for e in fieldnames :
            if e not in inter_historique :    
                break
            elif inter_historique[e][-1] != '':
                inter_dico[e] = inter_historique[e][i]
        V = inter_dico    
        writer.writerow(V)

"""
fin de l'actualisation de l'historique
--------------------------------------------------------------------
"""

"""
outils de test, sauvegarde d'un csv d'historique
identifiant_de_commande;prix_total;a1;a2;a3;a4
9_3;15;[1,3.5,2];[2,2,4]
10_3;13;[1,3.5,2];[2,2,3]
"""