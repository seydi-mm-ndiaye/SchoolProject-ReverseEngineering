#coding : utf-8

try:
 import os
 from lxml import etree
 from fonctions_version2 import *
 import json
 import requests
 liste = list()

 #1---On vérifie si le nom de la commande et les parametres entrés sont exactes.
 entree = input("Entrer une commande : ")
 liste = decoupeChaine(entree) 
 while ( liste[0]!="XJ_Convertor" or verifSyntaxe(liste)) :   
    #Vérifie si le nom de la commande est exacte.
    if (liste[0]!="XJ_Convertor"):
      print("Erreur : commande '{}' invalide.\n".format(liste[0]))
      print("La commande est : XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
  
    if (liste[0]=="XJ_Convertor" and verifSyntaxe(liste)!=0):
       messageErreur(verifSyntaxe(liste))  
       print("La commande est : XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
    
    entree = input("Entrer une commande : ")
    liste = decoupeChaine(entree)   
         
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
       dwg=svgwrite.Drawing(liste[6],profile='full',size=('100%','100%'),fill='blue')
       creationGraphe(dwg,len(entite_association))
      #Titre
       dwg.add(dwg.text("DONNEES DU FICHIER XML :",insert=(400,80),font_size=50))
       attributXML(dwg,len(Element_EA),Element_EA)
       dwg.save()
       print("Fichier '"+liste[6]+"' bien généré.\n")
   #2.1.2---Si le parametre '-h' est utilisé :  
     else:
       try: 
        donnees = requests.get(liste[4])
        print(donnees.text)
       except Exception as err:
         print("Erreur URL : ",err)
         exit()
         
       test = open("tmp.xml","w")
       test.write(donnees.text)
       test.close()  
       #On n'accede à cette partie si l'url est valide.
       try: 
         validation = etree.XMLParser() 
         arbre = etree.parse("tmp.xml", validation)
       except Exception as err0: 
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
       dwg=svgwrite.Drawing(liste[6],profile='full', size=('100%','100%'),fill='blue')
       creationGraphe(dwg,len(entite_association))
      #Titre
       dwg.add(dwg.text("DONNEES DU FICHIER XML :",insert=(400,80),font_size=50))
       attributXML(dwg,len(Element_EA),Element_EA)
       dwg.save()
       print("Fichier '"+liste[6]+"' bien généré.\n")     
       os.remove("tmp.xml")
  #2.2---Si le parametre '-t' est utilisé : 
    else:
    #2.2.1---Si le parametre '-f' est utilisé :
       if(liste[4]=="-f") :
          try: 
           validation = etree.XMLParser() 
           arbre = etree.parse(liste[5], validation)
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
        
      #Affichage des entités et des relations.
          afficheEntiteXML(len(Element_EA),Element_EA)
           
      #Création du fichier SVG  
          dwg=svgwrite.Drawing(liste[7],profile='full', size=('100%','100%'),fill='blue')
          creationGraphe(dwg,len(entite_association))
      #Titre
          dwg.add(dwg.text("DONNEES DU FICHIER XML :",insert=(400,80),font_size=50))
          attributXML(dwg,len(Element_EA),Element_EA)
          dwg.save()
          print("Fichier '"+liste[7]+"' bien généré.\n")
      
    #2.2.2---Si le parametre '-h' est utilisé :  
       else:          
         try: 
          donnees = requests.get(liste[5])
          print(donnees.text)
         except Exception as err:
          print("Erreur URL : ",err)
          exit()
         
         test = open("tmp.xml","w")
         test.write(donnees.text)
         test.close()  
       #On n'accede à cette partie si l'url est valide.
         try: 
          validation = etree.XMLParser() 
          arbre = etree.parse("tmp.xml", validation)
         except Exception as err0: 
          print ("Erreur de syntaxe XML : ",err0) 
          exit()
         
       #On n'accede à cette partie si l'url est valide.
         try:  
           validation = etree.XMLParser() 
           arbre = etree.parse("tmp.xml", validation)
         except Exception as err0: 
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
        
      #Affichage des entités et des relations.
         afficheEntiteXML(len(Element_EA),Element_EA)
           
      #Création du fichier SVG  
         dwg=svgwrite.Drawing(liste[7],profile='full', size=('100%','100%'),fill='blue')
         creationGraphe(dwg,len(entite_association))
      #Titre
         dwg.add(dwg.text("DONNEES DU FICHIER XML :",insert=(400,80),font_size=50))
         attributXML(dwg,len(Element_EA),Element_EA)
         dwg.save()
         print("Fichier '"+liste[7]+"' bien généré.\n")
         os.remove("tmp.xml") 
#3---Cas d'un fichier JSON :
 else:#Nous avons 'json' apres l'otion '-i'.
    #3.1---Si le parametre '-t' n'est pas utilisé :
     if(len(liste)==7):
      #3.1.1---Si le parametre '-f' est utilisé :     
       if(liste[3]=="-f"):
         try:
          with open(liste[4]) as fichierJson:
           donnees=json.load(fichierJson)
           
         except FileNotFoundError:
           print("Le fichier '"+liste[4]+"' n'existe pas.\n")  
         except json.JSONDecodeError as err:    
          print("Erreur de syntaxe JSON : ",err) 
         #On accede a cette partie que lorsque le document json est valide.
         with open(liste[4]) as fichierJson:
          donnees=json.load(fichierJson) 
          nombreEA=len(donnees["Vente"]["entite_association"])
          #Création du fichier SVG.
          dwg=svgwrite.Drawing(liste[6],profile='full', size=('100%','100%'),fill='blue')
          creationGraphe(dwg, nombreEA)#On crée un nombre de graphe égal au nombre d'entité association.
          #Titre
          dwg.add(dwg.text("DONNEES DU FICHIER JSON :",insert=(400,80),font_size=50))
          attributJSON(dwg, (nombreEA), donnees["Vente"]["entite_association"])
          dwg.save()
          print("Fichier '"+liste[6]+"' bien généré.\n")
      #3.1.2---Si le parametre '-h' est utilisé : 
       else:
         try: 
          donnees = requests.get(liste[4])
          print(donnees.text)
         except Exception as err:
          print("Erreur URL : ",err)
          exit()
         
         test = open("tmp.json","w")
         test.write(donnees.text)
         test.close()  
       #On n'accede à cette partie si l'url est valide.
         try:
          with open("tmp.json") as fichierJson:
           donnees=json.load(fichierJson)
            
         except json.JSONDecodeError as err:    
          print("Erreur de syntaxe JSON : ",err) 
         #On accede a cette partie que lorsque le document json est valide.
         with open("tmp.json") as fichierJson:
          donnees=json.load(fichierJson) 
          nombreEA=len(donnees["Vente"]["entite_association"])
          #Création du fichier SVG.
          dwg=svgwrite.Drawing(liste[6],profile='full', size=('100%','100%'),fill='blue')
          creationGraphe(dwg, nombreEA)#On crée un nombre de graphe égal au nombre d'entité association.
          #Titre
          dwg.add(dwg.text("DONNEES DU FICHIER JSON :",insert=(400,80),font_size=50))
          attributJSON(dwg, (nombreEA), donnees["Vente"]["entite_association"])
          dwg.save()
          print("Fichier '"+liste[6]+"' bien généré.\n")
          os.remove("tmp.json")
    #3.2---Si le parametre '-t' est utilisé :     
     else:#Si le nombre de parametre est égal à 8
      #3.2.1---Si le parametre '-f' est utilisé :      
       if(liste[4]=="-f"):
         try:
          with open(liste[5]) as fichierJson:
           donnees=json.load(fichierJson)
           
         except FileNotFoundError:
           print("Le fichier '"+liste[5]+"' n'existe pas.\n")  
         except json.decoder.JSONDecodeError as err:    
           print("Erreur de syntaxe JSON : ",err)
           
         #On accede a cette partie que lorsque le document json est valide.
         with open(liste[5]) as fichierJson:
          donnees=json.load(fichierJson) 
          nombreEA=len(donnees["Vente"]["entite_association"])
          
          #Affichage des entités et des relations au niveau du terminal.
          afficheEntiteJSON(nombreEA, donnees["Vente"]["entite_association"])
          
          #Création du fichier SVG.
          dwg=svgwrite.Drawing(liste[7],profile='full', size=('100%','100%'), fill='blue')
          creationGraphe(dwg, nombreEA)#On crée un nombre de graphe égal au nombre d'entité association.
          #Titre
          dwg.add(dwg.text("DONNEES DU FICHIER JSON :",insert=(400,80),font_size=50))
          attributJSON(dwg, (nombreEA), donnees["Vente"]["entite_association"])
          dwg.save()
          print("Fichier '"+liste[7]+"' bien généré.\n")
          
      #3.2.1---Si le parametre '-h' est utilisé :     
       else:
         try: 
          donnees = requests.get(liste[5])
          print(donnees.text)
         except Exception as err:
          print("Erreur URL : ",err)
          exit()
         
         test = open("tmp.json","w")
         test.write(donnees.text)
         test.close()  
       #On n'accede à cette partie si l'url est valide.
         try:
          with open("tmp.json") as fichierJson:
           donnees=json.load(fichierJson)
             
         except json.decoder.JSONDecodeError as err:    
           print("Erreur de syntaxe JSON : ",err)
           
         #On accede a cette partie que lorsque le document json est valide.
         with open("tmp.json") as fichierJson:
          donnees=json.load(fichierJson) 
          nombreEA=len(donnees["Vente"]["entite_association"])
          
          #Affichage des entités et des relations au niveau du terminal.
          afficheEntiteJSON(nombreEA, donnees["Vente"]["entite_association"])
          
          #Création du fichier SVG.
          dwg=svgwrite.Drawing(liste[7],profile='full', size=('100%','100%'), fill='blue')
          creationGraphe(dwg, nombreEA)#On crée un nombre de graphe égal au nombre d'entité association.
          #Titre
          dwg.add(dwg.text("DONNEES DU FICHIER JSON :",insert=(400,80),font_size=50))
          attributJSON(dwg, (nombreEA), donnees["Vente"]["entite_association"])
          dwg.save()
          print("Fichier '"+liste[7]+"' bien généré.\n")
          os.remove("tmp.json")
except ImportError as err:
  print("Erreur sur l'importation des modules :",err)
except KeyboardInterrupt:
 print("\nAnnulation de la commande.\nFin.\n")
except OSError as err:
 print("Erreur sur le fichier d'entrée : ",err) 
except json.decoder.JSONDecodeError as err:    
 pass  
    
     

