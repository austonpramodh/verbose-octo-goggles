from queue import PriorityQueue
import sys
from abstractGraph import Graph
from adjListGraph import AdjListGraph
from edgeWeight import EdgeCost

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

def strongConnectivityComponents(graph: AdjListGraph):
  numVertices = graph.numVertices()
  disc = [-1] * (numVertices)
  low = [-1] * (numVertices)
  stackMember = [False] * (numVertices)
  st =[]
  
  result = []

  def SCCUtil(graph:AdjListGraph, vertex, low, disc, stackMember, st, time = 0):

    disc[vertex] = time
    low[vertex] = time
    time += 1
    stackMember[vertex] = True
    st.append(vertex)

    for edge in graph.outgoingEdges(vertex):
      current_vertex = edge.end
      if disc[current_vertex] == -1 :
      
        SCCUtil(graph, current_vertex, low, disc, stackMember, st, time)

        low[vertex] = min(low[vertex], low[current_vertex])
            
      elif stackMember[current_vertex] == True:
        low[vertex] = min(low[vertex], disc[current_vertex])

    w = -1
    if low[vertex] == disc[vertex]:
      result.append([])
      while w != vertex:
        w = st.pop()
        print (w, end=" ")
        result[len(result)-1].append(w)
        stackMember[w] = False
        
      print()
      
  
  for i in range(numVertices):
    if disc[i] == -1:
      SCCUtil(graph, i, low, disc, stackMember, st)

  return result

def strongConnectivity(g):
    '''Given a directed graph g, returns a tuple consisting of
       (i) an array of LOWLINK values computed in the DFS,
       (ii) a list of roots of strongly connected components of g in the DFS tree and
       (iii) a list of biconnected components each of which is expressed as
           a list of edges
    '''
    lowLinkArr = dfsFindLowLink(g)
    sccComponents = strongConnectivityComponents(g)

    roots = [sccComponent[0] for sccComponent in sccComponents]
    comps = sccComponents
    return (lowLinkArr,roots,comps)

def shortestPathDijkstra(graph,sourceVertex = 0):
    '''Returns an array of shortest path lengths in directed graph g from
        sourceVertex to every other vertex in graph using Dijkstra's algorithm
        Assume EdgeCost objects are used for weights and they have positive values;
        also use * operation for addition of edge weights and + operation for
        minimum of 2 path lengths (this is consistent with semi-ring ops!!)
        See the example in BFS function
    '''
    D = {v: EdgeCost(float('inf')) for v in range(graph.numVertices())}
    D[sourceVertex] = EdgeCost(float(0))

    # pq = PriorityQueue()
    # pq.put((EdgeCost(float(0)), sourceVertex))
    pq = []
    pq.append((EdgeCost(float(0)), sourceVertex))

    # while not pq.empty():
    while len(pq) > 0:
        # (dist, current_vertex) = pq.get()
        (dist, current_vertex) = pq.pop(0)
        graph.setMark(current_vertex, VISITED)

        edges = graph.outgoingEdges(current_vertex)
        for edge in edges:
            neighbor = edge.end
            distance = edge.weight
            # If not visited
            if graph.getMark(neighbor) != VISITED:
                old_cost = D[neighbor]
                # Using * as the EdgeCost class has operator overloading for addition
                new_cost = D[current_vertex] * distance
                if float(new_cost.w) < float(old_cost.w):
                    # pq.put((new_cost, neighbor))
                    pq.append((new_cost, neighbor))
                    # TODO: Run pq sorting with lambda
                    pq.sort(key=lambda x: x[0].w)
                    D[neighbor] = new_cost

    # Manipyulating the return value for desired data structure
    shortestPathLengths = [0 for v in range(graph.numVertices())]
    for key in D:
        shortestPathLengths[key] = D[key].w

    return shortestPathLengths


def minCostSpanningTreePrim(graph: Graph,sourceVertex = 0):
    '''Returns minimum cost spanning tree of a connected undirected graph using Prim's
       algorithm starting from sourceVertex. The tree should be returned
       as AdjListGrap instance (undirected).
       Assume EdgeCost objects are used for weights and they have positive values;
       also use * operation for addition of edge weights and + operation for
       minimum edge weight
    '''
    mtx = adjListGraphToMtx(graph, 0)
    numVertices = graph.numVertices()
    INF = 9999999
    visited =  [0 for i in range(numVertices)]
    no_edge = 0
    visited[sourceVertex] = True

    resultingAdjListGraph = AdjListGraph(numVertices, graph.isDirected(), graph.edgeWtType)

    while (no_edge < numVertices - 1):
        minimum = EdgeCost(INF)
        x = 0
        y = 0
        for i in range(numVertices):
            if visited[i]:
                for j in range(numVertices):
                    if ((not visited[j]) and mtx[i][j]):
                        # The comparison operator overloading is not implemented in EdgeCost, therefore we 
                        # will need to access the "w"
                        if minimum.w > mtx[i][j].w:
                            minimum = mtx[i][j]
                            x = i
                            y = j
        resultingAdjListGraph.addEdge(x, y, mtx[x][y])
        visited[y] = True
        no_edge += 1

    return resultingAdjListGraph

# util

def adjListGraphToMtx(graph:Graph, defaultVal = float("inf")):
    # Generate a weight matrix from the graph
    numVertex = graph.numVertices()
    # mtx = [[float("inf") for i in range(0, numVertex)] for i in range(0, numVertex)]
    mtx = [[] for i in range(0, numVertex)]
    for row in range(0, numVertex):
        for col in range(0, numVertex):
            if row == col:
                mtx[row].append(0)
            else:
                mtx[row].append(defaultVal)
    # Get the verteces
    for current_vertex in range(0, numVertex):
        # Get the outgoing edge for this specific vertex
        edges = graph.outgoingEdges(current_vertex)
        for edge in edges:
            start = current_vertex
            end  = edge.end
            weight = edge.weight
            mtx[start][end] = weight
    return mtx

def allPairPathWarshallFloyd(graph:Graph):
    '''Returns the nxn matrix of all pair sum of path products using Floyd-Warshall
       algorithm. You should assume that all edges have abstract GraphEdgeWeight instances
       Use closure property provided in GraphEdgeWeight
    '''
    # Prepare the matrix for the algorthm
    numVertex = graph.numVertices()
    mtx = adjListGraphToMtx(graph)
    # Run the floydWarshall algorthm on the prepared matrix
    distMtx = list(map(lambda i: list(map(lambda j: j, i)), mtx))
 
    for k in range(numVertex):
         for i in range(numVertex):
            for j in range(numVertex):
                distMtx[i][j] = min(distMtx[i][j],
                # using * instead of + due to the operator overloading on the EdgeCost class
                                 distMtx[i][k] * distMtx[k][j])
    return distMtx
 