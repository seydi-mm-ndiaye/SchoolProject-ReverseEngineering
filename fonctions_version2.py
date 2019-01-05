#coding:utf-8

import svgwrite

#Fonction transformant la commande en objet de type list contenant les differentes parties de la commande.
def decoupeChaine(chaine):
  liste = chaine.split(" ")
  return liste

#Fonction vérifiant la syntaxe.
def verifSyntaxe(liste):
  if len(liste)==7 or len(liste)==8 :#Vérifie si on a le nombre minimum ou maximum de paramètres
     if len(liste)==7:#Si l'option '-t' n'est pas utilisée.
       if liste[1]!="-i":#Si l'option '-i' n'est pas utilisée.
        return 2
       else:
         if liste[2]!="xml" and liste[2]!="json":#Si le format n'est pas correctement spécifié.
           return 3
         else : 
            if liste[3]!="-f" and liste[3]!="-h" :#Si l'option '-f' ou '-h' n'est pas correctement spécifié.  
               return 4
            else:
              if liste[3]=="-f" and ((liste[2]=="xml" and liste[4].find(".xml")==-1)or(liste[2]=="json" and liste[4].find(".json")==-1)):
                return 5
              else:
                 if liste[5]!="-o" :#Si l'option '-o' n'est pas spécifié.
                   return 6
                 else:
                   if liste[6].find(".svg")==-1 :#Si le format du fichier de sortie n'est pas SVG.
                     return 7
                   else:
                     return 0 #Si la commande est correcte on renvoie 0.        
     
     else:#Si l'option '-t' est utilisé. 
       if liste[1]!="-i" :
          return 2
       else:
         if liste[2]!="xml" and liste[2]!="json" :
           return 3
         else:
           if liste[3]!="-t":
             return 8
           else:
             if liste[4]!="-f" and liste[4]!="-h":
               return 4
             else:
               if (liste[2]=="xml" and liste[5].find(".xml")==-1)or(liste[2]=="json" and liste[5].find(".json")==-1):      
                  return 5
               else:
                 if liste[6]!="-o":
                   return 6
                 else:
                   if liste[7].find(".svg")==-1:
                      return 7
                   else:
                     return 0                
  else:#Si le nombre de parametre fourni dépasse 8 ou est moins de 7
     return 1
  
  
  
#Fonction affichant le type d'erreur suivant le chiffre retourné par la fonction verifSyntaxe.
def messageErreur(code):
  if code==1: print("Erreur : le nombre de parametre doit etre egal à 7 ou 8.\n")
  elif code==2: print("Erreur : l'option '-i' est absente dans la comande.\n")
  elif code==3: print("Erreur : le format du fichier d'entrée n'est pas spécifié('xml' ou 'json').\n")
  elif code==4: print("Erreur : l'option '-f' ou '-h' n'est pas spécifié.\n")
  elif code==5: print("Erreur : le format du fichier d'entrée doit etre XML ou JSON en accord avec le parametre '-i'.\n")
  elif code==6: print("Erreur : l'optin '-o' n'est pas spécifié.\n")
  elif code==7: print("Erreur : le format du fichier de sortie doit etre SVG.\n")
  else: print("Erreur : l'option '-t' n'est pas spécifié.\n")
  
