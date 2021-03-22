#awnser_box
awnser = ['rock' , 'paper' , 'scissors']

#func
def rps_game():
    print()
    print('This is rock_paper_scissors game...play and enjoy!')
    
    #ask_to_choose
    player_1 = input('p_1...Choose (rock , paper , scissors): ')
    player_2 = input('p_2...Choose (rock , paper , scissors): ')
    
    #choose winner
    if player_1 == 'rock' and player_2 == 'scissors':
        print('<player_1> is Winner!\n')
    if player_2 == 'rock' and player_1 == 'scissors':
        print('<player_2> is Winner!\n')
    if player_1 == 'paper' and player_2 == 'rock':
        print('<player_1> is Winner!\n')
    if player_2 == 'paper' and player_1 == 'rock':
        print('<player_2> is Winner!\n')
    if player_1 == 'scissors' and player_2 == 'paper':
        print('<player_1> is Winner!\n')
    if player_2 == 'scissors' and player_1 == 'paper':
        print('<player_2> is Winner!\n')
    if player_1 == 'rock' and player_2 == 'rock':
        print('Equal\n')
    if player_1 == 'paper' and player_2 == 'paper':
        print('Equal\n')
    if player_1 == 'scissors' and player_2 == 'scissors':
        print('Equal\n')

    if player_1 not in awnser or player_2 not in awnser:
        print('invaild choice!! try again')
        rps_game()

    play_again()

#func    
def play_again():
    
    #ask_to_play_again
    ask = input('Do you want to play again? if yes type <y> and no type <n> and enter... : ')
    
    #awnser
    if ask == 'y':
        rps_game()
    elif ask == 'n':
        print('Goodby my friend')

    else:
        print('This is wrong choice!!')
        play_again()
    
rps_game()

#end