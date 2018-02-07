# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:53:51 2018

@author: brad_
"""

class BoardGame:
    def __init__(self):
        self.board_size = 19 # played on 19x19 board
        self.connection_requirement = 5 # need 5 in a row to win
        self.number_players = 2 # just two player support for now
        
        self.board = [[0] * self.board_size for i in range(self.board_size)]
        self.next_player = 1
        self.history = []
        self.turn_number = 0
        self.complete = False
        
    def is_move_on_board(self, row, col):
        if (row >= 0 and row < self.board_size and 
            col >= 0 and col < self.board_size): 
             return True
        return False   

    def is_move_valid(self, row, col):
        if (self.is_move_on_board(row, col) and 
                self.board[row][col] == 0 and
                self.complete == False): 
            return True
        return False
    
    def is_move_victorious(self, row, col, player):
        # 4 possible directions to make connection
        directions = [ 
                [1,0],
                [0,1],
                [1,1],
                [1,-1]]
        for direction in directions:
            count = 1
            # move both ways in along direction from position
            for sign in [-1,1]: 
                # max to look at to form connection is connection_requirement - 1
                for i in range(1, self.connection_requirement): 
                    r = row + sign * i * direction[0]
                    c = col + sign * i * direction[1]
                    if self.is_move_on_board(r, c) and self.board[r][c] == player:
                        count += 1
                    else:
                        break
            if count >= self.connection_requirement:
                return True
        return False
    
    def place_move(self, row, col):
        if self.is_move_valid(row, col):
            self.turn_number += 1
            self.board[row][col] = self.next_player
            if self.is_move_victorious(row, col, self.next_player):
                self.complete = True
            self.history.append((self.turn_number, self.next_player, row, col, self.complete))
            self.next_player = 1 if self.next_player == self.number_players else self.next_player + 1 
            return True, self.next_player, self.turn_number, self.complete
        else:
            return False, self.next_player, self.turn_number, self.complete
    
    def reset_board(self):
        self.board = [[0] * self.board_size for i in range(self.board_size)]
        self.next_player = 1
        self.history = []
        self.turn_number = 0
        self.complete = False
    
    def undo_move(self):
        pass