#Fonction créant les graphes des entités et des associations.     
def creationGraphe(dwg,nElemnt):
  
  #Rectangle principal.
  dwg.add(dwg.rect(insert=(0, 0), size=(650*nElemnt, 300*nElemnt),fill='white', stroke='black'))
  
  i=0
  X1,Y1 = 200,100#Abscisse et ordonnée du rectangle.
  largr,longr=300,40
  XC,YC=700,Y1+longr*2#Abscisse et ordonnée du centre.
  XR,YR=100,50#Abscisse et ordonnée du rayon.
  X2,Y2=850,100#Abscisse et ordonnée du rectangle.
  while i<nElemnt:    
      #--Rectangle accueillant l'entité. 
      dwg.add(dwg.rect(insert=(X1, Y1), size=(largr, longr*4),fill='white', stroke='black'))
      #Ligne séparant le nom de l'entité et ses attributs.
      hline = dwg.add(dwg.g(id='hline', stroke='black'))
      hline.add(dwg.line(start=(X1,(Y1+30)),end=((largr+X1),(Y1+30))))
     
      #--Cercle accueillant l'association.
      dwg.add(dwg.ellipse(center=(XC, YC), r=(XR, YR),fill='white',stroke='black'))
      #Ligne séparant l'association et ses attributs.
      hline = dwg.add(dwg.g(id='hline', stroke='black'))
      hline.add(dwg.line(start=(XC-XR,YC),end=(XC+XR,YC)))
          
      #--Rectangle accueillant l'entité.
      dwg.add(dwg.rect(insert=(X2, Y2), size=(largr, longr*4),fill='white', stroke='black'))
      #Ligne séparant le nom de l'entité et ses attributs.
      hline = dwg.add(dwg.g(id='hline', stroke='black'))
      hline.add(dwg.line(start=(X2,(Y2+30)),end=((largr+X2),(Y2+30))))
      
      #--Ligne reliant les entités et les associations.
      hline = dwg.add(dwg.g(id='hline', stroke='black'))
      hline.add(dwg.line(start=(X1+largr,YC),end=(XC-XR,YC)))
      hline = dwg.add(dwg.g(id='hline', stroke='black'))
      hline.add(dwg.line(start=(XC+XR,YC),end=(X2,YC)))     
      
      Y1+=250
      Y2=Y1
      YC=Y1+longr*2
      i+=1
  return dwg               
     
#Fonction remplissant les valeurs des attributs.
def attributXML(dwg, nElemnt, Element_EA):
  
  X1,Y1 = 200,100
  X2,Y2=850,100
  i=0
  
  while (i+2)<nElemnt: 
  #Texte entité 1
      dwg.add(dwg.text(Element_EA[i].tag,insert=(X1+10,Y1+25),font_size=30))
      dwg.add(dwg.text("+NumClient: "+Element_EA[i].attrib["NumClient"],insert=(X1+9,Y1+50),font_size=20))
      dwg.add(dwg.text("Prenom: "+Element_EA[i].attrib["prenom"],insert=(X1+9,Y1+80),font_size=20))
      dwg.add(dwg.text("Nom: "+Element_EA[i].attrib["nom"],insert=(X1+9,Y1+110),font_size=20))
      dwg.add(dwg.text("Adresse: "+Element_EA[i].attrib["adresse"],insert=(X1+9,Y1+140),font_size=20))
      
      
      #Texte entité 2
      dwg.add(dwg.text(Element_EA[i+2].tag,insert=(X2+10,Y2+25),font_size=30))
      dwg.add(dwg.text("+NumPrduit: "+Element_EA[i+2].attrib["NumPrduit"],insert=(X2+9,Y2+50),font_size=20))
      dwg.add(dwg.text("nomProduit: "+Element_EA[i+2].attrib["nomProduit"],insert=(X2+8,Y2+80),font_size=20))
      
      #Texte association
      dwg.add(dwg.text(Element_EA[i+1].tag,insert=(630,Y1+70),font_size=30))
      dwg.add(dwg.text("NumCommande: "+Element_EA[i+1].attrib["NumCommande"],insert=(635,Y1+95),font_size=15))
      dwg.add(dwg.text("Date: "+Element_EA[i+1].attrib["date"],insert=(635,Y1+110),font_size=15))
      dwg.add(dwg.text("Quantite: "+Element_EA[i+1].attrib["quantite"],insert=(650,Y1+125),font_size=15))
      
      Y1+=250
      Y2=Y1
      i+=3
