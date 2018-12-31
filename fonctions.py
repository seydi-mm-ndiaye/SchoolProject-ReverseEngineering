#coding:utf-8

import svgwrite

#Fonction transformant la commande en objet de type list contenant les differentes parties de la commande.
def decoupeChaine(chaine):
  liste = chaine.split(" ")
  return liste
  
#Fonction vérifiant si les parametres entrees sont valides.  
def isparamValid(liste) :
  if len(liste) == 7:
    if (liste[1]=="-i" and (liste[3]=="-h" or liste[3]=="-f") and liste[5]=="-o") :
       return 1  
    else :
       return 0   
  elif len(liste) == 8:
    if (liste[1]=="-i" and liste[3]!="-t" and (liste[4]!="-h" or liste[4]!="-f") and liste[6]!="-o") :
       return 1 
    else :
      return 0     
  else :
    return 0
    
#Fonction vérifiant si les extensions des fichiers sont valides.    
def valeurParam(liste) :
  if len(liste)==7 :
       if (liste[2]=="xml" and liste[4].split(".")[1]=="xml") or (liste[2]=="json" and liste[4].split(".")[1]=="json") :
          return 1
       else :
          return 0
  elif len(liste)==8 :
        if (liste[2]=="xml" and liste[5].split(".")[1]=="xml") or (liste[2]=="json" and liste[5].split(".")[1]=="json") :
          return 1
        else :
          return 0       
  else:
         return 0           
              
#Fonction verifiant si le fichier de sortie est  au format svg.              
def extensionSortie(liste) :
   if len(liste) == 7 and liste[6].split(".")[1]=="svg":
      return 1
   elif len(liste)==8 and liste[7].split(".")[1]=="svg":
      return 1
   else :
     return 0      
#Fonction créant les graphes des entités et des associations.     
def creationGraphe(dwg,nElemnt):
  
  #Rectangle principal.
  dwg.add(dwg.rect(insert=(0, 0), size=(650*nElemnt, 300*nElemnt),fill='white', stroke='black'))
  
  i=0
  X1,Y1 = 200,100#Abscisse et ordonnée du rectangle.
  largr,longr=200,40
  XC,YC=600,Y1+longr*2#Abscisse et ordonnée du centre.
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
def attribut(dwg, nElemnt, Element_EA):
  
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
      dwg.add(dwg.text(Element_EA[i+1].tag,insert=(530,Y1+70),font_size=30))
      dwg.add(dwg.text("NumCommande: "+Element_EA[i+1].attrib["NumCommande"],insert=(535,Y1+95),font_size=15))
      dwg.add(dwg.text("Date: "+Element_EA[i+1].attrib["date"],insert=(535,Y1+110),font_size=15))
      dwg.add(dwg.text("Quantite: "+Element_EA[i+1].attrib["quantite"],insert=(550,Y1+125),font_size=15))
      
      Y1+=250
      Y2=Y1
      i+=3
      
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
