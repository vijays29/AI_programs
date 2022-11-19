from tkinter import Tk,Button,messagebox
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
        if pos: return self.state[pos[0]]   
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
    def ai_move(self,ply_depth=8):
        best_state = self.best_move(ply_depth)
        if best_state:
            self.__dict__ = best_state.__dict__       
    def player_move(self,i):
        if self.is_valid_move(i):
            self.state[i] = self.player = self.opponent
class Game():
    '''The class for the gui'''
    def __init__(self):
        self.app = Tk()
        self.app.title("Tic Tac Toe")
        self.app.resizable(width=False, height=False)
        self.board = GameState()
        self.size = 3
        self.buttons = [
            Button(self.app,text=x) 
            for x in self.board.state
        ]
        for i in range(9):
            x,y = i//self.size,i%self.size
            self.buttons[i].grid(row = x,column = y)
            self.buttons[i]["command"] = lambda x = i: self.move(x)
        reset = Button(self.app,text = "reset",command = self.reset)
        reset.grid(row =self.size+1,column=0,columnspan = 4)
        self.reset()
        self.update()
    
    def update(self):
        for i in range(0,9):
            self.buttons[i]["text"] = self.board.state[i]
            if self.board.state[i]!= N:
                self.buttons[i]["disabledforeground"] = "black"
                self.buttons[i]["state"]="disabled"
        win_pos = self.board.win_position()
        if win_pos:
            for i in range(0,9):
                self.buttons[i]["state"]="disabled"
            for i in win_pos:
                self.buttons[i]["disabledforeground"]="red"
            self.retry_popup(self.board.winner()+" Wins!\n")
            return
        if self.board.is_draw():
            self.retry_popup("Match Draw!\n")
            return
            
    def reset(self):
        self.board = GameState()
        for i in range(0,9):
            self.board.state[i] = N
            self.buttons[i]["state"]="normal"
        self.update()

    def move(self,i):
        self.board.player_move(i)
        self.update()
        
        self.app.config(cursor="watch")
        self.app.update()
        self.board.ai_move()
        self.app.config(cursor="")
        self.app.update()
        self.update()
        
    def retry_popup(self,message):
        msg = messagebox.askretrycancel(message = message+"Do you want to retry ?",icon = "question")
        if not msg:
            self.app.destroy()
        else:
            self.reset()    
        
    def mainloop(self):
        
        self.app.mainloop()
if __name__ == "__main__":
    Game().mainloop()