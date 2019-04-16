# coding: utf-8
import tme1_3i25_exemple as exemple
#import time
# Pour pouvoir utiliser les methodes de exemple.py
#listes de preferences des etudiants et des masters
#a faire aussi avec la liste generee
#partie 1 du TP
listePrefEtu = exemple.lectureFichierEtu("TestPrefEtu.txt")
listePrefSpe, capacite = exemple.lectureFichierSpe("TestPrefSpe.txt") 
#on lance l'algo
"""
a, b = exemple.gs_etu(listePrefEtu,capacite,listePrefSpe)
print("Gale-Shapley cote etudiant")
print("liste des masters choisis pour chaque etudiant : ")
print(a)
print("liste des etudiants qui font le master pour chaque master : ")
print(b)
c, d = exemple.gs_master(listePrefEtu, capacite, listePrefSpe)
print("Gale-Shapley cote master")
print("liste des masters choisis pour chaque etudiant : ")
print(c)
print("liste des etudiants qui font le master pour chaque master : ")
print(d)
#on regarde s'il y a des instabilites
instableE = exemple.detecteur_dinstabilite_temporelle(listePrefEtu, listePrefSpe, a)
print("instabilites cote etudiants : \n", instableE)

instableM = exemple.detecteur_dinstabilite_temporelle(listePrefEtu,listePrefSpe,c)
print("instabilites cote masters : \n", instableM)
"""


exemple.createFichierLP_test("monFichierLP.lp",5,listePrefEtu,listePrefSpe,capacite)
#partie 2 du TP
"""NB_ETU = 3000
tmp1 = time.clock()
prefEtuRandom = exemple.genere_tableau_prefEtu(NB_ETU)
prefMasterRandom = exemple.genere_tableau_prefMaster(NB_ETU)
capa = exemple.genere_capaciteMaster(NB_ETU)
a1, a2 = exemple.gs_etu(prefEtuRandom, capa, prefMasterRandom)
print("Gale-Shapley aleatoire cote etudiant : ")
print("liste des masters choisis pour chaque etudiant : ")
print(a1)
print("liste des etudiants qui font le master pour chaque master : ")
print(a2)
instableEtuRandom = exemple.detecteur_dinstabilite_temporelle(prefEtuRandom, prefMasterRandom, a1)
print("instabilites cote etudiants : \n", instableEtuRandom)
tmp2 = time.clock()
print("temps d'execution : ", tmp2 - tmp1)
print("NB_ETU = ", NB_ETU)"""
"""
NB_ETU = 3000
tmp1 = time.clock()
prefEtuRandom = exemple.genere_tableau_prefEtu(NB_ETU)
prefMasterRandom = exemple.genere_tableau_prefMaster(NB_ETU)
capa = exemple.genere_capaciteMaster(NB_ETU)
a1, a2 = exemple.gs_master(prefEtuRandom, capa, prefMasterRandom)
print("Gale-Shapley aleatoire cote etudiant : ")
print("liste des masters choisis pour chaque etudiant : ")
print(a1)
print("liste des etudiants qui font le master pour chaque master : ")
print(a2)
#instableEtuRandom = exemple.detecteur_dinstabilite_temporelle(prefEtuRandom, prefMasterRandom, a1)
#print("instabilites cote etudiants : \n", instableEtuRandom)
tmp2 = time.clock()
print("temps d'execution : ", tmp2 - tmp1)
print("NB_ETU = ", NB_ETU)
"""
