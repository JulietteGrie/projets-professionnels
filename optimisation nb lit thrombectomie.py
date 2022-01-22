# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:31:58 2021

@author: Juliette
"""
#packages
import numpy as np
import random as rm
import statistics
from pyexcel_ods import get_data
from scipy.spatial import distance_matrix

data = get_data('coordonnées génération matrice distance.ods')
coordonnees = data["Feuille1"]

#données 
hospital = ["CHU Angers", "Cholet", "Saumur", "Longué-Jumelles", "CESAME Angers", "Beaugeois-Vallée", "La corniche angevine", "Doué-en-Anjou", "Layon-Aubance", "Lys-Hyrôme",
            "CHU Laval", "Haut Anjou", "Ernee", "Evron", "Nord Mayenne", "Villaines la Juhel", "sud-ouest mayennais",
            "Le Mans", "EPSM Sarthe", "Beaumont", "Bonne table", "Chateau du Loir", "La Ferté Bernard", "Sarthe et Loir", "St-Calais", "Sille le Guillaume", "François de Daillon",
            "CHD La-Roche-sur-Yon", "Loire Vendée océan", "collines vendéennes", "Noirmoutier", "Georges Mazurelle", "Côte de lumière", "Dumonte Île d'Yeu", "Fontenay le Comte",
            "CHU Nantes", "Blain", "Pierre Delaroche", "Corcoue sur Lorgne", "presqu'île", "pays du Retz", "Maubreuil", "Loire et Sillon", "Sevre et Loire", "Bouguenais", "Erdre et Loire", "Chateaubriand",
            "CHU Rennes", "Montfort-sur-Meu", "St Meen le grand", "Fougeres", "Redon Carentoir", "Vitre", "La Guerche de Bretagne", "marches de Bretagne", "Grand Fougeray", "Janze", 
            "CHU Tours", "CHU Amboise-Chateau-Renault", "Loches", "Jean Pages de Luynes", "Sevestre-La Membrolle", "Chinonais", "Andre-Georges Voisin", "pays de Richelieu", "la Croix Papillon", "Ste Maure de Touraine"] #hôpitaux

 #matrice des distances
distance = distance_matrix(coordonnees, coordonnees)


#paramètres exponentiels 
l = 1.25 #fréquence moyenne des thrombus
throm = 2 #durée moyenne thrombectomie


def optimisation(x):
    
    
    '''
    initialisation
    '''
    T = [0] #instant où le thrombus apparaît, initialisation à 0

    #nombre de lits par hôpital
    nb_lit_max = {0:x, 10:1, 27:1, 35:5, 47:5, 57:2, 58:1} #capacité de chaque hôpital pour une thrombectomie
    nb_lit = {0:x, 10:1, 27:1, 35:5, 47:5, 57:2, 58:1} #initialisation du nombre de lits libres
    # 0 = Angers
    # 10 = Laval
    # 27 = La-Roche-Sur-Yon
    # 35 = Nantes
    # 47 = Rennes
    # 57 = Tours
    # 58 = Amboise
    
    #données temporelles PEC pour chaque hôpital
    t_hop = {i:[[0, 0],[]] for i in nb_lit.keys()}  
    # [[instant T où la thrombectomie est prise en charge] => récurrence double
    # [durée de la thrombectomie]]

    #fonction récompense    
    f = 0
    
    
    '''
    corps algorithme
    '''
    for i in range(7000): #représente environ 1 an
        
        
        # apparition d'un thrombus
        T.append(T[-1] + np.random.exponential(l, 1)[0]) #un thrombus apparaît à l'instant T...
        h = rm.randint(0, len(hospital) - 1) # dans l'hôpital h
        
        
        # détermination de l'hôpital de prise en charge
        libre = [0] + list(keys for keys, values in nb_lit_max.items() if values > 0) #renvoie les hôpitaux où il y a des lits de libre
        d = {k:distance[h][k] for k in libre} #renvoie la distance entre l'hôpital de départ et un hôpital où il y a de la place
        a = min(d.values()) #renvoie le minimum de ces distances
        hosp = [m for m in d.keys() if d[m] == a] #renvoie les hôpitaux où la thrombectomie pourrait avoir lieu
        
        
        #mise à jour de la fonction récompense
        if 0 in hosp: #si Angers est le seul hôpital disponible
            if nb_lit[0] == 0: #si l'hôpital d'Angers doit refuser une intervention => pénalité
                f = f - 1
                nb_lit[0] = 0
            else: # la thrombectomie a lieu à Angers
                t_hop[0][0].append(T[-1]) #la thrombectomie est prise en charge à l'instant T
                t_hop[0][1].append(np.random.exponential(throm, 1)[0]) #elle dure un certain temps
                nb_lit[0] = nb_lit[0] - 1 #on perd un lit

            
        #hôpital de PEC
        else:
            H = hosp[-1]
            t_hop[H][0].append(T[-1]) #la thrombectomie est prise en charge à l'instant T
            t_hop[H][1].append(np.random.exponential(throm, 1)[0]) #elle dure un certain temps
            nb_lit[H] = nb_lit[H] - 1 #on perd un lit
            
            
        #mise à jour du nombre de lits disponibles
        for j in nb_lit_max.keys():
            if nb_lit[j] - nb_lit_max[j] < 0 and t_hop[j][1] != []:
                duree_int = t_hop[j][1][0]
                while t_hop[j][1] != [] and duree_int < t_hop[j][0][-1] - t_hop[j][0][-2]: #tant qu'on a le temps de traiter les malades, on rajoute des lits
                    duree_int = duree_int + t_hop[j][1][0]
                    nb_lit[j] = min(nb_lit[j] + 1, nb_lit_max[j])
                    t_hop[j][1].remove(t_hop[j][1][0])
        
        
    '''
    résultats
    '''    
    return(f)


def essai():
    liste = [optimisation(x) for x in range(1, 5)]
    test = max(liste)
    lit = liste.index(test)
    return(lit + 1)

print(statistics.mean([essai() for i in range(10)]), statistics.variance([essai() for i in range(10)]))
print(statistics.mean([essai() for i in range(100)]), statistics.variance([essai() for i in range(100)]))





