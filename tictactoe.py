from tttlib import *
T = genBoard()
while True:
   printBoard(T)
   moveX = input("X Move?")
   if int(moveX) > 9 or int(moveX) < 0:
      print("Could you not")
      break
   T[int(moveX)] = 1
   state = analyzeBoard(T)
   if state == 1:
      print("X Wins!")
      break
   elif state == 3:
      print("It's a Draw!")
      break
   printBoard(T)
   print("Computer Move")
   while True:
      if genWinningMove(T,2) !=-1:
         T[genWinningMove(T,2)] = 2
         break
      else:
         if genNonLoser(T,2) !=-1:
            T[genNonLoser(T,2)] = 2
            break
         else:
            if genRandomMove(T,2) !=-1:
               T[genRandomMove(T,2)] = 2
               break
            else:
               if genOpenMove(T,2) != -1:
                  T[genOpenMove(T,2)] = 2
                  break
   state = analyzeBoard(T)
   if state == 2:
      print("O Wins!")
      break
   elif state == 3:
      print("It's a Draw!")
      break
