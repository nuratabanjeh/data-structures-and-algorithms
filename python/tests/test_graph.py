class Vertex:
    def __init__(self, value=None):
        self.value = value
    def __str__(self):
        return 
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


    def depth_first(self, startV):
        visited = []
        def check(vertex):
            visited.append(vertex)
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                if neighbor[0] not in visited:
                    check(neighbor[0])

        check(startV)
        return visited

############Test#############

def test_depth_first():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A','C')
    graph.add_edge('A','B')
    graph.add_edge('C','D')
    graph.add_edge('B','A')
    actual = graph.depth_first('A')
    expected = ['A', 'C', 'D', 'B']
    assert actual == expected

   