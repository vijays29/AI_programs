from copy import deepcopy

X,O,N = "X","O"," "

class GameState:
    def __init__(self,state=None,current_player=O):
        self.state = state or [N for _ in range(9)] 
        self.player = current_player
    
    @property
    def opponent(self):
        return X if self.player == O else O
        
    def next_states(self):
        for i in range(9):
            if self.state[i] == N:
                next_state = deepcopy(self)
                next_state.state[i] = next_state.player = self.opponent
                yield next_state
        return
    
    def win_position(self):
        state = self.state
        win_pos = [
            (0,1,2),(3,4,5),(6,7,8),(0,3,6),
            (1,4,7),(2,5,8),(0,4,8),(2,4,6)
        ]
        for pos in win_pos:
            if (state[pos[0]] == state[pos[1]] == state[pos[2]] != N):
                return pos
    
    def winner(self):
        pos = self.win_position()
        if pos: 
            return self.state[pos[0]]
    
    def is_filled(self):
        return N not in self.state
    
    def is_final(self):
        return True if self.winner() or self.is_filled() else False

    def has_won(self,player):
        return self.winner() == player

    def is_draw(self):
        return not self.winner() and self.is_final()

    def has_lost(self,player):
        winner = self.winner()
        return winner and winner != player

    def score(self,player):
        return (
            10 if self.has_won(player) else
            -10 if self.has_lost(player) else
            0
        )
    
    def is_valid_move(self,move):
        return self.state[move]==N
    
    def best_move(self,ply_depth):
        (best_state,_) = self.find_best_move(ply_depth)
        return best_state
        
    def find_best_move(self,depth):
        if depth == 0 or self.is_final():
            return (None, self.score(self.player))
        best_state,best_score = (None, None)
        for next_state in self.next_states():
            (_,score) =  next_state.find_best_move(depth-1)
            if best_score == None or (score >best_score):
                best_state,best_score = (next_state,score)
        return (best_state,best_score/-2)

    def __str__(self):
        return  '''\
Player: {} Opponent: {}
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------
'''.format(self.player,self.opponent,*self.state)
    
    def ai_move(self,ply_depth=8):
        best_state = self.best_move(ply_depth)
        if best_state:
            self.__dict__ = best_state.__dict__
        
    def player_move(self,i):
        if self.is_valid_move(i):
            self.state[i] = self.player = self.opponent
if __name__ == "__main__":
    g = GameState()
    print(g) 
    while True:
        pos = int(input("Enter a position to play [0-8]:"))
        while not g.is_valid_move(pos):
            print("\nCell already filled!\n")
            pos = int(input("Please, Enter another position to play [0-8]:"))
        g.player_move(pos)
        print(g)
        if g.is_final(): break
        print("The AI plays:")
        g.ai_move()
        print(g)
        if g.is_final(): break
    winner = g.winner()
    print(
        "Player Wins!"if winner == X else
        "AI Wins!" if winner == O else
        "Match Draw!"
    ) 