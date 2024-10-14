from Noeud import Noeud

class Solveur:
    liste_noeuds_ouvertes:list[Noeud]=None
    liste_noeuds_fermé:list[Noeud]=None
    def __init__(self,grille):
        self.liste_noeuds_ouvertes=[]
        self.liste_noeuds_fermé=[]
        self.finalState=grille
    
    def astar(self,grille=None,h="h2"):

        self.liste_noeuds_ouvertes.append(Noeud(grille))
        k=0
        while(len(self.liste_noeuds_ouvertes)>0):
            noeud_courant:Noeud=self.liste_noeuds_ouvertes.pop(0)
            self.liste_noeuds_fermé.append(noeud_courant)
            successeurs=noeud_courant.successeurs()
            print("Listes ouverte")
            for v in self.liste_noeuds_ouvertes:
                print(v)
                print(f"f={v.cout(self.finalState,h)}->g={v.g}")

            print("Listes fermée")
            for v in self.liste_noeuds_fermé:
                print(v)
                print(f"f={v.cout(self.finalState,h)}->g={v.g}")
                
            if noeud_courant.estUnEtatFinal(Noeud(self.finalState)):
                return;
            else:
                for succ in successeurs:
                    if self.isInCloseList(succ)==False:
                        if self.isInOpenList(succ)==False:
                            self.liste_noeuds_ouvertes.append(succ)
                        else:
                            for i in range(len(self.liste_noeuds_ouvertes)):
                                if self.liste_noeuds_ouvertes[i].cout(self.finalState,h)>succ.cout(self.finalState,h):
                                    self.liste_noeuds_ouvertes[i]=succ

    
    def isInCloseList(self,node:Noeud):
        for n in self.liste_noeuds_fermé:
            if n==node:
                return True
        return False
    
    def isInOpenList(self,node:Noeud):
        for n in self.liste_noeuds_ouvertes:
            if n==node:
                return True
        return False
    
    def printSuccesseur(self,successeurs:list[Noeud]):
        for v in successeurs:
            print(v,end="\t")
