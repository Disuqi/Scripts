import discord

class tictactoe:
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    playerX = True
    won = False
    def display_board(self):
        board = self.board
        print(f'\n{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}\n')


    def play(self, position, player):
        if position < 10 and position > 0:
            if player == True and self.board[position-1] == '-':
                self.board[position-1] = 'X'
                self.playerX = False
            elif player == False and self.board[position-1] == '-':
                self.board[position-1] = 'O'
                self.playerX = True
            else:
                print('That position is already taken')
                self.playGame()
                return
            self.checkWin()
        else:
            print('The number you entered is too small or big it should be from 1 - 9\n')
            print('1|2|3\n4|5|6\n7|8|9\n\nTry again!')


    def playGame(self):
        while self.won == False:
            self.display_board()
            if self.playerX == True:
                print("It's playerX's turn")
            else:
                print("It's playerO's turn")
            try:
                position = int(input('Choose where you want to place the X(Enter a position from 1 - 9 ): '))
            except ValueError:
                print('You did not enter a number! Try again')
                self.playGame()
                return
            self.play(position, self.playerX)


    def checkWin(self):
        board = self.board
        counter = 9

        if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X' or board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X' or board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] =='X':
            print('PlayerX won!')
            self.someoneWon()
        elif board[0] == board[1] == board[2] == 'O' or board[3] == board[4] == board[5] == 'O' or board[6] == board[7] == board[8] == 'O' or board[0] == board[0] == board[3] == board[6] == 'O' or board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == board[8] == 'O' or board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] =='O':
            print('PlayerO won!')
            self.someoneWon()
        elif  self.won == False:   
            for sign in board:
                if sign != '-':
                    counter -= 1
                if counter == 0:
                    self.display_board()
                    print('Tie, noone won :( \nNoobs!')
                    self.won = True


    def someoneWon(self):
        self.won = True
        self.display_board()






def hello():
    return
game = tictactoe()
game.playGame()