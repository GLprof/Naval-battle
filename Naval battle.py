player1_board=[[' ' for _ in range(10)] for _ in range(10)]
player2_board=[[' ' for _ in range(10)] for _ in range(10)]

class ShipGame:
    def __init__(self):
        self.board=[[' ' for _ in range(10)] for _ in range(10)]
        self.ships=[(4), (3,3), (2,2,2), (1,1,1,1)]
        self.player=0
    
    def place_ship(self, row, col, lenth, direction):
        if direction=='V':
            for i in range(lenth):
                self.board[row+i][col]=str(lenth)
        else:
            for i in range(lenth):
                self.board[row][col+i]=str(lenth)
    def print_board(self):
        for row in self.board:
            print(' '. join(row))
            
    def attack(self, row, col):
        if self.board[row][col]==' ':
            print('Промазал!')
        else:
            lenth=int(self.board[row][col])
            n=sum(1 for row in self.board for cell in row if cell==str(lenth))
            if n==1:
                print(f'Потопил {lenth}')
            else:
                print(f'Просто попал')
            self.board[row][col]
    
    def play(self):
        while any(str(i) in row for row in self.board for i in range(1,5)):
            print(f'ход игрока {self.player+1}')
            self.print_board()
            row=int(input('Дай номер строки: '))
            col=int(input('Дай номер столбца: '))
            self.attack(row, col)
            self.player=(self.player+1)%2
        print(f'Игрок {self.player+1} Победа!')

if __name__=='__main__':
    game=ShipGame()
    game.place_ship(1, 1, 4, 'V')
    game.place_ship(2, 3, 3, 'h')
    game.place_ship(4, 4, 2, 'v')
    game.place_ship(7, 6, 1, 'h')
    game.play()
    
                
            