#Fonction qui affiche les entités et les relations à l'écran. 
def  afficheEntiteXML(nElemnt,Element_EA):
   i=0
   j=0
   while (i+2<nElemnt) :
      print("Commande n° ",j+1,"\n")
      print("->"+Element_EA[i].tag+"( N°:"+Element_EA[i].attrib["NumClient"]+", Prenom: "+Element_EA[i].attrib["prenom"]+", Nom: "+Element_EA[i].attrib["nom"]+", Adresse: "+Element_EA[i].attrib["adresse"]+")")
      print("->"+Element_EA[i+1].tag+"(N°:"+Element_EA[i+1].attrib["NumCommande"]+", Date: "+Element_EA[i+1].attrib["date"]+", Quantité: "+Element_EA[i+1].attrib["quantite"]+")")
      print("->"+Element_EA[i+2].tag+"(N°: "+Element_EA[i+2].attrib["NumPrduit"]+", Nom produit: "+Element_EA[i+2].attrib["nomProduit"]+")\n")
      i+=3
      j+=1     
      
#Fonction remplissant les attributs des entités extraits du fichier JSON.                    
def attributJSON(dwg, nElemnt, entite):                    
                    
  X1,Y1 = 200,100
  X2,Y2=850,100
  i=0
  cles=list(entite[0].keys())

  while (i)<nElemnt: 
  #Texte entité 1
      dwg.add(dwg.text(cles[0],insert=(X1+10,Y1+25),font_size=30))
      dwg.add(dwg.text("+NumClient: "+entite[i][cles[0]]["NumClient"],insert=(X1+9,Y1+50),font_size=20))
      dwg.add(dwg.text("Prenom: "+entite[i][cles[0]]["prenom"],insert=(X1+9,Y1+80),font_size=20))
      dwg.add(dwg.text("Nom: "+entite[i][cles[0]]["nom"],insert=(X1+9,Y1+110),font_size=20))
      dwg.add(dwg.text("Adresse: "+entite[i][cles[0]]["adresse"],insert=(X1+9,Y1+140),font_size=20))
      
      
      #Texte entité 2
      dwg.add(dwg.text(cles[2],insert=(X2+10,Y2+25),font_size=30))
      dwg.add(dwg.text("+NumPrduit: "+entite[i][cles[2]]["NumProduit"],insert=(X2+9,Y2+50),font_size=20))
      dwg.add(dwg.text("nomProduit: "+entite[i][cles[2]]["NomProduit"],insert=(X2+8,Y2+80),font_size=20))
      
      #Texte association
      dwg.add(dwg.text(cles[1],insert=(630,Y1+70),font_size=30))
      dwg.add(dwg.text("NumCommande: "+entite[i][cles[1]]["NumCommande"],insert=(635,Y1+95),font_size=15))
      dwg.add(dwg.text("Date: "+entite[i][cles[1]]["date"],insert=(635,Y1+110),font_size=15))
      dwg.add(dwg.text("Quantite: "+entite[i][cles[1]]["quantite"],insert=(650,Y1+125),font_size=15))
      
      Y1+=250
      Y2=Y1
      i+=1                 
                    
                    
def afficheEntiteJSON(nElemnt, entite):                    
   i=0
   
   cles=list(entite[0].keys())
   while (i<nElemnt) :
      print("Commande n° ",i+1,"\n")
      print("->"+cles[0]+"( N°:"+entite[i][cles[0]]["NumClient"]+", Prenom: "+entite[i][cles[0]]["prenom"]+", Nom: "+entite[i][cles[0]]["nom"]+", Adresse: "+entite[i][cles[0]]["adresse"]+")")
      print("->"+cles[1]+"(N°:"+entite[i][cles[1]]["NumCommande"]+", Date: "+entite[i][cles[1]]["date"]+", Quantité: "+entite[i][cles[1]]["quantite"]+")")
      print("->"+cles[2]+"(N°: "+entite[i][cles[2]]["NumProduit"]+", Nom produit: "+entite[i][cles[2]]["NomProduit"]+")\n")
      i+=1
                   
                    
                    
                    
                    
                    
                    
                    
