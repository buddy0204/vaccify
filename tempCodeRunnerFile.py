# Library for INT_MAX
import sys


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.parent = [-1] * vertices  # Array to store constructed shortest path tree

    def printPath(self, j):
        """Function to print shortest path from source to j using parent array"""
        if self.parent[j] == -1:  # Base Case : If j is source
            print(j, end='')
            return
        self.printPath(self.parent[j])
        print(" ->", j, end='')

    def printSolution(self, dist, src):
        print("Vertex\tDistance from Source\tPath")
        for i in range(1, self.V):
            print("\n%d --> %d \t\t%d \t\t\t" % (src, i, dist[i]), end='')
            self.printPath(i)

    def minDistance(self, dist, sptSet):
        # Initialize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not yet processed.
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than new distance and the vertex is not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    self.parent[v] = u

        self.printSolution(dist, src)


# Driver's code
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    # Take root node (source vertex) from user
    src = int(input("Enter source node (0 to 8 for this graph): "))
    g.dijkstra(src)
