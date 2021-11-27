# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:21:30 2020

@author: aurel
"""

import numpy as np
import random as rd
import copy

class grille:
    
    def __init__(self):
        self.initialisation_grille()

    def initialisation_grille(self):
        self.s = [['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.tourdujoueur = 'X'
        return self.s
            
    
        
    def Action(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if(self.s[i][j] == '.'):
                    actions.append((i,j))
        return actions
    
                
    def Terminal_Test(self):
       #colonne
        for i in range(3):
            if(self.s[0][i] != '.' and self.s[0][i] == self.s[1][i] and self.s[1][i] == self.s[2][i]):
                return self.s[0][i]
           
         #ligne 
        for i in range(3):
            if(self.s[i]==['X','X','X']):
                return 'X'
            elif(self.s[i]==['O','O','O']):
                return 'O'
            
         #diag 1   
        if(self.s[0][0] != '.' and self.s[0][0] == self.s[1][1] and self.s[1][1] == self.s[2][2]):
            return self.s[0][0]
        
        #diag 2
        if(self.s[0][2] != '.' and self.s[0][2] == self.s[1][1] and self.s[1][1] == self.s[2][0]):
            return self.s[0][2]
        
        #si case vide on continue
        for i in range(3):
            for j in range(3):
                if self.s[i][j] == '.':
                    return None
        #partie finie = match nul
        for i in range(3):
            for j in range(3):
                if self.s[i][j] != '.':
                    return '.'
    
    
    def Utility(self,resultat): #vient de terminal test
    
        if resultat == 'X':
            return 1 #victoire
        elif resultat == 'O':
            return -1 #défaite
        elif resultat == '.':
            return 0 #match nul
        elif resultat == None:
            return None
        
        
    def result(self,action,s, joueur): 
        nouvellegrille = copy.deepcopy(s)
        nouvellegrille[action[0]][action[1]] = joueur
        return nouvellegrille
        
        
        
        
    def Max(self, alpha, beta): #resultat d'utility
        valeur = self.Terminal_Test()
     
        maxi = -2
        px = None
        py = None
        
        if valeur == 'X':
            return (-1, 0, 0)
        elif valeur == 'O':
            return (1, 0, 0)
        elif valeur == '.':
            return (0, 0, 0)
        
        for i in range(3):
            for j in range(3):
                if self.s[i][j] == '.':
                    self.s[i][j] = '0'
                    (m,min_i,min_j) = self.Min(alpha, beta)
                    if m > maxi:
                        maxi = m
                        px = i
                        py = j
                        
                    self.s[i][j] = '.'
                    
                    if maxi >= beta:
                        return (maxi, px, py)
                    
                    if maxi > alpha:
                        alpha = maxi
                        
        return (maxi,px,py)
        
        
            
    def Min(self, alpha, beta):
       valeur = self.Terminal_Test()
       
       mini = 2
       qx = None
       qy = None
       
       if valeur == 'X':
            return (-1, 0, 0)
       elif valeur == 'O':
            return (1, 0, 0)  
       elif valeur == '.':
            return (0, 0, 0)
        
       for i in range(3):
          for j in range(3):
              if self.s[i][j] == '.':
                  self.s[i][j] = 'X'
                  (m,max_i,max_j) = self.Max(alpha, beta)
                  if m < mini:
                      mini = m
                      qx = i
                      qy = j
                  self.s[i][j] = '.'
                  
                  if mini <= alpha:
                      return(mini, qx, qy)
                      
                  if mini < beta:
                      beta = mini
                      
       return (mini,qx,qy)
       
        
       
    def affichergrille(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.s[i][j]), end=" ")
            print()
        print()
        
        
    
    def alphabeta(self):
        while True:
            
            self.affichergrille()
            resultat = self.Terminal_Test()
            valeur = self.Utility(resultat)
            
            if valeur != None:   
                if valeur == 1:
                    print('Vainqueur X')
                elif valeur == -1:
                    print('Vainqueur O')
                elif valeur == 0:
                    print("Egalité")
                    
                self.initialisation_grille()
                return
            
            if self.tourdujoueur == 'X':
                while True:
                    
                    (m,qx, qy) = self.Min(-2,2)
                    print(self.Min(-2,2))
                    print('Mouvement recommandé: X = {}, Y = {}'.format(qx,qy))
                    px = int(input('Entrez X: '))
                    py = int(input('Entrez Y: '))

                    qx = px
                    qy = py
                    actions = self.Action()
                    print(actions)
                    if actions.__contains__((px,py)) == True:
                         
                         self.s[px][py] = 'X'
                         self.tourdujoueur = 'O'
                         break
                    else:
                         print('Mouvement impossible')
            else:
                (m, px, py) = self.Max(-2,2)
                self.s[px][py] = 'O'
                self.tourdujoueur = 'X'
        
            

def main():
    g = grille()
    g.alphabeta()

if __name__ == "__main__":
    main()