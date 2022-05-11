from collections import defaultdict

# class Graph:
#
# 	def __init__(self):
# 		self.graph = defaultdict(list)
#
# 	def addEdge(self,u,v):
# 		self.graph[u].append(v)
#
# 	def DFSUtil(self,v,visited):
# 		print(v, end=" ")
# 		visited[v] = True
#
# 		for neighbour in self.graph[v]:
# 			if not visited[neighbour]:
# 				self.DFSUtil(neighbour, visited)
#
# 	def DFS(self,v):
# 		visited = [False] * len(self.graph)
# 		self.DFSUtil(v,visited)

class Graph:

	def __init__(self):
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self,u):
		visited = [False] * len(self.graph)

		queue=[]
		queue.append(u)
		visited[u]=True

		while queue:
			u = queue.pop()
			print(u, end=" ")

			for i in self.graph[u]:
				if visited[i] == False:
					queue.append(i)
					visited[i]=True


g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("BFS Starting from vertex 1 is ")
g.BFS(1)

