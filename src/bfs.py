import queue

class BFS:
	def __init__(self, map, start, dest, cols, rows, draw_func):
		self.map = map
		self.start = start
		self.dest = dest
		self.cols = cols
		self.rows = rows
		self.draw_func = draw_func

	# Run BFS
	def run(self):
		# Start a queue and insert the starting cell to it
		q = queue.Queue()
		q.put((self.start[0], self.start[1]))
		visited = [] # Keeps track of cells we visited
		pi = {} # Keeps track of the cell that led to each cell. i.e. {(5,4): (5,3)} means that we got to (5,4) from (5,3)
		pi[(self.start[0], self.start[1])] = None
		finished = False

		while not q.empty():
			row, col = q.get()
			visited.append((row, col))

			# If this is not the starting or end point, set it as 'V' (visited)
			if self.map[row][col] != 'S' and self.map[row][col] != 'D':
				self.map[row][col] = 'V'

			# Call the draw function to draw by the updates map
			self.draw_func()

			# If we got to the destination point, set finished and break
			if row == self.dest[0] and col == self.dest[1]:
				finished = True
				break

			# Add right adjacent cell
			if col+1 < self.cols and (row, col+1) not in visited:
				if self.map[row][col+1] != 'X':
					q.put((row, col+1))
					visited.append((row, col+1))
					pi[(row, col+1)] = (row, col)
			# Add left adjacent cell					
			if col-1 >= 0 and (row, col-1) not in visited:
				if self.map[row][col-1] != 'X':
					q.put((row, col-1))
					visited.append((row, col-1))
					pi[(row, col-1)] = (row, col)
			# Add bottom adjacent cell
			if row+1 < self.rows and (row+1, col) not in visited:
				if self.map[row+1][col] != 'X':
					q.put((row+1, col))
					visited.append((row+1, col))
					pi[(row+1, col)] = (row, col)
			# Add top adjacent cell
			if row-1 >= 0 and (row-1, col) not in visited:
				if self.map[row-1][col] != 'X':
					q.put((row-1, col))
					visited.append((row-1, col))
					pi[(row-1, col)] = (row, col)

		# Check if we got to the destination point
		if finished:
			self.get_pi(pi, (self.dest[0], self.dest[1]))
		else:
			print("Could not get to destination!")

	# Get the pi (cell that led to this cell) of each cell, recursively
	def get_pi(self, pi, cell):
		# Return if we reached the starting cell
		if pi[cell] == None:
			return

		# If this cell is not the starting or end point, mark is as 'P' (path)
		if self.map[cell[0]][cell[1]] != 'S' and self.map[cell[0]][cell[1]] != 'D':
			self.map[cell[0]][cell[1]] = 'P'

		self.get_pi(pi, pi[cell])