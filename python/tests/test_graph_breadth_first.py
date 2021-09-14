from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)



class Vertex:
    def __init__(self, value=None):
        self.value = value
    # def __str__(self):
    #     return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex.value] = []
        return vertex.value
    

    def add_edge(self, startV , endV, wight=0):
        if startV in self.adjacency_list and endV in self.adjacency_list :
            self.adjacency_list[startV].append(Edge(endV, wight))
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
        if vertex in self.adjacency_list :
            n = [(v.vertex, v.wight) for v in self.adjacency_list[vertex]]
            return n
        else: 
            return 'not exist'
 
    
    def size(self):
        return len(self.adjacency_list.keys())

    def breadth_first(self,node):
        if node not in self.adjacency_list:
            return 'Exception'
        all_nodes=[]
        breadth = Queue()
        visited = set()
        breadth.enqueue(node)
        visited.add(node)
        while breadth:
            front=breadth.dequeue()
            all_nodes.append(front)
            for edge in self.adjacency_list[front]:
                if edge.vertix not in visited:
                    visited.add(edge.vertix)
                    breadth.enqueue(edge.vertix)

        return all_nodes
#############TEST###########

def test_breadth_first():
    graph = Graph()
    pandora= graph.add_vertex('pandora')
    arendelle= graph.add_vertex('arendelle')
    metroville= graph.add_vertex('metroville')
    narina= graph.add_vertex('narina')
    naboo= graph.add_vertex('naboo')
    manstropolis= graph.add_vertex('manstropolis')
    graph.add_edge(pandora,arendelle)
    graph.add_edge(arendelle,pandora)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(metroville,arendelle)
    graph.add_edge(metroville,manstropolis)
    graph.add_edge(metroville,naboo)
    graph.add_edge(metroville,narina)
    graph.add_edge(narina,metroville)
    graph.add_edge(narina,naboo)
    graph.add_edge(naboo,narina)
    graph.add_edge(naboo,metroville)
    graph.add_edge(naboo,manstropolis)
    graph.add_edge(manstropolis,naboo)
    graph.add_edge(manstropolis,arendelle)
    graph.add_edge(manstropolis,metroville)
    actual=graph.breadth_first(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,naboo,narina]
    assert actual==expected



def test_edge_cases():
    graph = Graph()
    pandora=Vertex('pandora')
    actual=graph.breadth_first(pandora)
    expected='Exception'
    assert actual==expected


def test_expected_failure():
    graph = Graph()
    pandora= graph.add_vertex('pandora')
    arendelle= graph.add_vertex('arendelle')
    metroville= graph.add_vertex('metroville')
    narina= graph.add_vertex('narina')
    naboo= graph.add_vertex('naboo')
    manstropolis= graph.add_vertex('manstropolis')
    graph.add_edge(pandora,arendelle)
    graph.add_edge(arendelle,pandora)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(metroville,arendelle)
    graph.add_edge(metroville,manstropolis)
    graph.add_edge(metroville,naboo)
    graph.add_edge(metroville,narina)
    graph.add_edge(narina,metroville)
    graph.add_edge(narina,naboo)
    graph.add_edge(naboo,narina)
    graph.add_edge(naboo,metroville)
    graph.add_edge(naboo,manstropolis)
    graph.add_edge(manstropolis,naboo)
    graph.add_edge(manstropolis,arendelle)
    graph.add_edge(manstropolis,metroville)
    actual=graph.breadth_first(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,narina,naboo]
    assert actual!=expected