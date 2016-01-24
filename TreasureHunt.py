# stores each number in a list one line at a time
with open("initialMap.txt") as file:
    initialMap = [x.split() for x in file.readlines()]

# serves as boolean 2-d array to mark visited spots, set to 0 for false
visited = [[0 for x in range(11)] for x in range(11)]

"""Recursively backtracks till it gets all the correct moves and finds a corner of the board
   or finds that there is no path from the middle of the board that can reach a corner. """
def treasureHunt(row, col, pathSoFar):
    visited[row][col] = 1;
    if (((row == 10) and (col == 10)) or ((row == 0) and (col == 0)) or
      ((row == 0) and (col == 10)) or ((row == 10) and (col == 0))):
        return pathSoFar;

    steps = int(initialMap[row][col]);

    if (row - steps > -1) and (visited[(row - steps)][col] == 0):
        result = treasureHunt(row - steps, col, pathSoFar + " up");
        if result is not None:
            return result;
    if (col + steps < 11) and (visited[row][(col + steps)] == 0):
        result = treasureHunt(row, col + steps, pathSoFar + " right");
        if result is not None:
            return result;
    if (row + steps < 11) and (visited[(row + steps)][col] == 0):
        result = treasureHunt(row + steps, col, pathSoFar + " down");
        if result is not None:
            return result;
    if (col - steps > -1) and (visited[row][(col - steps)] == 0):
        result = treasureHunt(row, col - steps, pathSoFar + " left");
        if result is not None:
            return result;
    return None

print treasureHunt(5, 5, "")







