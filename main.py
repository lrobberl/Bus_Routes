"""
815. Bus Routes
https://leetcode.com/problems/bus-routes/description/
"""
import networkx as netxlib

best_path_steps = 501
routes = [[1,2,3],[3,5,7],[8,5,9],[10,3,2,7]]
S = 1       # start stop
T = 10       # end stop
G = netxlib.Graph()


def depth_visit(G, v, actual_node, actual_path):
    """
    :param G: graph
    :param v: list containing for each cell 0/1 indicating if the i-th node has been visited or not
    :param actual_node: node that is now examined
    :param actual_path: length of the path obtained to this point
    :return: nothing
    """
    # if the actual path is longer than the best one, backtrack the search
    global best_path_steps
    if actual_path >= best_path_steps:
        return

    # terminal case, if the destination is reached
    if T in routes[actual_node]:
        # if we found a better path, update best path length
        best_path_steps = actual_path
        return

    # if the starting stop is found along the path, this means we will be able to surely find a better path
    # starting from this node, so we return, immediately stopping the research in this breanch, since that node
    # will be a starting point of our path in the next iterations
    if S in routes[actual_node] and actual_path != 1:
        return

    # cycle through each neighbor
    for neighbor in G[actual_node]:
        # if the neighbor hasn't been visited yet, do so
        if v[neighbor] == 0:
            actual_path += 1
            v[neighbor] = 1
            depth_visit(G, v, neighbor, actual_path)
            v[neighbor] = 0
            actual_path -= 1


# add nodes to the graph
i = 0
visited = [0] * len(routes)
for route in routes:
    G.add_node(i, visited=0)
    i += 1

# add all edges
for node1 in G.nodes:
    for node2 in G.nodes:
        # try to add a new edge only if the nodes are not the same
        if node1 != node2:
            for stop1 in routes[node1]:
                if stop1 in routes[node2]:
                    G.add_edge(node1, node2)
                    break

# for all the nodes
for node in G:
    # if the starting stop is in the analyzed node
    if S in routes[node]:
        visited[node] = 1
        depth_visit(G, visited, node, 1)
        visited[node] = 0

print("To go from %d to %d the best solution is to take %d buses" % (S, T, best_path_steps))
