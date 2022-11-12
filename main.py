import networkx as nx
import pylab as plt
import numpy as np
import random

n = 6

matrix_1 = np.random.randint(0, 2, size=(n, n))
matrix_2 = np.random.randint(0, 2, size=(n, n))

luckyNumber = random.randint(1,7);

list_edge_G1 = []
list_edge_G2 = []

G1 = nx.Graph()
G2 = nx.Graph()

def generateGraph():
    count = 0
    for i in range(0,n):
        count = 0
        for j in matrix_2[i]:
            if j != 0:
                list_edge_G2.append((i,count))
            count += 1

    for i in range(0,n):
        count = 0
        for j in matrix_1[i]:
            if j != 0:
                list_edge_G1.append((i,count))
            count += 1

def generateIsomorphismGraph():

    for i in range(0, n):
        for j in range(0,n):
            matrix_2[i][j] = matrix_1[i][j]

    for i in range(0,n):
        count = 0
        for j in matrix_2[i]:
            if j != 0:
                list_edge_G2.append((i,count))
            count += 1

    for j in range(0,int(n/2)):
        c = random.randint(0,n-1)
        d = random.randint(0,n-1)
        a = min(c,d)
        b = max(c,d)
        p = b - a

        for i in range(0,n):
            matrix_1[i][a], matrix_1[i][b] = matrix_1[i][b], matrix_1[i][a]

        for i in range(0,n):
            matrix_1[a][i], matrix_1[b][i] = matrix_1[b][i], matrix_1[a][i]

    for i in range(0,n):
        for j in range(0,n):
            if(matrix_1[i][j] != 0):
                if(i == a or i == b or j == a or j == b):
                    if(i == a and j == a):
                        list_edge_G1.append((i + p,j + p))
                    elif(i == b and j == b):
                        list_edge_G1.append((i - p,j - p))
                    elif(i == a and j == b):
                        list_edge_G1.append((i + p,j - p))
                    elif(i == b and j == a):
                        list_edge_G1.append((i - p,j + p))
                    elif(j == a):
                        list_edge_G1.append((i,j + p))
                    elif(j == b):
                        list_edge_G1.append((i,j - p))
                    elif(i == a):
                        list_edge_G1.append((i + p,j))
                    elif(i == b):
                        list_edge_G1.append((i - p,j))
                else:
                    list_edge_G1.append((i,j))


'''
    generateGraph() to create two normal graph
    generateIsomorphismGraph() to create two isomorphic graph
'''
if(luckyNumber % 2 == 0):
    generateIsomorphismGraph()
else:
    generateGraph()

print(luckyNumber)

for i in list_edge_G1:
    G1.add_edge(i[0],i[1])

for i in list_edge_G2:
    G2.add_edge(i[0],i[1])

pos1 = nx.spring_layout(G1)
node_colors1 = [np.sqrt((xy**2).sum()) for xy in pos1.values()]
pos2 = nx.spring_layout(G2)
node_colors2 = [np.sqrt((xy**2).sum()) for xy in pos2.values()]

plt.subplot(1,2,1)
nx.draw(G1, node_color=node_colors1 ,with_labels = True, font_color = "white")
plt.subplot(1,2,2)
nx.draw(G2, node_color=node_colors2, with_labels = True, font_color = "white")

plt.show()
GM = nx.isomorphism.GraphMatcher(G1, G2)
GM.is_isomorphic()
list_matching = GM.mapping
print(list_matching)

f = open("Matching.txt", "w")
for i in list_matching:
    f.write(str(i) + " -> " + str(list_matching[i]))
    f.write("\n")
f.close()


    

