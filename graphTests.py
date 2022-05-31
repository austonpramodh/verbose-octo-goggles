from edgeWeight import EdgeCost, EdgeProbability
from adjListGraph import AdjListGraph
import graphAlgorithms as galg

e = EdgeCost(100)
print('closure of e in min semi ring = ' + str(e.closure()))
print('add identity for EdgeCost = ' + str(EdgeCost.addIdent()))
print('mult identity for EdgeCost = ' + str(EdgeCost.multIdent()))

e1 = EdgeProbability(0.6)
print('closure of e1 in max probability semiring = ' + str(e1.closure()))
print('add identity for EdgeProbability = ' + str(EdgeProbability.addIdent()))
print('mult identity for EdgeProbability = ' + str(EdgeProbability.multIdent()))

DEBUG = 1
g = AdjListGraph(8,False,EdgeCost)
g.addEdge(1,2,EdgeCost(5))
g.addEdge(1,4,EdgeCost(3))
g.addEdge(1,3,EdgeCost(2))
g.addEdge(0,3,EdgeCost(6))
g.addEdge(0,4,EdgeCost(2))
g.addEdge(6,4,EdgeCost(3))
g.addEdge(6,5,EdgeCost(4))
g.addEdge(6,7,EdgeCost(5))
g.addEdge(5,7,EdgeCost(8))
print(g)
print("# of vertices of g = " + str(g.numVertices()))
print("# of edges of g = " + str(g.numEdges()))
galg.traverse(g,galg.dfs)
galg.traverse(g,galg.bfs)

g1 = AdjListGraph(8,True,EdgeCost)
g1.addEdge(0,1,EdgeCost(1))
g1.addEdge(0,3,EdgeCost(1))
g1.addEdge(0,4,EdgeCost(1))
g1.addEdge(1,2,EdgeCost(1))
g1.addEdge(1,3,EdgeCost(1))
g1.addEdge(2,0,EdgeCost(1))
g1.addEdge(3,2,EdgeCost(1))
g1.addEdge(4,3,EdgeCost(1))
g1.addEdge(6,4,EdgeCost(1))
g1.addEdge(5,6,EdgeCost(1))
g1.addEdge(5,7,EdgeCost(1))
g1.addEdge(7,3,EdgeCost(1))
g1.addEdge(7,5,EdgeCost(1))
g1.addEdge(7,6,EdgeCost(1))
print(g1)
print("# of vertices of g1 = " + str(g1.numVertices()))
print("# of edges of g1 = " + str(g1.numEdges()))
(lowLinkArr,componentRoots, comps) = galg.strongConnectivity(g1)
print('low link values : {}'.format(lowLinkArr))
print('roots of strongly connected components of directed graph g1 in DFS tree = {}'.format(
           componentRoots))
print('strongly connected components of g1 = {}:', end = " ")
for comp in comps:
    print(str(comp), end = ',')
print('')

