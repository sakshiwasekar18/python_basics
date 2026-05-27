def minion_game(string):
   player1=0
   player2=0
   s=input()
   if s in string:
        first=s[0].lower()
        
        if first in "aeio":
            player1+=1
   print(player1)
minion_game("Banana")