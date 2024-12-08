#Cycle detenction in graph--> start node and end node have to be the same 
#it will return true if cycle is detenced, and false if not 

from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isCyclicUtil(self,v,visited,recstack):
        #step1: mark the current node as visited and put it in the recstack
        visited[v] = True
        recstack[v] = True

        #recur down the graph with neighbor nodes and if that node is in the recstack-
        #then the graph is cyclic
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor,visited,recstack) == True:
                    return True
                
            elif visited[neighbor]==True:
                return True
            

    #if cycle detected return True or False
    def iscycle(self):
        visited=[False] * (self.v+1)
        recstack=[False] * (self.v+1)
        for node in range(self.v):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recstack)==True:
                    return True
                
        return False
    
g = Graph(4)

g.addEdge(0,1)
g.addEdge(0,2)

g.addEdge(1,2)
g.addEdge(2,0)

g.addEdge(2,3)
g.addEdge(3,3)

if g.iscycle()==1:
    print("the graph is cyclic")
else:
    print("graph is non cyclic")

    


