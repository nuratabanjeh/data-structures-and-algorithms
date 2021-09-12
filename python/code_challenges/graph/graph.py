class Vertex:
    def __init__(self, value=None):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'
class Edge:
    def __init__(self, vertex, wight):
        self.vertex = vertex
        self.wight = wight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_vertex(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex.value] = []
        return vertex.value


    def add_edge(self, startV , endV, wight=0):
        if startV in self._adjacency_list and endV in self._adjacency_list :
            self._adjacency_list[startV].append(Edge(endV, wight))
        else:
            return 'not exist'

    def get_nodes(self):
        list=[]
        for vertix in self.adjacency_list.keys():
            list.append(vertix)
        if len(list)==0:
            return None
        return list

    def get_neighbors(self , vertex):
        if vertex in self._adjacency_list :
            n = [(v.vertex, v.wight) for v in self._adjacency_list[vertex]]
            return n
        else: 
            return 'not exist'

    def size(self):
        return len(self._adjacency_list)




 