from collections import defaultdict

# Read input
n, m = map(int, input().split())

# Create a dictionary to store the edges of the graph
graph = defaultdict(list)

# Read the edges and add them to the graph
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# Initialize the colors for each city to 0 (uncolored)
colors = [0] * (n+1)

# Create a queue for the breadth-first search
queue = []

# Add the first city to the queue
queue.append(1)

# Set the color of the first city to 1
colors[1] = 1

# Create a variable to store the result
result = []

# Perform breadth-first search
while queue:
  # Get the next city in the queue
  city = queue.pop(0)

  # Add the city to the appropriate group in the result
  if colors[city] == 1:
    result.append(city)
  else:
    result[0] = city

  # Get the neighbors of the city
  neighbors = graph[city]

  # Color the neighbors with the opposite color
  for neighbor in neighbors:
    if colors[neighbor] == 0:
      colors[neighbor] = -colors[city]
      queue.append(neighbor)
    elif colors[neighbor] == colors[city]:
      # If a neighbor has the same color as the current city, it is not possible to partition the cities
      print("Nelze")
      exit()

# Print the result
print(" ".join(map(str, result[::-1])))
print(" ".join(map(str, result[1:])))
