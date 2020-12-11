#minion_game
def minion_game(s):
    kk = ss = 0
    for i in range(len(s)):
        if s[i] in ['A','E', 'I', 'O', 'U']:
            kk+= len(s)-i
        else:
            ss+=len(s)-i
    if ss > kk: print("Stuart", ss)
    elif ss < kk: print("Kevin", kk)
    else: print("Draw")
        
        

if _name_ == '_main_':
    s = input()
    minion_game(s)
