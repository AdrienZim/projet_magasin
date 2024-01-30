# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:16:59 2024

@author: douchinap

"""
import csv

# SOUS LA FORME {num_panier:[num_client,[[num_article,prix,quantitÈ],[num_article,prix,quantitÈ]],total]}
# panier = {69:[2,[[5,2,3],[2,4,6]]]}

stockage_panier = []

def prix_total(panier,num_panier):
    total = 0
    for e in panier[num_panier][1] :
        total += e[1]*e[2]
    return total


"""
Actualisation des parametres de numéro de commande
--------------------------------------------------------------------
"""

def actualisation():    
    inter_parametre = {}
    with open('./classes/Parametre.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            for e in row :
                inter_parametre[e]=int(row[e])
                
    inter_parametre['Dernier_num_panier'] += 1
    numero = inter_parametre['Dernier_num_panier']
    
    with open('./classes/Parametre.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        K =list(inter_parametre.keys())
        writer.writerow(K)
        V =list(inter_parametre.values())
        writer.writerow(V)
    return numero

"""
--------------------------------------------------------------------
"""

class Panier():
    def __init__(self,num_client,contenu):
        self.num_panier = actualisation()
        self.num_client = num_client
        self.contenu = contenu

    def dico(self):
        P = {self.num_panier:[self.num_client,self.contenu]}
        P[self.num_panier].append(prix_total(P, self.num_panier))
        return P
    
    def ajout(self,nouvel_article):
        P = self.dico()
        P[self.num_panier][1].append(nouvel_article)
        t = prix_total(self.dico(), self.num_panier)
        P[self.num_panier][-1] = t
        return P
        
    def suppr(self,n):
        P = self.dico()
        del P[self.num_panier][1][n-1]
        t = prix_total(self.dico(), self.num_panier)
        P[self.num_panier][-1] = t
        assert n < len(P[self.num_panier][1])
        return P


###################################################################
######################### Tests unitaires #########################
###################################################################

# panier = Panier(2,[[5,2,3],[2,4,6]])
# print(panier.ajout([6,99,2]))
# print(panier.suppr(1))