import GraphProcessing as g

grafo = g.Graph()
grafo.loadData('dblp.txt')

print('#' * 30)
print('O arquivo de teste identifica: ')

#número de pesquisadores
print(f'\n{grafo.numVertex()} pesquisadores')

#número de colaborações
print(f'\n{grafo.numEdges()} colaborações')

#id do pesquisador que mais colaborou e quantas foram as colaborações
print(f'\n{grafo.biggestResearcher()} como o pesquisador que mais colaborou, com {grafo.maxDegree()} colaborações')

#menor número de colaborações
print(f'\n{grafo.minDegree()} como sendo o menor número de colaborações')

#número de subredes de colaboração
print(f'\n{grafo.components()} subredes de colaboração')

print('#' * 30)