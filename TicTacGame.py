class TicTacGame():
    def __init__(self):
        self.board = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
        self.players = ('a', 'b')
        
    def display(self):
        for row in self.board:
            print(row[0] +" | "+ row[1] +" | "+ row[2])
            if self.board.index(row) < 2:
                print("-- -- --")
    
    def player_name(self, player1):
        if player1:
            return self.players[0]
        else:
            return self.players[1]
        
    def win_check(self, player):
        result = self.board[0][0] == self.board[1][1] == self.board[2][2] == player or self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        
        if result:
            return True
        
        for n in range(0, 3):
            result = self.board[n][0] == self.board[n][1] == self.board[n][2] == player or self.board[0][n] == self.board[1][n] == self.board[2][n] == player
            if result:
                return True
        
        return False
        
                
    def start_game(self):
        count = 0
        p1 = True
        
        while True:
            if count >= 9:
                break
            player = self.player_name(p1)
            position = int(input("Player "+ player +"Please enter desired position between 0 - 8  "))
            
            if position < 0 or position > 8:
                print(f"Invalid position {position}")
                continue
            else:
                col = int(position%3)
                row = int(position/3)
                
                if self.board[row][col] != 'x':
                    print(f"Invalid input. Position {position} already filled")
                    continue
                else:
                    self.board[row][col] = player
                    p1 = not p1
                    count = count + 1
                    self.display()
                    if self.win_check(player):
                       break
                    
        print(f"Game completed ... winner is {player}")

            
            
