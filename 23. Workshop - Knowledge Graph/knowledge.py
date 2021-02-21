from suggestions import Suggestions


class KnowledgeGraph:
    MAX_DEPTH = 2

    def __init__(self, term):
        self.__term = term
        self.__nodes = [term]
        self.__edges = []
        self.__build_graph(term)

    @property
    def nodes(self):
        return self.__nodes

    @property
    def edges(self):
        return self.__edges

    def __build_graph(self, term, depth=0):
        if depth == self.MAX_DEPTH:
            return

        suggestions = Suggestions(term).get_suggestions()

        for suggestion in suggestions:
            if not suggestion.count(' vs ') == 1:
                continue

            first_word, second_word = suggestion.split(' vs ')
            if second_word not in self.__nodes:
                self.__nodes.append(second_word)
                edge = (first_word, second_word)
                if edge not in self.__edges and tuple(reversed(edge)) not in self.__edges:
                    self.__edges.append(edge)

                self.__build_graph(second_word, depth=depth+1)


if __name__ == '__main__':
    graph = KnowledgeGraph('python')
    print(graph.nodes)
    print(graph.edges)


