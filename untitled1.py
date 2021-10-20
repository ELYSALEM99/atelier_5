# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:07:58 2021

@author: Mohamed
"""

#Importer toutes les fonctions du module pyhton random
from random import *
import time

def gen_list_random_int(int_nbr:int=10,int_binf:int=0,int_bsup:int=10)->list:
    """

    Parameters
    ----------
    int_nbr : int, optional
        la taille de la liste . The default is 10.
    int_binf : int, optional
        le minimum de la liste . The default is 0.
    int_bsup : int, optional
        le maximum de la liste. The default is 10.

    Returns
    -------
    list
        retounre une liste de nombres aléatoires .

    """
    result=[]
    for i in range(int_nbr):
        #renvoie un entier aleatoire N telque int_binf<=N<=int_bsup
        result.append(randint(int_binf,int_bsup))
    return result

def mix_list(list_to_mix:list)->list:
    """
    la fonction (mix_list) qui prend en paramètre une liste (list_to_mix) de n'importe
    quoi potentiellement triée et qui retourne la liste mélangée.

    Parameters
    ----------
    list_to_mix : list
        liste triée.

    Returns
    -------
    list
        liste melangée.

    """
    lst_sorted=[]  #liste melangée
    indi_ele_list=[] #pour ajouter les indices de ma liste 
    while (len(list_to_mix)!=len(lst_sorted)):
        ind=randint(0,len(list_to_mix)-1)
        if ind not in indi_ele_list:
#cette condition va me permetre d'eviter l'ajout d'un element qui est deja dans ma liste
            lst_sorted.append(list_to_mix[ind])
            indi_ele_list.append(ind)   
    return lst_sorted

def choose_element_list(list_in_which_to_choose:list)->int:
    return list_in_which_to_choose[randint(0,len(list_in_which_to_choose)-1)]
    
def extract_elements_list(list_in_which_to_choose:list,int_nbr_of_element_to_extract:int)->list:
    """
    

    Parameters
    ----------
    list_in_which_to_choose : list
        DESCRIPTION.
    int_nbr_of_element_to_extract : int
        DESCRIPTION.

    Returns
    -------
    list
        une liste composée de nombre d'élément à extraire .

    """
 
    lst_nbr_of_element_to_extract=[] 
    indi_ele_list=[] #pour ajouter les indices de ma liste 
    while (len(lst_nbr_of_element_to_extract)!=int_nbr_of_element_to_extract):
        ind=randint(0,len(list_in_which_to_choose)-1)
        if ind not in indi_ele_list:
#cette condition va me permetre d'eviter l'ajout d'un element qui est deja dans ma liste
            lst_nbr_of_element_to_extract.append(list_in_which_to_choose[ind])
            indi_ele_list.append(ind)
    return lst_nbr_of_element_to_extract
        
            
def tri_list(liste:list)->list:
    temp_list=0
    for j in range(len(liste)-1):
        for i in range(len(liste)-1):
            if liste[i]>liste[i+1]:
                temp_list=liste[i]
                liste[i]=liste[i+1]
                liste[i+1]=temp_list
    return liste
    
    



list_test_triee=[1,2,3,5,7,8,9,18,20,30,35,40]
print(list_test_triee)
print(mix_list(list_test_triee))
print(choose_element_list(list_test_triee))
print(extract_elements_list(list_test_triee,6))
#Pour mesurer le temps d'exécution nous avons à notre disposition 
#la fonction perf_counter()
#Récupération du temps système et démarrage du chronomètre
start_pc_1 = time.perf_counter()
n=500
for i in range(n):
    mix_list(list_test_triee)
end_pc = time.perf_counter()
elapsed_time_pc_1 = end_pc-start_pc_1
print("le temps d’exécution moyen de la fonction mix_list : ",elapsed_time_pc_1/n)
start_pc_2 = time.perf_counter()

for i in range(n):
    shuffle(list_test_triee)
end_pc = time.perf_counter()
elapsed_time_pc_2 = end_pc-start_pc_2
print("le temps d’exécution moyen de la fonction shuffle : ",elapsed_time_pc_2/n)
my_lst_to_sort = [10, 9, 8, 7, 7, 5, 4, 3, 2, 1, 0, -1]
print(tri_list(my_lst_to_sort))
