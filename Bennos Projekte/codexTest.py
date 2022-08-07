# create a class to represent a graph
class Graph:
    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    # function to add vertices
    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    # function to add edges
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph


    # function to find the shortest path using dijkstra
    def dijkstra(self, start, end):
        # initializing the distance to infinity
        dist = {}
        prev = {}
        for vertex in self.vertices():
            dist[vertex] = float('inf')
            prev[vertex] = None
        dist[start] = 0
        Q = self.vertices()
        while len(Q) > 0:
            # find the vertex with the minimum distance
            u = min(dist, key=dist.get)
            # remove the minimum distance vertex from the set
            Q.remove(u)
            if u == end:
                break
            # update the distances
            for v in self.__graph_dict[u]:
                alt = dist[u] + self.__graph_dict[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        # reconstruct the path
        path = []
        u = end
        while prev[u] is not None:
            path.insert(0, u)
            u = prev[u]
        path.insert(0, u)
        return path

    # function to return edges of the graph
    def edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    # function to print the graph
    def print_graph(self):
        print(self.__graph_dict)


# create a graph for testing purposes
graph = {'A': {'B': 10, 'C': 20},
         'B': {'C': 1, 'D': 2},
         'C': {'D': 3, 'E': 5},
         'D': {'E': 1},
         'E': {'B': 1}
         }

# create a graph object
g = Graph(graph)

# print the vertices
print(g.vertices())

# print the edges
print(g.edges())

# print the shortest path
print(g.dijkstra('A', 'D'))
