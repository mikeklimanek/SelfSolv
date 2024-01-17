# SelfSolv

# WORK IN PROGRESS
UPCOMING CHANGES using previous Self Solving Maze, the remake will rework a maze 
into a game with levels of difficulty

1. top left corner would write "start" 
2. bottom right corner would write "finish"
3. it would create a maze of a size 4x4 (num_rows = 4 and num_cols = 4)
4. When the maze is created, user would start on "start" and use keyboard to navigate inside the maze (with W, A, S, D keys as up, left, down, right)
5. if a player gets to a finish line, it would say "level (number of level) complete"
6. it would ask if player want to continue. (using Y as yes and N as no)
7. if player selects yes, it would make a new maze, but the grid would increase by one. Example if player finished first level of 4x4 grid, it would increase to 5x5 so 5rows and 5cols.



![SelvSolv](https://github.com/mikeklimanek/SelfSolv/assets/46258877/5e70ff96-5dfc-4cbd-81f4-35fcefd7a6d7)

# Previous release (main branch)
1) create a window
2) finishing window actions
3) implement main()
4) splitting into coresponding files
5) creating point and lines
6) compiled all back to main to find problems in code
7) created a test.py for easier testing
8) spreading back to each file
9) redefinided Line and Maze
10) centered the whole maze
11) increased number of cols and rows
12) added start and finish points
13) debugged and corrected code for test.py to work
14) found and solved a problem with start and finish points
15) breaking walls of cells to create a maze
16) self reset for cells visited
17) canvas line that connects a path used to solve the maze
18) updates to paths of solving line, correctly comes back from dead ends until it finds finish line
19) creating maze is now much faster
20) SelfSolving line goes a little slower for showing purposes