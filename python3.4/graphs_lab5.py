
class Graph:
    def __init__(self):
        self.list_neighbor = {}
        self.list_node = {}

    def add_node(self, node):
        """
        Creating node and adding it to graph
        :param node: new node
        :return: None
        """
        self.list_node[node] = True

    def add_edge(self, node, node2):
        """
        :param node: node of start of new edge
        :param node2: node of end of edge
        :return:
        """
        try:
            self.list_neighbor[node].append(node2)
        except:
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(node2)

    def neighbors(self, node):
        """
        :param node: node of start of edges
        :return: list of neighbour nodes to node
        """
        try:
            return self.list_neighbor[node]
        except:
            return []

    def nodes(self):
        """
        :return: list of nodes in directed graph
        """
        return self.list_node.keys()

    def delete_edge(self, node, node2):
        """
        Function deletes edge node->node2
        :param node: node of start of edge
        :param node2: node of end of edge
        :return: None
        """
        self.list_neighbor[node].remove(node2)

    def delete_node(self, node):
        """
        This function deletes node by its name
        :param node: node to delete
        :return: None
        """
        try:
            del self.list_node[node]
            del self.list_neighbor[node]
        except:
            return "error"

    def common_friends(self, node1, node2):
        """
        :param node1: first node
        :param node2: second node
        :return: list of common friends of two nodes
        """
        return list(set(G.neighbors(node1)) & set(G.neighbors(node2)))

    def common_friends_second_order(self, node1, node2):
        """
        :param node1: first node
        :param node2: second node
        :return: list of common friends of friends of node1 and node2
        """
        #get list of all friends of all friends of node1
        for_node_1 = list()
        for i in self.neighbors(node1):
            for_node_1.extend(self.neighbors(i))
        #get list of all friends of all friends of node2
        for_node_2 = list()
        for i in self.neighbors(node2):
            for_node_2.extend(self.neighbors(i))
        #for_node_1 = [self.neighbors(i) for i in self.neighbors(node1)]
        #for_node_2 = [self.neighbors(i) for i in self.neighbors(node2)]
        return list(set(for_node_1) & set(for_node_2))

    """
    def cycle_check(self):
        was_here = {}
        cycles = []
        tree = {}

        def find_cycle(node, prev):
            cycle = []
            while node != prev:
                if node is None:
                    return []
                cycle.append(node)
                node = tree[node]
            cycle.append(node)
            cycle.reverse()
            return cycle

        def dfs(node):
            was_here[node] = True
            neighbour_list = self.neighbors(node)
            for each in neighbour_list:
                if each not in was_here:
                    tree[each] = node
                    dfs(each)
                else:
                    if tree[node] != each:
                        cycles.extend(find_cycle(node, each))

        for each in list(self.nodes()):
            if each not in was_here:
                tree[each] = None
                dfs(each)
        return cycles
    """

if __name__ == "__main__":
    G = Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)

    G.add_node(7)
    G.add_node(8)
    G.add_node(9)
    G.add_node(10)
    G.add_edge(1, 5)
    G.add_edge(1, 4)
    G.add_edge(1, 3)
    G.add_edge(2, 5)
    G.add_edge(2, 6)
    G.add_edge(2, 4)
    G.add_edge(3, 7)
    G.add_edge(4, 8)
    G.add_edge(5, 7)
    G.add_edge(5, 9)
    G.add_edge(6, 10)
    """
    #print(list(G.nodes()))
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(4, 2)
    G.add_edge(3, 5)
    G.add_edge(5, 4)
    G.add_edge(5, 6)
    """
    print(G.common_friends(1, 2))
    print(G.common_friends_second_order(1, 2))
