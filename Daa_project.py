import random
import timeit

# prints the matrix
def d(mat):
	print()
	for item in mat:
		print(*item)
	print()

# appending values to sample path
def getPath(i, j):

	if i==j==0:
		return

	x, y = visited[i][j][0]
	sample_paths.append([i, j])
	getPath(x, y)


rows = int(input("\nEnter number of rows: "))
columns = int(input("Enter number of columns: "))

# generate random matrix of 1 and 0
mat = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]

# the a[0][0] element will be 1
mat[0][0] = 1

# print the matrix
d(mat)

# array to store the last cell visited
visited = [[[] for _ in range(columns)] for _ in range(rows)]

# queue for backtracking
q = [[0, 0]]

# initial there are 0 paths
paths = 0

# start the timer
start = timeit.default_timer()

while(len(q)>0):
	pt = q.pop(0)
	x, y = pt
	
	# the top left corner 
	if (pt == [0, 0]):
		if (mat[x][y+1] != 0):
			q.append([x, y+1])
			visited[x][y+1].append([0, 0])
		
		if (mat[x+1][y+1] != 0):
			q.append([x+1, y+1])
			visited[x+1][y+1].append([0, 0])

		if (mat[x+1][y] != 0):
			q.append([x+1, y])
			visited[x+1][y].append([0, 0])

	# last column
	elif (y == columns-1):
		if (mat[x][y] == 1):
			paths+=1

	# leftmost column excluding 1st and last row
	elif (x>0 and x<rows-1 and y == 0):
		for i in range(x-1, x+2):
			for j in range(y, y+2):
				if ((i!=x or j!=y) and mat[i][j]!=0 and ([i, j] not in visited[x][y])):
					q.append([i, j])
					visited[i][j].append([x, y])

	# bottom left corner
	elif (x == rows-1 and y == 0):
		if (mat[x][y+1] != 0 and ([x, y+1] not in visited[x][y])):
			q.append([x, y+1])
			visited[x][y+1].append([x, y])
		
		if (mat[x-1][y+1] != 0 and ([x-1, y+1] not in visited[x][y])):
			q.append([x-1, y+1])
			visited[x-1][y+1].append([x, y])

		if (mat[x-1][y] != 0 and ([x-1, y] not in visited[x][y])):
			q.append([x-1, y])
			visited[x-1][y].append([x, y])

	# entire first row
	elif (x == 0):
		for i in range(x, x+2):
			for j in range(y-1, y+2):
				if ((i!=x or j!=y) and mat[i][j]!=0 and ([i, j] not in visited[x][y])):
					q.append([i, j])
					visited[i][j].append([x, y])		
	
	# entire last row
	elif (x == rows-1):
		for i in range(x-1, x+1):
			for j in range(y-1, y+2):
				if ((i!=x or j!=y) and mat[i][j]!=0 and ([i, j] not in visited[x][y])):
					q.append([i, j])
					visited[i][j].append([x, y])

	# inside the outermost square
	# excluding 1st and last row as well as 1st and last column
	elif (x>0 and x<rows-1 and y>0 and y<columns-1):
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if ((i!=x or j!=y) and mat[i][j]!=0 and ([i, j] not in visited[x][y])):
					q.append([i, j])
					visited[i][j].append([x, y])

	else:		
		print(pt, "Error")
		break

# stop the timer
stop = timeit.default_timer()

all_paths = []

# adding the elements to sample path
for i in range(rows):
	if len(visited[i][columns-1])>0:
		sample_paths = []
		getPath(i, columns-1)
		sample_paths.append([0, 0])
		sample_paths.reverse()
		all_paths.append(sample_paths)

# if paths exist then print some of them
if paths>0:
	print("Some of the possible paths are: \n")

	for item in all_paths:
		print()
		print(*item, sep=' -> ')
		print("Cost of the path is:", len(item)-1)

# print the total number of paths
print("\nTotal number of paths:", paths)

# print the time taken for algorithm
print("\nTime taken:", stop - start, "seconds")
