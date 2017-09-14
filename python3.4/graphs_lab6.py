

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

    def add_edge(self, node, nodebis):
        """
        :param node: first node of new edge
        :param nodebis: second node of edge
        :return:
        """
        try:
            self.list_neighbor[node].append(nodebis)
        except:
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(nodebis)
        try:
            self.list_neighbor[nodebis].append(node)
        except:
            self.list_neighbor[nodebis] = []
            self.list_neighbor[nodebis].append(node)

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

    def delete_edge(self, node, nodebis):
        """
        Function deletes edge node->nodebis and nodebis->edge
        :param node: node of start of edge
        :param nodebis: node of end of edge
        :return: None
        """
        self.list_neighbor[node].remove(nodebis)
        self.list_neighbor[nodebis].remove(node)

    def delete_node(self, node):
        """
        This function deletes node by its name
        :param node: node to delete
        :return: None
        """
        del self.list_node[node]
        try:
            for nodebis in self.list_neighbor[node]:
                self.list_neighbor[nodebis].remove(node)
            del self.list_neighbor[node]
        except:
            return "error"

    def cycles(self):
        """
        Function that finds almost all cycles in graph
        :return: list of cycle lists
        """
        was_here = {}  #list of nodes, we passed
        cycles = []    #list of cycles
        tree = {}      #tree for building edges between nodes - where current node can go

        def find_cycle(node, prev):
            """
            Find cycle from current node to previous node in cycle.
            :return: list of nodes in cycle
            """
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
            """
            DFS algorithm - search in depth
            """
            was_here[node] = True
            neighbour_list = self.neighbors(node)
            for each in neighbour_list:
                if each not in was_here:
                    tree[each] = node
                    dfs(each)
                else:
                    if tree[node] != each:
                        cycle = find_cycle(node, each)
                        if len(cycle):
                            cycles.append(cycle)

        for each in list(self.nodes()):
            if each not in was_here:
                tree[each] = None
                dfs(each)
        return cycles

    def cycle_check(self):
        if len(self.cycles()):
            return True
        else:
            return False

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


    #var 3
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(7, 4)
    G.add_edge(5, 8)
    G.add_edge(5, 6)
    G.add_edge(6, 9)
    G.add_edge(9, 10)


    #var 2
    """
    G.add_edge(1, 4)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(5, 8)
    G.add_edge(6, 9)
    G.add_edge(7, 10)
    G.add_edge(8, 9)
    G.add_edge(9, 10)
    """


    #var 1
    """
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(3, 9)
    G.add_edge(5, 4)
    G.add_edge(6, 9)
    G.add_edge(7, 10)
    G.add_edge(8, 9)
    G.add_edge(9, 10)

    """

   # many cycles
    """
    G.add_edge(1, 5)
    G.add_edge(1, 2)
    G.add_edge(1, 6)
    G.add_edge(2, 7)
    G.add_edge(3, 7)
    G.add_edge(3, 4)
    G.add_edge(4, 8)
    G.add_edge(5, 9)
    G.add_edge(6, 7)
    G.add_edge(7, 10)
    G.add_edge(8, 10)
    G.add_edge(9, 10)
    """
    print(G.cycles())
    print(G.cycle_check())