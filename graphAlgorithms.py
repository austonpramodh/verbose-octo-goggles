from adjListGraph import AdjListGraph

UNVISITED = 0
VISITED = 1
DEBUG = 1

def preVisit(g,v):
    if DEBUG:
        print('{}({}),'.format(v,g.getMark(v)))

def postVisit(g,v):
    pass
          
def dfs(g,v,dfNum):
    '''Traverse graph starting from vertex v using DFS'''
    '''Marks indicate DFS number of vertices'''
    dfNum += 1
    g.setMark(v,dfNum)
    preVisit(g,v)
    edges = g.outgoingEdges(v)
    for edge in edges:
        w = edge.end
        if g.getMark(w) != UNVISITED:
            continue
        dfNum = dfs(g,w,dfNum)
    postVisit(g,v)
    return dfNum

 
def bfs(g,startVertex,num):
    '''Traverse graph starting vertex b using BFS'''
    '''Marks indicate level numbers of vertices in BFS tree'''
    queue = [startVertex]
    cost = [g.edgeWtType.multIdent() for i in range(g.numVertices())]
    g.setMark(startVertex,1)
    sumCosts = g.edgeWtType.addIdent()
    while len(queue) > 0:
        v = queue.pop(0)
        preVisit(g,v)
        edges = g.outgoingEdges(v)
        for edge in edges:
            w = edge.end
            if g.getMark(w) != UNVISITED:
                continue
            cost[w] = cost[v] * edge.weight
            sumCosts += edge.weight
            if DEBUG:
                print('Cost of path from {} to {} in BFS tree = {}'.
                      format(startVertex, w, cost[w]))
            g.setMark(w,g.getMark(v)+1)
            queue.append(w)
        postVisit(g,v)
    if DEBUG:
        print('sum of costs of all paths in BFS tree {}'.format(sumCosts))

        
def traverse(g,method):
    '''Traverse graph g using method (dfs or bfs))'''
    for u in range(g.numVertices()):
        g.setMark(u,UNVISITED)
    num = 0
    for u in range(g.numVertices()):
        if g.getMark(u) != UNVISITED:
            continue
        if DEBUG:
            print('Start vertex : ' + str(u))
        num = method(g,u,num)
    if DEBUG:
        print('\n')
        
def biconnectivity(g):
    '''Given an undirected graph g, returns a tuple consisting of
       (i) an array of LOW values computed in the DFS,
       (ii) a list of separation vertices of g and 
       (iii) a list of biconnected components each of which is expressed as
            a list of edges
    '''
    lowArr = [0 for i in range(g.numVertices())]
    sepVertices = []
    comps = []
    return (lowArr,sepVertices,comps)

# TODO: modified code here----
def dfsFindLowLink(graph, vertex = 0, lowLinkArr = [], prevVertex = 0):
    '''Traverse graph starting from vertex v using DFS'''
    '''Marks indicate DFS number of vertices'''

    if len(lowLinkArr) != graph.numVertices():
        lowLinkArr = [99999 for i in range(graph.numVertices())]

    graph.setMark(vertex,VISITED)
    edges = graph.outgoingEdges(vertex)
    for edge in edges:
        endVertex = edge.end
        print(f'start: {edge.start}, end: {edge.end}')
        print(f"prevVertex={prevVertex} lowLinkArr[vertex]={lowLinkArr[vertex]}, edge.end={edge.end}")

        lowLinkArr[vertex] = min(lowLinkArr[vertex],vertex, endVertex)

        # Already visited
        if graph.getMark(endVertex) != UNVISITED:
            continue

        dfsFindLowLink(graph, endVertex, lowLinkArr)

    return lowLinkArr
# TODO: modified code here----

def strongConnectivity(g):
    '''Given a directed graph g, returns a tuple consisting of
       (i) an array of LOWLINK values computed in the DFS,
       (ii) a list of roots of strongly connected components of g in the DFS tree and
       (iii) a list of biconnected components each of which is expressed as
           a list of edges
    '''
    lowLinkArr = dfsFindLowLink(g)
    
    roots = []
    comps = []
    return (lowLinkArr,roots,comps)

def shortestPathDijkstra(g,sourceVertex):
    '''Returns an array of shortest path lengths in directed graph g from
        sourceVertex to every other vertex in graph using Dijkstra's algorithm
        Assume EdgeCost objects are used for weights and they have positive values;
        also use * operation for addition of edge weights and + operation for
        minimum of 2 path lengths (this is consistent with semi-ring ops!!)
        See the example in BFS function
    '''

def minCostSpanningTreePrim(g,sourceVertex):
    '''Returns minimum cost spanning tree of a connected undirected graph using Prim's
       algorithm starting from sourceVertex. The tree should be returned
       as AdjListGrap instance (undirected).
       Assume EdgeCost objects are used for weights and they have positive values;
       also use * operation for addition of edge weights and + operation for
       minimum edge weight
    '''

def allPairPathWarshallFloyd(g):
    '''Returns the nxn matrix of all pair sum of path products using Floyd-Warshall
       algorithm. You should assume that all edges have abstract GraphEdgeWeight instances
       Use closure property provided in GraphEdgeWeight
    '''
            
    


