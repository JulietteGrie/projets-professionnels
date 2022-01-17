# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:20:37 2022

@author: Juliette
"""
import random
import csv


## nombre de patients

parametre = int(input('Combien y a-t-il de patients?:'))

    

## écriture du fichier CSV
with open('patients.csv', 'w', newline = '') as csvfile:
    
    filewriter = csv.writer(csvfile)
    
    filewriter.writerow([## variables quantitatives
           'identite', 'age', 'nbmedic',  
           ## variables qualitatives
           'agecl', 'sexe', 'situation_familiale', 
           'mode_de_vie', 'aide_a_domicile', 'chute', 
           'CV', 'psy', 'antidiabetiques', 
           'autresmed', 'marche_autonome'])    

    for indice in range(parametre + 1):
        if indice == 0:
            filewriter.writerow([## variables quantitatives
           'identite', 'age', 'nbmedic',  
           ## variables qualitatives
           'agecl', 'sexe', 'situation_familiale', 
           'mode_de_vie', 'aide_a_domicile', 'chute', 
           'CV', 'psy', 'antidiabetiques', 
           'autresmed', 'marche_autonome'])  
        else:
            filewriter.writerow(
                # identité du patient
                [indice] + 
                ## les patients ont de 0 à 100 ans
                [random.randint(0, 100)] +
                ## les patient prennent de 0 à 10 médicaments différents
                [random.randint(0, 10)] +
                ## valeurs qualitatives
                [random.randint(0, 1) for i in range(len('patients.csv') - 1)])
            


