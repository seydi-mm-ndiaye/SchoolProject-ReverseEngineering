#coding : utf-8

import os
from lxml import etree
from fonctions import *



liste = list()

#1---On vérifie si le nom de la commande et les parametres entrés sont exactes.
while (len(liste)==0)or(liste[0]!="XJ_Convertor")or(isparamValid(liste)==0)or(valeurParam(liste)==0)or(extensionSortie (liste)==0) :
   entree = input("Entrer une commande : ")
   liste = decoupeChaine(entree)
   #Vérifie si le nom de la commande est exacte.
   if (liste[0]!="XJ_Convertor"):
     print("Erreur : commande '{}' invalide.\n\n".format(liste[0]))
     print("La commande est : XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
     continue
   #Vérifie si la liste des parametres est valides  
   if isparamValid(liste)==0 :
     print("Erreur : paramètres non valides.\n")  
     print("Les parametres valides sont : '-i', '-t', '-h', '-f' et '-o'.\n\n")
     continue
   #Si l'extension du format des fichiers fournit en entrée sont 'xml' et 'json' et aussi que le paramètre fournit au niveau du  
   #parametre -i est conforme avec le format du fichier fournit en entrée.
   if valeurParam(liste)==0 :
     print("Erreur : valeur des formats des fichiers non valides.\n")
     print("Les extensions de fichiers valide sont : 'xml' et 'json'\n\n")
     continue
   #Si l'extension du fichier de sortie est différent de "svg"
   if(extensionSortie(liste)==0) :
     print("Erreur : extension du fichier de sortie non valide.\n")
     print("L'extension du fichier de sortie doit etre : 'svg'.\n\n") 
         
#2---Cas d'un ficher XML :     
if(liste[2]=="xml") : 
  #2.1---Si le parametre '-t' n'est pas utilisé :
   if(len(liste)==7) :
  #2.1.1---Si le parametre '-f' est utilisé :
    if(liste[3]=="-f") :
      try: 
       validation = etree.XMLParser() 
       arbre = etree.parse(liste[4], validation)
      except etree.XMLSyntaxError as err0: 
       print ("Erreur de syntaxe XML : ",err0) 
       exit()
      #On accede a cette partie que lorsque notre fichier XML est valide.  
      racine = arbre.getroot()
      entite_association=list()
      Element_EA=list()
      
      for  child in racine :#Permet de recupérer les attributs principaux du fichier XML
        entite_association.append(child)#Met les elements dans une liste
        for child0 in child :#Permet de recupérer les attributs des attributs principaux. 
         Element_EA.append(child0)#Met les elements dans une liste.      
      
      #Création du fichier SVG  
      dwg=svgwrite.Drawing(liste[6],profile='full')
      creationGraphe(dwg,len(entite_association))
      attribut(dwg,len(Element_EA),Element_EA)
      dwg.save()
      print("Fichier bien généré.\n")
 
  
  
  
  
  
  
  
  
  
  
#3---Cas d'un fichier JSON :




 
    
    
     

