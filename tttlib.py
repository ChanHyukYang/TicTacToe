import random
def genBoard():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]

def printBoard(T):
    n = 0
    for i in T:
        if type(i) == int:
            n = n + 1
        else:
            return False
    if len(T) < 9:
        return False
    elif len(T) > 9:
        return False
    for i in T:
        if i < 0:
            return False
        elif i > 2:
            return False
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = 0
    for i in T:
         if i == 0:
            x[n] = n
            n = n + 1
         elif i == 1:
            x[n] = 'X'
            n = n + 1
         elif i == 2:
            x[n] = 'O'
            n = n + 1
    print(" " + str(x[0]) + " | " + str(x[1]) + " | " + str(x[2]))
    print("---|---|---")
    print(" " + str(x[3]) + " | " + str(x[4]) + " | " + str(x[5]))
    print("---|---|---")
    print(" " + str(x[6]) + " | " + str(x[7]) + " | " + str(x[8]))
    return True
def analyzeBoard(T):
        n = 0
        for i in T:
                if type(i) == int:
                        n = n + 1
                else:
                        return -1
        if len(T) < 9:
                return -1
        elif len(T) > 9:
                return -1
        for i in T:
                if i < 0:
                        return -1
                elif i > 2:
                        return -1
        if (T[0] == 1 and T[3] == 1 and T[6] == 1 and T[1] == 2 and T[4] == 2 and T[7] == 2) or (T[1] == 1 and T[4] == 1 and T[7] == 1 and T[2] == 2 and T[5] == 2 and T[8] == 2) or  (T[2] == 1 and T[5] == 1 and T[8] == 1 and T[0] == 2 and T[3] == 2 and T[6] == 2) or (T[0] == 2 and T[3] == 2 and T[6] == 2 and T[1] == 1 and T[4] == 1 and T[7] == 1) or (T[1] == 2 and T[4] == 2 and T[7] == 2 and T[2] == 1 and T[5] == 1 and T[8] == 1) or (T[2] == 2 and T[5] == 2 and T[8] == 2 and T[0] == 1 and T[3] == 1 and T[6] == 1) or (T[0] == 1 and T[3] == 1 and T[6] == 1 and T[2] == 2 and T[5] == 2 and T[8] == 2) or (T[0] == 2 and T[3] == 2 and T[6] == 2 and T[2] == 1 and T[5] == 1 and T[8] == 1) or (T[0] == 1 and T[1] == 1 and T[2] == 1 and T[3] == 2 and T[4] == 2 and T[5] == 2) or (T[3] == 1 and T[4] == 1 and T[5] == 1 and T[6] == 2 and T[7] == 2 and T[8] == 2) or (T[6] == 1 and T[7] == 1 and T[8] == 1 and T[0] == 2 and T[1] == 2 and T[2] == 2) or (T[0] == 2 and T[1] == 2 and T[2] == 2 and T[3] == 1 and T[4] == 1 and T[5] == 1) or (T[3] == 2 and T[4] == 2 and T[5] == 2 and T[6] == 1 and T[7] == 1 and T[8] == 1) or (T[6] == 2 and T[7] == 2 and T[8] == 2 and T[0] == 1 and T[1] == 1 and T[2] == 1) or (T[0] == 1 and T[1] == 1 and T[2] == 1 and T[6] == 2 and T[7] == 2 and T[8] == 2) or (T[0] == 2 and T[1] == 2 and T[2] == 2 and T[6] == 1 and T[7] == 1 and T[8] == 1):
                return -1
        a = T[0] + T[1] + T[2] + T[3] + T[4] + T[5] + T[6] + T[7] + T[8]
        if (T[0] == 1 and T[3] == 1 and T[6] == 1) or (T[1] == 1 and T[4] == 1 and  T[7] == 1) or (T[2] == 1 and T[5] == 1 and T[8] == 1) or (T[0] == 1 and T[1]  == 1 and T[2] == 1) or (T[3] == 1 and T[4] == 1 and T[5] == 1) or (T[6] == 1 and T[7] == 1 and T[8] == 1) or (T[0] == 1 and T[4] == 1 and T[8] == 1) or (T[6] == 1 and T[4] == 1 and T[2] == 1):
                return 1
        elif (T[0] == 2 and T[3] == 2 and T[6] == 2) or (T[1] == 2 and T[4] == 2 and T[7] == 2) or (T[2] == 2 and T[5] == 2 and T[8] == 2) or (T[0] == 2 and T[1] == 2 and T[2] == 2) or (T[3] == 2 and T[4] == 2 and T[5] == 2) or (T[6] == 2 and T[7] == 2 and T[8] == 2) or (T[0] == 2 and T[4] == 2 and T[8] == 2) or (T[6] == 2 and T[4] == 2 and T[2] == 2):
                return 2
        elif a < 13:
                return 0
        elif a == 13 or a == 14:
                return 3
def genNonLoser(T,player):
   if type(T) != list:
      return -1
   if (player != 1) and (player != 2):
      return -1
   analyzeBoard(T)
   if (analyzeBoard(T) == 3) or (analyzeBoard(T) == -1):
      return -1
   if player == 1:
      opp = 2
   elif player == 2:
      opp = 1
   pos = 0
   for i in T:
      tempBoard = list(T)
      if i == 0:
         tempBoard[pos] = opp
         state = analyzeBoard(tempBoard)
         if state == opp:
            return pos
      pos+=1
   return -1
def genWinningMove(T,player):
   if type(T) != list:
      return -1
   if (player != 1) and (player != 2):
      return -1
   analyzeBoard(T)
   if (analyzeBoard(T) == 3) or (analyzeBoard(T) == -1):
      return -1
   if player == 1:
      opp = 2
   elif player == 2:
      opp = 1
   pos = 0
   for i in T:
      tempBoard = list(T)
      if i == 0:
         tempBoard[pos] = player
         state = analyzeBoard(tempBoard)
         if state == player:
            return pos
      pos+=1
   return -1
def genRandomMove(T, player):
   if type(T) != list:
      return -1
   if (player != 1) and (player != 2):
      return -1
   analyzeBoard(T)
   if (analyzeBoard(T) == 3) or (analyzeBoard(T) == -1):
      return -1
   if player == 1:
      opp = 2
   elif player == 2:
      opp = 1
   if 0 in T:
      while True:
         tempBoard = list(T)
         rand = random.randint(0,8)
         if tempBoard[rand] == 0:
            return rand
   else:
      return -1
def genOpenMove(T, player):
   if type(T) != list:
      return -1
   if (player != 1) and (player != 2):
      return -1
   analyzeBoard(T)
   if (analyzeBoard(T) == 3) or (analyzeBoard(T) == -1):
      return -1
   if player == 1:
      opp = 2
   elif player == 2:
      opp = 1
   pos = 0
   for i in T:
      if i == 0:
         return pos
      elif i == 1 or i == 2:
         pos = pos + 1
   return -1
