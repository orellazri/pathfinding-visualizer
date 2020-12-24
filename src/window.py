import pygame
from bfs import BFS

class Window:
	def __init__(self, width, height, cols, rows, map, start, dest):
		pygame.init()
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Pathfinding Visualizer (ENTER = Start, SPACE = Reset after run)")
		# Fill the screen with black so the cells will have an outline
		self.screen.fill((0, 0, 0)) 

		self.clock = pygame.time.Clock()
		self.running = True
		self.ran_algo = False # Whether we ran any pathfinding algorithm yet
		self.width = width
		self.height = height
		self.cols = cols
		self.rows = rows
		self.map = map
		self.original_map = [[self.map[i][j] for i in range(self.cols)] for j in range(self.rows)] # Keep a copy of the map for resetting purposes
		self.start = start
		self.dest = dest

		# Calculate cell size by the given width/height and rows/columns
		self.cell_width = self.width // self.cols
		self.cell_height = self.height // self.rows

		self.bfs = BFS(self.map, self.start, self.dest, self.cols, self.rows, self.draw_cells)

		# Call main loop
		self.loop()

	# Main loop
	def loop(self):
		while self.running:
			self.clock.tick(60)

			for event in pygame.event.get():
				self.handle_events(event)

			self.draw_cells()
			
			pygame.display.update() 

		# If we got here, we are out of the main loop
		pygame.quit()

	# Handle pygame events
	def handle_events(self, event):
		if event.type == pygame.QUIT:
			# Quit
			self.running = False

		# Key down events
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				# Quit
				self.running = False
			elif event.key == pygame.K_SPACE and self.ran_algo:
				# Reset map
				self.map = [[self.original_map[i][j] for i in range(self.cols)] for j in range(self.rows)]
				self.bfs = BFS(self.map, self.start, self.dest, self.cols, self.rows, self.draw_cells)
				self.ran_algo = False
			elif event.key == pygame.K_RETURN and not self.ran_algo:
				# Run algorithm
				self.bfs.run()
				self.ran_algo = True

		# Hold left mouse button to draw obstacles
		if pygame.mouse.get_pressed()[0]:
			x, y = pygame.mouse.get_pos()
			x = x // self.cell_width
			y = y // self.cell_height

			if self.map[y][x] == '0':
				self.map[y][x] = 'X'

		# Hold right mouse button to remove obstacles
		if pygame.mouse.get_pressed()[2]:
			x, y = pygame.mouse.get_pos()
			x = x // self.cell_width
			y = y // self.cell_height

			if self.map[y][x] == 'X':
				self.map[y][x] = '0'

	# Draw the cells of the map
	def draw_cells(self):
		"""
			0 = Empty
			S = Start
			D = Destination
			V = Visited
			P = Path (Result)
			X = Obstacle
		"""
		for i in range(self.rows):
			for j in range(self.cols):
				if self.map[i][j] == '0':
					color = (255, 255, 255)
				if self.map[i][j] == 'S':
					color = (0, 255, 0)
				if self.map[i][j] == 'D':
					color = (0, 0, 255)
				if self.map[i][j] == 'V':
					color = (60, 60, 60)
				if self.map[i][j] == 'P':
					color = (128, 20, 128)
				if self.map[i][j] == 'X':
					color = (10, 10, 10)

				pygame.draw.rect(self.screen, color, pygame.Rect(j * self.cell_width, i * self.cell_height, self.cell_width - 2, self.cell_height - 2))

		pygame.display.update() 