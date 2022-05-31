from abstractGraph import Graph,Edge

class AdjListGraph(Graph):
    '''Adjacency list implementation of the graph'''

    def __init__(self,nVertices,directed,edgeWtType):
        super().__init__(nVertices, directed, edgeWtType)
        self.adjLists = [[] for i in range(nVertices)]

    def addGraphEdge(self,u,v,weight):
        edges = self.outgoingEdges(u)
        for edge in edges:
            if edge.end == v:
                raise ValueError('Edge from ' + u + ' to ' + v
                                 + ' not added as it already exists')
        self.adjLists[u].append(Edge(u,v,weight))

    def outgoingEdges(self,u):
        self.checkVertex(u)
        '''return self.EdgeIter(self.adjLists[u])'''
        return iter(self.adjLists[u])

    def delGraphEdge(self,u,v):
        edges = self.outgoingEdges(u)
        index = 0
        for edge in edges:
            if edge.end == v:
                break
            index += 1
        if index < len(self.adjLists[u]):
            return self.adjLists[u].pop(index)
        else:
            return None

    def getEdge(self,u,v):
        self.checkVertex(u)
        edges = self.outgoingEdges(u)
        for edge in edges:
            if edge.end == v:
                return edge
        return None

    def isEdge(self,u,v):
        return self.getEdge(u,v) is not None


        
        
        
