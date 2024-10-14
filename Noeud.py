
from copy import deepcopy
class Noeud:

    def __init__(self,grille,g=0,pere=None):
        self.grille=grille # Grille du noeud courant
        self.pere=pere # Parent du noeud courant
        self.g=g # Nombre de déplacement


    def getNewNoeud(self,i,j,index,g=0):
        pere=deepcopy(self.grille)
        tempG=deepcopy(self.grille)
        temp=tempG[i][j]
        tempG[i][j]=0
        tempG[index[0]][index[1]]=temp
        succ=Noeud(tempG,g,pere)
        return succ

    def __str__(self):

        string="[\n"
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                
                string+=f"\t{self.grille[i][j]}"

            string+="\n"

        string+="]"
        return string
    
    def __eq__(self, value)->bool:
        equal=False
        for i in range(len(value.grille)):
            for j in range(len(value.grille[0])):
                if value.grille[i][j]!=self.grille[i][j]:
                    return False
                else:
                    equal=True
        return equal
    
    

    def _estBienPlacé(self,i,j,grilleF)->bool:
        if self.grille[i][j]==grilleF[i][j]:
            return True
        return False
    
    
    def h2_helper(self,v,i,j,grilleF):
        for z in range(len(grilleF)):
            for t in range(len(grilleF[0])):
                if grilleF[z][t]==v:
                    return abs(i-z) + abs(j-t)
    
    def h2(self,grilleF):
        h=0
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                if self.grille[i][j]!=0:
                    v=self.h2_helper(self.grille[i][j],i,j,grilleF)
                    h+=v
        return h
        


    def h1(self,grilleF):
        v=0
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                if self.grille[i][j]!=0:
                    if(self._estBienPlacé(i,j,grilleF)==False):
                        v+=1
        return v
    
    def cout(self,grilleF,h="h1"):
        if h=="h1":
            return self.g+self.h1(grilleF)
        return self.g + self.h2(grilleF)
    
    def estUnEtatFinal(self,node)->bool:
        return self==node
    
    def getIndex(self)->tuple:
        
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                if self.grille[i][j]==0:
                    return (i,j)
    
    def successeurs(self)->list:
        index=self.getIndex()
        successeur=[]
        
        deplacement=self.getDéplacement(index)

        for v in deplacement:
            
            if v=="bas":
                successeur.append(self.getNewNoeud(index[0]+1,index[1],index,self.g+1))
            elif v=="haut":
                successeur.append(self.getNewNoeud(index[0]-1,index[1],index,self.g+1))
            elif v=="gauche":
                successeur.append(self.getNewNoeud(index[0],index[1]-1,index,self.g+1))
            else:
                successeur.append(self.getNewNoeud(index[0],index[1]+1,index,self.g+1))
        return successeur
        

    def getDéplacement(self,index):
        
        if index[1]==0:
            if index[0]==0:
                return ["droit","bas"]
            elif index[0]==len(self.grille)-1:
                return ["droit","haut"]
            else:
                return ["droit","haut","bas"]
        elif index[1]==len(self.grille[0])-1:
            if index[0]==0:
                return ["gauche","bas"]
            elif index[0]==len(self.grille)-1:
                return ["gauche","haut"]
            else:
                return ["gauche","haut","bas"]
            
        elif index[1]>=1 and index[1]<len(self.grille[0])-1:
            if index[0]==0:
                return ["gauche","droite","bas"]
            elif index[0]==len(self.grille)-1:
                return ["gauche","droite","haut"]
            else:
                return ["gauche","droite","haut","bas"]
            
            
    


