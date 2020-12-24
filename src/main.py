from window import Window

width = height = 800 # Width and height of the window
rows = cols = 25 # Number of rows and columns in the map
start = (2, 1) # Starting point
dest = (20, 22) # Destination point

map = [['0' for i in range(cols)] for j in range(rows)] # Fill a rows x cols matrix with zeros
map[start[0]][start[1]] = 'S' # Set starting point to 'S'
map[dest[0]][dest[1]] = 'D' # Set destination point to 'D'

window = Window(width, height, cols, rows, map, start, dest)