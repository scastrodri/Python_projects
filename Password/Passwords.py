# Make an 8 letter password by combining characters from the three strings
import random

letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

passw = ''.join(random.sample(letters+caps+numbers,8))
print(passw)

# Make a four word password by combining words from the list of nouns, verbs and adjs
nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 
        'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 
        'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 
        'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 
        'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 
        'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 
        'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 
        'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 
        'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 
        'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 
        'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 
        'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 
        'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed',
        'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest',
        'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste',
        'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 
        'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 
        'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 
        'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect',
        'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 
        'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']

all_wrds = nouns+verbs+adjs
passw = ''.join(random.sample(all_wrds,4))
print(passw)

# Have at least one capital letter and a number in your password.
passw = ''
replaces = {'a':'4','e':'3','i':'1','o':'0','u':'2'}
wrds = random.sample(all_wrds,4)
place1 = random.randint(0,len(wrds)-1)
wrds[place1] = wrds[place1].capitalize()
place2 = random.randint(0,len(wrds)-1)
vowel_num = ('"','"')
done1 = True
while done1:
    if  vowel_num[0] in wrds[place2]:
        wrds[place2] = wrds[place2].replace(vowel_num[0],vowel_num[1])
        done1 = False
    vowel_num = random.choice(list(replaces.items()))

passw = ''.join(wrds)
print(passw)


# How many guesses would it take to guess a 4 letters password?
my_password = "abzd"
guess_num = 0
done2 = False
while not done2:
    guessed_pw = ''.join(random.sample(letters, 4))
    guess_num += 1
    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done2 = True