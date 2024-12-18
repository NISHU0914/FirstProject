import pygame
from color import colors
#this function is created by Nishu
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors=colors.get_cell_colors()#this function is created by Amisha


    def is_inside(self, row, column):
        if row>=0 and row < self.num_rows and column>=0 and column < self.num_cols:
            return True
        return False
    def is_empty(self, row, column): #this function is created by nishu
        if self.grid[row][column] == 0:
            return True
        return False
    def is_row_full(self, row): #this function is created by nishu
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    def clear_rows(self,row): #this function is created by nishu
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows): #this function is created by nishu
        # Check if the target row is within bounds
        if row + num_rows < self.num_rows:
            # Move the row down by copying its contents
            for column in range(self.num_cols):
                self.grid[row + num_rows][column] = self.grid[row][column]
            # Clear the original row
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    def clear_full_rows(self):#this function is created by nishu
        completed=0
        for row in range(self.num_rows-1,0,-1):
            if self.is_row_full(row):
                self.clear_rows(row)
                completed+=1
            elif completed>0:
                self.move_row_down(row, completed)
        return completed
    def reset(self): #this function is created by nishu
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    def draw(self,screen): #this function is created by nishu
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value=self.grid[row][col]
                cell_rect=pygame.Rect(col*self.cell_size+10,row*self.cell_size+10,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect)