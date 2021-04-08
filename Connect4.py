#Connect 4 The Game
from termcolor import colored, cprint

def board(place):
    for row in range(11):
        if row%2==0:
            Rrow=int(row/2)
            for col in range(13):
                if col%2==0:
                    Rcol=int(col/2)
                    if col != 12:
                        print(cplace[Rcol][Rrow],end="")
                    else:
                        print(cplace[Rcol][Rrow])
                else:
                    print("|",end="")
        else:
            print("----------------------------")


def result(res):
    if "XXXX" in res:
        print("Game over...\n Congratulations! Player 1 has won!...")
        return True
    elif "OOOO" in res:
        print("Game over...\n Congratulations! Player 2 has won!...")
        return True
    else:
        return False
   
   
def wincol():
    Cres=""
    for i in cplace:
        for j in i:
            Cres+=j.strip()
        if result(Cres)==True:
            return True
            break
        
def winrow():
    Rres=""
    for i in range(6):
        for j in cplace:
            Rres+=j[i].strip()
        if result(Rres)==True:
            return True
            break


def windia():
    dia=[[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)],
     [(1,0),(2,1),(3,2),(4,3),(5,4),(6,5)],
     [(2,0),(3,1),(4,2),(5,3),(6,4)],
     [(3,0),(4,1),(5,2),(6,3)],
     [(0,1),(1,2),(2,3),(3,4),(4,5)],
     [(0,2),(1,3),(2,4),(3,5)]]
    
    Dres=""
    
    for i in dia:
        for j in i:
            x=j[0]
            y=j[1]
            Dres+=cplace[x][y].strip()
        if result(Dres)==True:
            break

def winindia():
    diai=[[(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)],
     [(1,5),(2,4),(3,3),(4,2),(5,1),(6,0)],
     [(2,5),(3,4),(4,3),(5,2),(6,1)],
     [(3,5),(4,4),(5,3),(6,2)],
     [(0,4),(1,3),(2,2),(3,1),(4,0)],
     [(0,3),(1,2),(2,3),(3,0)]]
    
    Dires=""
    
    for i in diai:
        for j in i:
            x=j[0]
            y=j[1]
            Dires+=cplace[x][y].strip()
        if result(Dires)==True:
            break

plyr=1
cplace=[["   ","   ","   ","   ","   ","   "],
        ["   ","   ","   ","   ","   ","   "],
        ["   ","   ","   ","   ","   ","   "],
        ["   ","   ","   ","   ","   ","   "],
        ["   ","   ","   ","   ","   ","   "],
        ["   ","   ","   ","   ","   ","   "],
        ["   ","   ","   ","   ","   ","   "]]
cond=True
count=0
while(cond==True):
    if plyr==1:
        print("Player 1's turn")
        colmn=int(input("set the column you want to place: "))
        for i in range(5,-1,-1):
            li=cplace[colmn][i]
            if li=="   ":
                cplace[colmn][i]=colored(" X ",'blue',attrs=['reverse'])
                plyr=2
                count+=1
                break
    else:
        print("Player 2's turn")
        colmn=int(input("set the column you want to place: "))
        for i in range(5,-1,-1):
            li=cplace[colmn][i]
            if li=="   ":
                cplace[colmn][i]=colored(" O ",'red',attrs=['reverse'])
                plyr=1
                count+=1
                break
    
    board(cplace)
    
    if count==42:
        print("Game over..\n Draw")
        cond=False
    

    
    if wincol()==True:
        cond=False
    elif winrow()==True:       
        cond=False
    elif windia()==True:        
        cond=False
    elif winindia()==True:        
        cond=False
    





        






                



