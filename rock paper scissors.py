import random, sys
win = 0
draw = 0
loss = 0
print('Win 5 times to leave!')
d = {1:'rock', 2:'paper', 3:'scissors'}
while True:
    print('Rock, Paper or Scissors')
    player = input().lower()
    computer = random.randint(1,3) # 1 = rock, 2 = paper, 3 = scissors
    if player not in ('rock', 'paper', 'scissors'):
        print('You have made a spelling mistake')
        continue
    computer = d[computer]
    print('Computer chose ' + computer)
    if player == computer:
        print('Draw!')
        draw += 1
    elif player == 'rock' and computer == 'scissors' or player == 'paper' and computer == 'rock' or player == 'scissors' and computer == 'paper':
        print('You win!')
        win += 1
    else:
        print('You lose!')
        loss += 1
    print('wins = ' + str(win),'draws = ' + str(draw),'losses = ' + str(loss), sep='\n')
    if win == 5:
       print('Well done!')
       break



