def Min_Latency_Path(graph, source, destination):
    """
    This function finds the path with the minimum latency in a graph.

    Parameters:
    graph (dict): A dictionary representing the network topology, where each key is a node and each value is a dictionary of its neighbors and their latencies
    source (str): The source node
    destination (str): The destination node

    Returns:
    list: The path with the minimum latency
    """

    min_latency = float('inf')
    min_path = []
    visited = set()

    def DFS(node, path, latency):
        nonlocal min_latency, min_path
        if node == destination:
            if latency < min_latency:
                min_latency = latency
                min_path = path
            return

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                DFS(neighbor, path + [neighbor], latency + graph[node][neighbor])

        visited.remove(node)

    DFS(source, [source], 0)

    return min_path
