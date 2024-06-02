import random

class Ship:
    def __init__(self, lenght):
        self.lenght=lenght
        self.coordinates=[]
        
class Board:
    def __init__(self, size):
        self.size=size
        self.grid=[[' ' for _ in range(size)] for _ in range(size)]
        self.ships=[]
    
    def place_ship(self, ship):
        placed=False
        while not placed:
            x=random.randint(0, self.size-1)
            y=random.randint(0, self.size-1)
            orientatin=random.choice(['горизонталь','вертикаль'])
            if self.check_placement(x,y, orientatin, ship.lenght):
                ship.coordinates=[(x+i, y) if orientatin=='горизонталь' else (x, y+i) for i in range(ship.lenght)]
                self.ships.append(ship)
                placed=True
                
                
    def check_placement(self, x, y, orientatin, lenght):
        if orientatin=='горизонталь' and x+lenght<=self.size:
            for i in range(lenght):
                if self.grid[x+i][y]!=' ':
                    return False
                return True
        elif orientatin=='вертикаль' and y+lenght<=self.size:
             for i in range(lenght):
                 if self.grid[x+i][y]!=' ':
                     return False
                 return True
        elif orientatin=='вертикаль' and y+lenght<=self.size:
            for i in range(lenght):
                if self.grid[x][y+i]!=' ':
                    return False
            return True
        return False
    
    def print_board(self):
        for row in self.grid:
            print(' '.join(row))
    def attack(self, x, y):
        if self.grid[x][y]==' ':
            self.grid[x][y]=='0'
            print('Мимо')
        else:
            for ship in self.ships:
                if (x,y) in ship.coordinates:
                    ship.coordinates.remove((x,y))
                    self.gridp[x][y]='X'
                    print('Попал')
                    if not ship.coordinates:
                        self.coordinates.remove(ship)
                        print('ты потопил корабль!')
                    return
        print('Ещё раз')
        
        
class Player:
    def __init__(self, board):
        self.board=board
        
    def make_move(self):
        try:
            x=int(input('Введите x: '))
            y=int(input('Ведите y: '))
            if 0<=self.board.size and 0<=self.board.size:
                self.board.attac(x, y)
            else:
                print('Неверные координаты, пробуй снова.')
        except ValueError:
            print('Неверный ввод, заного')

def main():
    board_size=5
    player_board=Board(board_size)
    computer_board=Board(board_size)
    
    player_ship=Ship(3)
    computer_ship=Ship(3)
    
    player_board.place_ship(player_ship)
    computer_board.place_ship(computer_ship)
    
    player=Player(player_board)
    
    while player_board.ships and computer_board.ships:
        print('доска для игрокa')
        player_board.print_board()
        player.make_move()
    print('Конец')

if __name__=="__main__":
    main()                        