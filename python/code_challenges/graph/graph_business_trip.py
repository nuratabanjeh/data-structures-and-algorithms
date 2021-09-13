class Vertex:
    def __init__(self, value=None):
        self.value = value
    def __str__(self):
        return f'vertix > {self.value}'

class Edge:
    def __init__(self, vertex , weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex.value] = []
        return vertex.value
    

    def add_edge(self, startV , endV, weight=0):
        if startV in self.adjacency_list and endV in self.adjacency_list :
            self.adjacency_list[startV].append(Edge(endV, weight))
        else:
            return 'not exist'
    
    def get_nodes(self):
        list=[]
        for vertex in self.adjacency_list.keys():
            list.append(vertex)
        if len(list)==0:
            return None
        return list
    
    def get_neighbors(self , vertex):
        if vertex in self.adjacency_list :
            n = [(v.vertex, v.weight) for v in self.adjacency_list[vertex]]
            return n
        else: 
            return 'not exist'
 
    
    def size(self):
        return len(self.adjacency_list.keys())

def business_trip(graph,cities):
    boolean = True
    cost = 0
    for i in range(len(cities)-1):
        for city in graph.get_neighbors(cities[i]):
            if cities[i+1]==city[0]:
                cost+=city[1]
                break
            else:
                boolean=False
        
    if boolean==False:
            cost=0
    
    return boolean, '$'+str(cost)  





if __name__ == '__main__':
    graph = Graph()

    pandora= graph.add_vertex('pandora')
    arendelle= graph.add_vertex('arendelle')
    metroville= graph.add_vertex('metroville')
    narina= graph.add_vertex('narina')
    naboo= graph.add_vertex('naboo')
    manstropolis= graph.add_vertex('manstropolis')
    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,manstropolis,42)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,manstropolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narina,37)
    graph.add_edge(narina,metroville,37)
    graph.add_edge(narina,naboo,250)
    graph.add_edge(naboo,narina,250)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,manstropolis,73)
    graph.add_edge(manstropolis,naboo,73)
    graph.add_edge(manstropolis,arendelle,42)
    graph.add_edge(manstropolis,metroville,105)
    print(business_trip(graph,[metroville,pandora]))