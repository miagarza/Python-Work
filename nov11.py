



queue= deque[(start)]
distance[start]=0
parent[start]=None
order=[]



#while loop
while queue:
    current=queue.popleft()
    order.append(current)

    #visit the adj list of the vertex removed
    for neighbor in self.adj[current]:
        if distance[neighbor] is None:
            distance[neightbor]=distance[current]+1
            parent[neighbor]=current
            queue.append(neighbor)

print("Vertex, Distance, Parent")

for vertex in self.adj:
    print(vertex, ", ", distance[vertex], ", ", parent[vertex])