from collections import deque

class Graph:
    def __init__(self):
        self.numOfVertex = 0
        self.numOfEdges = 0
        self.numOfComponents = 0
        self.graph = [None]
    

    def defineGraph(self):
        self.graph = [[] for vertex in range(self.numOfVertex + 1)]
        self.marked = [False] * len(self.graph)
        self.graph[0] = None


    def addEdge(self, u, v):
        self.graph[v].append(u) # insere u na lista de adjacencias de v
        self.graph[u].append(v) # insere v na lsita de adjacencias de u
        self.numOfEdges += 1

    def loadData(self, dataPath):
        print('Carregando dados...')
        file = open(dataPath, 'r')
        read = file.readlines()

        self.numOfVertex = int(read[0])

        self.defineGraph()

        for edge in read[1:]:
            E = edge.strip().split() #EX: elemento '1 102\n' passa a ser um vetor ['1', '102']
            
            self.addEdge(int(E[0]), int(E[1]))
        print('dados carregados com sucesso\n')

    #exibe as listas de adjacencia de n vértices no grafo, começando em m 
    def showAdjList(self, n = 0, m = 1):
        if(self.numOfVertex == 0):
            print(f'Grafo vazio\n{self.graph}')
            return
        
        for vertex in range(m+n)[m:]:
            print(f'{vertex}:', end='  ')
            for edge in self.graph[vertex]:
                print(f'{edge}  ->', end='  ')
            print('\n\n')

    def adjList(self):
        return self.graph

    def numVertex(self):
        return self.numOfVertex

    def numEdges(self):
        return self.numOfEdges

    def biggestResearcher(self):
        self.maxDegree()
        return self.biggestCollaboratorID

    def minDegree(self):
        allDegrees = [len(v) for v in self.graph[1:]]
        minD = min(degree for degree in allDegrees if degree > 0)
        return minD

    def maxDegree(self):
        maxLength = max(self.graph[1:], key = lambda v: len(v))
        maxD = len(maxLength)
        self.biggestCollaboratorID = self.graph.index(maxLength)
        return maxD
    

    def components(self):
        #print('iniciando contagem de componentes por meio de busca em profundidade...')
        self.marked[0] = True #marca o elemento 0 (nulo) da lista de adjacencia
        
        for vIndex in range(1, len(self.graph)):
            vertice = self.graph[vIndex]
            # tratamento de vértices q não existem no grafo
            if len(vertice) == 0:
                self.marked[vIndex] = True
                continue

            if not self.marked[vIndex]:
                self.depthFirstSearch(vIndex)
                self.numOfComponents += 1
                
        return self.numOfComponents
        
    def depthFirstSearch(self, startingPoint):
        g = self.adjList()
                
        pilha = deque()
        pilha.append(startingPoint)

        while (len(pilha) > 0):
            vertice = pilha[-1]
            pilha.pop()

            if not self.marked[vertice]:
                self.marked[vertice] = True
                for adjacency in list(reversed(g[vertice])):
                    if (not self.marked[adjacency]):
                        pilha.append(adjacency)
