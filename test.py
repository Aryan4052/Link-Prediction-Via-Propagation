import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('dataset/dataset.txt',delimiter=' ',create_using=nx.DiGraph(),nodetype=int)
print(nx.info(g))
#unconnected = list(nx.isolates(g))
#print(unconnected)

g1Edges = g.edges()
edge1 = []
edge2 = []
count = 0
count1 = 0
for a in g.nodes():
    count1 = 0
    for b in g.nodes():
        if count1 < 5 and a != b and (a,b) not in g1Edges:
            print("sho == "+str(nx.dijkstra_path(g,a,b)))
            edge1.append(a)
            edge2.append(b)
            print(str(a)+" "+str(b))
            count = count + 1
            count1 = count1 + 1
    if count > 20:
        break

def commonInfluenceSet(a, b):
    size = 0
    count = 0
    if len(a) > len(b):
        size = len(a)
    else:
        size = len(b)
    dup = []    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and a[i] not in dup:
                count = count + 1
        if a[i] not in dup:
            dup.append(a[i])        
    sim_score = 0
    if count > 0:
        sim_score = count/size
    a_set = set(a) 
    b_set = set(b) 
    return a_set & b_set, sim_score

pos = nx.spring_layout(g)    
betCent = nx.betweenness_centrality(g, normalized=True, endpoints=True)
cis = sorted(betCent, key=betCent.get, reverse=True)[:7]
print(cis)

node_color = [20000.0 * g.degree(v) for v in g]
node_size =  [v * 10000 for v in betCent.values()]

plt.figure(figsize=(20,20))
nx.draw_networkx(g, pos=pos, with_labels=True,
                 node_color=node_color,
                 node_size=node_size )
#plt.axis('off')
plt.show()

for i in range(len(edge1)):
    e1 = edge1[i]
    e2 = edge2[i]
    common1 = sorted(nx.all_neighbors(g, e1))
    common2 = sorted(nx.all_neighbors(g, e2))
    com,score = commonInfluenceSet(common1,common2)
    print(str(e1)+" "+str(e2)+" "+str(com)+" "+str(common1)+" "+str(common2)+" "+str(score))
                        
