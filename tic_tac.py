import imp
from tkinter import Tk,Button,messagebox
from copy import deepcopy

X,O,N='X',"O"," "
class GameState:
    def __init__(self,state=None,current_player=0):
        self.state=state or [N for _ in range(9)]
        self.player=current_player
@property
def opponent(self):
    return x if self.player == 0 else 0
def next_states(self):
    for i in range(9):
        if self.state[i]==N:
            next_state=deepcopy(self)
            next_state.state[i]=next_state.player=self.opponent
            yield next_state
       return            
def win_position(self):
    state=self.state
    win_pos=[
        (0,1,2),(3,4,5),(6,7,8),(0,3,6),
        (1,4,7),(2,5,8),(0,4,8),(2,4,6)
    ]
    for pos in win_pos:
        if(state[pos[0]]==state[pos[1]]==state[pos[2]]!=N):
           return pos
def winner(self):
    pos=self.win_position()
    if pos:return self.state[pos[0]]
def is_filled(self):
    return N not in self.state
def is_final(self):
     return True if self.winner    
