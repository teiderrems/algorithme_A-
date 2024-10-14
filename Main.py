# from Noeud import Noeud
from Solveur import Solveur

def main():

    grille=[
        [7,3,1],
        [4,0,2],
        [8,6,5]]

    # grille=[
    #     [2, 0 ,5] ,
    #     [1 ,6, 3], 
    #     [4, 7, 8]
    # ]
    
    grilleF=[
        [1,2,3],
        [4,5,6],
        [7,8,0]]

    solveur=Solveur(grilleF)

    solveur.astar(grille,h="h1")




if "__main__"=="__main__":
    main()