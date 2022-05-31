from edgeWeight import GraphEdgeWeight

def checkInput(val,reqType):
    if not isinstance(val,reqType):
        raise ValueError(str(val) + " is not a type of " + typeOf)
 
class Edge:
    ''' Defines a graph edge'''
    _immutable = False
    def __init__(self,u,v,weight):
        self.start = u
        self.end = v
        self.weight = weight
        self._immutable = True

    def __str__(self):
        return '({},{})({})'.format(self.start,self.end,self.weight)

    def __setattr__(self, *args, **kwargs):
        if self._immutable:
            raise AttributeError('Edge is immutable!')
        object.__setattr__(self, *args, **kwargs) 

class Graph:
    '''Defines an abstract graph interface'''
    def checkVertex(self,u):
        checkInput(u, int)
        if u < 0 or u >= self.nVertices:
            raise ValueError('Vertex ' + str(u)  + ' is not valid')

    def __init__(self,nVertices, directed,edgeWtType):
        checkInput(nVertices, int)
        checkInput(directed, bool)
        self.nVertices = nVertices
        self.directed = directed
        self.edgeWtType = edgeWtType
        self.marks = [0 for i in range(nVertices)]
        self.nEdges = 0

    def isDirected(self):
        return self.directed

    def numVertices(self):
        '''Number of vertices in the graph'''
        return self.nVertices

    def numEdges(self):
        '''Number of edges in the graph'''
        return self.nEdges

    def addGraphEdge(self,u,v,weight):
        '''Add a graph edge -- implement dependent'''
        pass

    def addEdge(self,u,v,weight):
        '''Add edge from u to v with weight'''
        self.checkVertex(u)
        self.checkVertex(v)
        checkInput(weight, self.edgeWtType)
        self.addGraphEdge(u,v,weight)
        if not self.directed:
            self.addGraphEdge(v,u,weight)
        self.nEdges += 1

    def delGraphEdge(self,u,v):
        '''Delete the graph edge from u to v if it exists'''
        pass

    def delEdge(self,u,v):
        '''Delete edge from u to v'''
        self.checkVertex(u)
        self.checkVertex(v)
        self.delGraphEdge(u,v)
        if not self.directed:
            self.delGraphEdge(v,u)
        self.nEdges -= 1

    def setMark(self,u,val):
        '''set a mark on vertex u'''
        self.checkVertex(u)
        checkInput(val,int)
        self.marks[u] = val

    def getMark(self,u):
        '''get mark of vertex u'''
        self.checkVertex(u)
        return self.marks[u]

    def getEdge(self, u,v) -> Edge:
        ''' get edge from u to v if it exists else None'''
        pass

    def isEdge(self, u, v) -> bool:
       '''Is there an edge from u to v ?'''
       pass

    def outgoingEdges(self,u) -> iter:
        '''get outgoing edge iterator for vertex u'''
        pass

    def __str__(self):
        st = 'Printing the edges of the '
        if self.directed:
            st += 'directed graph:\n'
        else:
            st += 'undirected graph:\n'
        for u in range(self.nVertices):
            st += 'Outgoing edges from ' + str(u) + ':'
            for e in self.outgoingEdges(u):
                st += str(e) + ','
            st += '\n'
        return st


        

    

        

    

        
        

        
