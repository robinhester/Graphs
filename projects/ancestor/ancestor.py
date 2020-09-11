from graph.graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for vertex_1, vertex_2 in ancestors:
        graph.add_vertex(vertex_1)
        graph.add_vertex(vertex_2)
        # add edges
    for vertex_1, vertex_2 in ancestors:
        graph.add_edge(vertex_1, vertex_2)

    targetVertex = None
    longestPath = 1
    for vertex in graph.vertices:
        path = graph.dfs(vertex, starting_node)
        if path:
            if len(path) > longestPath:
                longestPath = len(path)
                targetVertex = vertex
        elif not path and longestPath == 1:
            targetVertex = -1

    return targetVertex