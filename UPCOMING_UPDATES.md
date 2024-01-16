1. top left corner would write "start"
2. bottom right corner would write "finish"
3. it would create a maze of a size 4x4 (num_rows = 4 and num_cols = 4)
4. When the maze is created, user would start on "start" and use keyboard to navigate inside the maze (with W, A, S, D keys as up, left, down, right)
5. if a player gets to a finish line, it would say "level (number of level) complete"
6. it would ask if player want to continue. (using Y as yes and N as no)
7. if player selects yes, it would make a new maze, but the grid would increase by one. Example if player finished first level of 4x4 grid, it would increase to 5x5 so 5rows and 5cols.
8. when all of this would work, we would add a timer. It would give player for example 5 seconds for each move. Whenever they choose a new direction with W,A,S,D it would count from 5seconds again etc. If a player managed to reach the end without failing the timer, he would win that level and continue to next one. But if a player failed to move in time, it would show him how to solve said level and player would see "you lose" with the correct path made with maze.solve()
