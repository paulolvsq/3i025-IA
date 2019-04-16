# coding: utf-8

import random

def lectureFichierEtu(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne
    monFichier.close() #Fermeture du fichier
    nbEtu = int(contenu[0])
    contenu2 = []
    contenu3 = []
    for i in range(nbEtu):
        contenu2.append(contenu[i+1].split("\t"))
        contenu3.append([])
        for j in range(len(contenu2[i])-2):
            contenu3[i].append(int(contenu2[i][j+2]))
    return contenu3
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)

def lectureFichierSpe(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne
    monFichier.close() #Fermeture du fichier
    nbEtu = contenu[0].split()
    nbEtu = int(nbEtu[1])
    captmp = contenu[1].split()
    capacite = []
    for i in range(1,len(captmp)):
        capacite.append(int(captmp[i]))
    contenu2 = []
    contenu3 = []
    for i in range(9):
        contenu2.append(contenu[i+2].split("\t"))
        contenu3.append([])
        for j in range(len(contenu2[i])-2):
            contenu3[i].append(int(contenu2[i][j+2]))
    return contenu3,capacite

def gs_etu(listeEtudiants,listeCapacite,listeMasters):
    resEtu = [] #liste des masters affectes aux etudiants
    freeEtu = [] #liste disant si un etudiant i est affecté ou pas
    resMaster = [] #liste des etudiants affectes aux masters
    capaMaster = listeCapacite.copy() #liste des places restantes dans chaque master
    propEtu = [] #nombre de propositions déjà effectuées par un etudiant i
    numEtu = 0 #init de la boucle
    nbIterations = 0
    #init de toutes les listes à la con
    for i in range(len(listeEtudiants)):
        resEtu.append(None) #liste resultat vide pour le moment
        freeEtu.append(1) #tous les etudiants sont libres
        propEtu.append(0) #aucun etudiant n'a fait de proposition pour le moment
    for i in range(len(listeMasters)):
        resMaster.append([]) #liste de liste d'etudiant pour chaque master
    while(sum(freeEtu)): #tant qu'ily a au moins un etudiant sans master
        if freeEtu[numEtu]: #si l'etudiant en cours n'a pas de master
            choixMaster = listeEtudiants[numEtu][propEtu[numEtu]] #on regarde le prochain master dans ses choix
            propEtu[numEtu]+=1 #il vient de faire une proposition -> incrementation de cpt
            listePreferencesMaster = [] #liste des ordres de preferences du master demandé pour les etudiants deja inscrits dedans
            for i in resMaster[choixMaster]: #on remplit la liste
                listePreferencesMaster.append(listeMasters[choixMaster].index(i))
            if len(listePreferencesMaster) > 0: #si la liste est pas vide, on note la preference du master pour le "pire" etudiant inscrit dans ordrePireEtu
                ordrePireEtu = max(listePreferencesMaster)
            if capaMaster[choixMaster]: #si le master n'est pas plein, on s'inscrit (rien de fou)
                capaMaster[choixMaster] -= 1 #on deceremente la capacite du master
                freeEtu[numEtu] = 0 #l'etudiant courant n'est plus libre
                resMaster[choixMaster].append(numEtu) #on ajoute a la liste resultat a l'indice du master l'etudiant qui a ce master
            elif listeMasters[choixMaster].index(numEtu) < ordrePireEtu: #si le master est plein mais que le master nous prefere à son pire etudiant
                freeEtu[numEtu] = 0 #on s'inscrit
                tmp= listeMasters[choixMaster][ordrePireEtu] #l'etudiant qui est dans le master mais dont ce dernier souhaite se débarasser
                freeEtu[tmp] = 1 #on remet l'autre mec en liste d'attente
                resMaster[choixMaster].remove(tmp) #on le desinscrit du master
                resMaster[choixMaster].append(numEtu) #on prend sa place
        nbIterations += 1
        numEtu = (numEtu+1)%len(listeEtudiants) #on fait tourner pour que les autres puissent avoir des places
    for i in range(len(resMaster)): #creation de resEtu à partir de resmaster, en regardant les correspondances directement c'est izi
        resMaster[i] = sorted(resMaster[i]) #on trie la liste (pas forcément opti niveau complexite -> tri en n log n)
        for j in range(len(resMaster[i])): #on parcourt chaque sous liste 
            resEtu[resMaster[i][j]] = i #on met dans la liste resultat chaque etudiant a l'indice de son master
    print("Nb iterations : ", nbIterations)
    return resEtu, resMaster


def gs_master(listeEtudiants,listeCapacite,listeMasters):
    resEtu = [] #liste des masters affectés aux etudiants
    freeEtu = [] #liste disant si un etudiant i est affecté ou pas
    resMaster = [] #liste des étudiants affectés aux masters
    capaMaster = listeCapacite.copy() #liste des places restantes dans chaque master
    propMaster = [] #nombre de propositions déjà effectuées par un etudiant i
    nbIterations = 0
    #init de toutes les listes
    for i in range(len(listeEtudiants)):
        resEtu.append(None) #liste resultat vide pour le moment
        freeEtu.append(1) #tous les etudiants sont libres
    for i in range(len(listeMasters)):
        resMaster.append([]) #liste de listes d'etudiants pour chaque master
        propMaster.append(0) #aucun master n'a propose a un etudiant pour le moment
    numMaster = 0 #init de la boucle
    while(sum(capaMaster)): #tant que tous les masters n'ont pas trouve un etudiant
        if capaMaster[numMaster]: #s'il reste de la place dans le master courant
            choixEtu = listeMasters[numMaster][propMaster[numMaster]] #on recupere le choix du master qui correspond a un etudiant
            propMaster[numMaster] += 1 #on incremente le nombre de propositions faites par un master
            if freeEtu[choixEtu]: #si l'etudiant est libre
                freeEtu[choixEtu] = 0 #l'etudiant n'est plus libre
                capaMaster[numMaster] -= 1 #on reserve sa place en master
                resEtu[choixEtu] = numMaster #on ajoute a la liste resultat le master a l'indice de l'etudiant
            elif listeEtudiants[choixEtu].index(numMaster) < listeEtudiants[choixEtu].index(resEtu[choixEtu]): #sinon s'il existe un etudiant prefere par le master courant
                capaMaster[numMaster] -= 1 #on reserve sa place dans le nouveau master
                capaMaster[resEtu[choixEtu]] += 1 #l'ancien master de l'etudiant : resEtu[etu] -> on rend sa place dispo pour d'autres etudiants
                resEtu[choixEtu] = numMaster #on ajoute a la liste resultat le master a l'indice de l'etudiant 
        numMaster = (numMaster+1)%len(listeMasters) #on fait tourner pour que les autres puissent avoir des places
        nbIterations += 1
    for i in range(len(resEtu)): #creation de resEtu à partir de resmaster, en regardant les correspondances directement c'est izi
        resMaster[resEtu[i]].append(i) #on ajoute les etudiants dans les sous listes de resMaster pour avoir les listes d'etudiants associes a un master
    for i in range(len(resMaster)): #on parcourt la liste des listes d'etudiants pour chaque master
        resMaster[i] = sorted(resMaster[i]) #on les trie (pas forcement opti niveau complexite -> tri en n log n)
    print("Nb iterations : ", nbIterations)
    return resEtu, resMaster

def detecteur_dinstabilite_temporelle(listea, listeb, listeAffectations):
    res = [] #liste resultat des paires instables
    if len(listea) == len(listeAffectations): 
        longueurliste = len(listea)
        listereference = listea
        autreliste = listeb
    else:
        longueurliste = len(listeb)
        listereference = listeb
        autreliste = listea
    for i in range(longueurliste):
        #pour chaque etudiant
        #pour chaque master qu'il prefere a celui qu'il a
        #on verifie si le master prefere lui ou son pire etudiant
        if isinstance(listeAffectations[0], int): #on regarde si on est devant une liste ou une liste de listes selon le cas qu'on va traiter
            restmp = internal_function1(listereference, autreliste, listeAffectations, i) #on regarde si on a une paire instable
            if restmp != None: #si la paire instable n'est pas nulle 
                res.append(restmp) #on la met dans la liste resultat
        elif isinstance(listeAffectations[0], list): #on regarde si on est devant une liste ou une liste de listes
            for z in range(len(listeAffectations[i])): #on parcourt chaque sous liste
                print("les données entrées sont traitées par un code non encore implémenté, veuillez réessayer plus tard")
                return
                restmp =internal_function2(listereference, autreliste, listeAffectations, i, z) #on regarde si on a une paire instable
                if restmp != None: #si la paire instable n'est pas nulle
                    res.append(restmp) #on la met dans la liste resultat
    if len(res) == 0: #si la liste resultat est vide
        return "ptdr y en a pas" #on n'a pas de paire instable
    return res


def internal_function1(listereference, autreliste, listeAffectations, i):
    ordre_preference = listereference[i].index(listeAffectations[i]) #on recupere l'indice de preference du master a l'indice i
    for j in range(ordre_preference-1): #on parcourt tous les masters qu'il y a avant
        meilleurChoix = listereference[i][j] #on recupere un meilleur choix a chaque fois
        l = [] #liste vide qui va contenir les preferences eventuelles
        for k in range(len(listeAffectations)): #on parcourt la liste des affectations pour l'etudiant
            if listeAffectations[k] == meilleurChoix: #on regarde s'il y a dans la liste un master qui serait un meilleur choix
                tmp = autreliste[meilleurChoix].index(k) #dans ce cas on conserve la preference
                l.append(tmp) #on l'ajoute a la liste resultat
        if autreliste[meilleurChoix].index(i) < max(l): #on regarde s'il y a un meilleur choix possible dans la liste des meilleurs choix qu'on vient de determiner
            return [i, listeAffectations[i]] #dans ce cas on le renvoie c'est une paire instable
    return #autrement on renvoie None

def internal_function2(listereference,autreliste,listeAffectations,i,z): #marche pas encore 
    #meme schema que precedemment mais on doit faire ca pour des listes de listes -> listes d'etudiants pour chaque master
    ordre_preference = listereference[i].index(listeAffectations[i][z])
    for j in range(ordre_preference-1):
        meilleurChoix = listereference[i][j]
        l = []
        for k in range(len(listeAffectations)):
            for y in range(len(listeAffectations[k])):
                if listeAffectations[k][y] == meilleurChoix:
                    tmp = autreliste[meilleurChoix].index(y)
                    #print(autreliste[meilleurChoix],tmp)
                    l.append(tmp)
        ll = -(2**31)
        for ind in range(z):
            ll = max(autreliste[meilleurChoix].index(ind),ll)
        if ll < max(l):
            return [i,listeAffectations[i][z]]
    return

def genere_tableau_prefEtu(n):
    R = [] #liste resultat
    for i in range(n): #pour tous les etudiants de 0 a n
        L = [0, 1, 2, 3, 4, 5, 6, 7, 8] #on definit la liste des masters
        random.shuffle(L) #on la melange
        R.append(L) #on la met dans la liste resultat
    return R
    
def genere_tableau_prefMaster(n):
    L = [] #liste resultat
    for i in range(9): #pour chaque parcours en master
        L.append(random.sample(range(0, n), n)) #on ajoute une liste dans L avec des nombres uniques tires entre 0 et n
    return L
    
def genere_capaciteMaster(n):
    L = [0, 0, 0, 0, 0, 0, 0, 0, 0] #liste resultat
    R = [0, 1, 2, 3, 4, 5, 6, 7, 8] #liste des indices a incrementer
    for i in range(n):
        value = random.choice(R)
        L[value] += 1
    return L
    
    
def createFichierLP(nomFichier,nombreVariables):
    monFichier=open(nomFichier,"w") #Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    monFichier.write("obj: ")
    for i in range(0,nombreVariables): #Boucle i variant de 0 a NombreVariables-1
        monFichier.write("x"+str(i)+" ") #write pour ecrire. Indentation
        if (i<nombreVariables-1): # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
            monFichier.write("+ ")
        else:
            monFichier.write("\n")
    monFichier.write("Subject To\n")
    monFichier.write("c1: \nc2: \nc3: \nBounds\n\n")
    monFichier.write("Binary\n")
    for i in range(0,nombreVariables):
        monFichier.write("x"+str(i)+" ")
    monFichier.write("\n")
    monFichier.write("End")
    monFichier.close()
    return
    """
def createFichierLP_test(nomFichier,k,listeEtu,listeMaster,listeCapa):
    monFichier=open(nomFichier,"w") #Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    monFichier.write("obj: ")
    listeVariables = []
    for i in range(len(listeEtu)): #Boucle i variant de 0 a NombreVariables-1
        listeVariables.append([])
        for j in range(k):            
            listeVariables[i].append(listeEtu[i][j])
            #monFichier.write(str(k-j)+" x"+str(i)+"_"+str(listeEtu[i][j])+" ")
            monFichier.write("x"+str(i)+"_"+str(listeEtu[i][j])+" ")
            if (i<len(listeEtu)-1 or j < k -1): # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
                monFichier.write("+ ")
            else:
                monFichier.write("\n")
    print(listeVariables)
    monFichier.write("Subject To\n")
    for i in range(len(listeEtu)):        
        monFichier.write("c"+str(i+1)+": ")
        for j in range(k):
            monFichier.write("x"+str(i)+"_"+str(listeEtu[i][j])+" ") 
            if (j < k -1):
                monFichier.write("+ ")
            else:
                sommePlacesMaster = 0
                for a in listeVariables[i]:
                    sommePlacesMaster += listeCapa[a]
                monFichier.write(" <= "+str(sommePlacesMaster)+"\n")
    monFichier.write("Bounds\n")
    monFichier.write("Binary\n")
    for i in range(0,len(listeEtu)):
        for j in range(k):
            monFichier.write("x"+str(i)+"_"+str(listeEtu[i][j])+" ")
    monFichier.write("\n")
    monFichier.write("End")
    monFichier.close()
    return
 
    """
def createFichierLP_test(nomFichier,k,listeEtu,listeMaster,listeCapa):
    monFichier=open(nomFichier,"w") #Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    monFichier.write("obj: ")
    listeVariables = []
    for i in range(len(listeEtu)): #Boucle i variant de 0 a NombreVariables-1
        listeVariables.append([])
        for j in range(k): 
            #if i in listeMaster[listeEtu[i][j]][:k]:
            listeVariables[i].append(listeEtu[i][j])                
                #monFichier.write(str(k-j)+" x"+str(i)+"_"+str(listeEtu[i][j])+" ")
    
    cpt = 0
    tmp = 0
    for i in range(len(listeEtu)):
        for j in listeVariables[i]:
            cpt+=1
    for i in range(len(listeEtu)):
        for j in listeVariables[i]:
            monFichier.write("x"+str(i)+"_"+str(j)+" ")
            if ( tmp<cpt-1 ): # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
                monFichier.write("+ ")
            tmp+=1
    monFichier.write("\n")
    print(listeVariables)
    cptCond = 0
    monFichier.write("Subject To\n")
    for i in range(len(listeEtu)):    
        if(len(listeVariables[i])):
            monFichier.write("c"+str(cptCond)+": ")
            cptCond+=1
        tmp1 = 0
        for j in listeVariables[i]:
            monFichier.write("x"+str(i)+"_"+str(j)+" ") 
            if (tmp1 < len(listeVariables[i]) -1):
                monFichier.write("+ ")
            else:
                monFichier.write("= 1\n")
            tmp1+=1
    
    for a in range(len(listeMaster)):
        monFichier.write("c"+str(cptCond)+": ")
        cptCond+=1
        cpt = 0
        tmp = 0
        for i in range(len(listeVariables)):
            for j in range(len(listeVariables[i])):
                if(listeVariables[i][j] == a):
                    cpt+=1
        
        for i in range(len(listeVariables)):
            for j in range(len(listeVariables[i])):
                if listeVariables[i][j] == a:
                    monFichier.write("x"+str(i)+"_"+str(a)+" ")
                    if(tmp<cpt-1):
                        monFichier.write("+ ")
                    tmp+=1
        if(i == len(listeVariables)-1 and j == len(listeVariables[i])-1):
            monFichier.write("= "+str(listeCapa[a])+"\n")
        
        
    monFichier.write("Bounds\n")
    monFichier.write("Binary\n")
    for i in range(0,len(listeEtu)):
        for j in listeVariables[i]:
            monFichier.write("x"+str(i)+"_"+str(j)+" ")
    monFichier.write("\n")
    monFichier.write("End")
    monFichier.close()
    return
    

       
    
    
    
    
    
    
    