# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:16:59 2024

@author: douchinap
"""

# SOUS LA FORME {num_panier:[num_client,[[num_article,prix,quantite],[num_article,prix,quantite]],total]}
# panier = {69:[2,[[5,2,3],[2,4,6]]]}


def prix_total(panier,num_panier):
    total = 0
    for e in panier[num_panier][1] :
        total += e[1]*e[2]
    return total




class Panier():
    def __init__(self,num_panier,num_client,contenu):
        self.num_panier = num_panier
        self.num_client = num_client
        self.contenu = contenu

    def dico(self):
        P = {self.num_panier:[self.num_client,self.contenu]}
        P[self.num_panier].append(prix_total(P, self.num_panier))
        return P
    
    def ajout(self,nouvel_article):
        P = panier.dico()
        P[self.num_panier][1].append(nouvel_article)
        t = prix_total(panier.dico(), self.num_panier)
        P[self.num_panier].append(t)
        return P
        
    def suppr(self,n):
        P = panier.dico()
        del P[self.num_panier][1][n-1]
        t = prix_total(panier.dico(), self.num_panier)
        P[self.num_panier].append(t)
        assert n < len(P[self.num_panier][1])
        return P


###################################################################
######################### Tests unitaires #########################
###################################################################

panier = Panier(69,2,[[5,2,3],[2,4,6]])
# print(panier.ajout([6,99,2]))
# print(panier.suppr(1))