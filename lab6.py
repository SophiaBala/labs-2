def dijkstra(start, graph, nodes):
    distance = [float('inf')] * (nodes + 1)
    visited = [False] * (nodes + 1)
    distance[start] = 0

    for i in range(nodes):
        min_node = -1
        min_distance = float('inf')
        for node in range(1, nodes + 1):
            if not visited[node] and distance[node] < min_distance:
                min_distance = distance[node]
                min_node = node

        if min_node == -1:
            break

        visited[min_node] = True

        for neighbor, weight in graph[min_node]:
            if not visited[neighbor]:
                new_distance = distance[min_node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance

    return distance

def find_best_server(nodes, client_nodes, connections):
    graph = [[] for i in range(nodes + 1)]
    for u, v, delay in connections:
        graph[u].append((v, delay))
        graph[v].append((u, delay))

    best_max_delay = float('inf')
    clients = set(client_nodes)

    for candidate in range(1, nodes + 1):
        if candidate in clients:
            continue

        distances = dijkstra(candidate, graph, nodes)

        max_delay = max([distances[client] for client in client_nodes])

        if max_delay < best_max_delay:
            best_max_delay = max_delay

    return int(best_max_delay)


with open("gamsrv.in.txt", "r") as file:
    n, m = map(int, file.readline().split())
    clients = list(map(int, file.readline().split()))
    connections = []

    for i in range(m):
        u, v, latency = map(int, file.readline().split())
        connections.append((u, v, latency))


result = find_best_server(n, clients, connections)

with open("gamsrv.out", "w") as file:
    file.write(str(result) + "\n")
