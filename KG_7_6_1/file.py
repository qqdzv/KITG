class Graph:
    """
    Класс для представления графа и нахождения его компонент связности с помощью поиска в глубину (DFS).
    """

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """
        Добавляет ребро между двумя вершинами u и v. Если граф не содержит вершины,
        она автоматически добавляется.

        Аргументы:
        u, v -- вершины графа
        """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        if v not in self.graph[u]:  # Учитываем только уникальные ребра
            self.graph[u].append(v)
        if u not in self.graph[v]:  # Для неориентированного графа
            self.graph[v].append(u)

    def _dfs(self, v, visited, component):
        """
        Вспомогательный метод для выполнения поиска в глубину (DFS).

        Аргументы:
        v -- текущая вершина
        visited -- множество посещенных вершин
        component -- текущая компонента связности
        """
        visited.add(v)
        component.append(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, component)

    def connected_components(self):
        """
        Находит все компоненты связности в графе с использованием DFS.

        Возвращает:
        list[list[int]] -- список компонент связности
        """
        visited = set()
        components = []
        for vertex in self.graph:
            if vertex not in visited:
                component = []
                self._dfs(vertex, visited, component)
                components.append(sorted(component))  # Сортируем для удобства проверки
        return components

    def __str__(self):
        """
        Представляет граф в виде строки.

        Возвращает:
        str -- строка с ребрами графа
        """
        result = "Граф:\n"
        for key in self.graph:
            result += f"{key} -> {self.graph[key]}\n"
        return result


# Тесты
def test_connected_components():
    """
    Тесты для проверки работы алгоритма построения компонент связности.
    """
    # Тест 1: Граф с несколькими компонентами связности
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(3, 4)
    assert sorted(g1.connected_components()) == sorted([[0, 1, 2], [3, 4]]), "Test 1 Failed"

    # Тест 2: Граф с одной компонентой связности
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 2)
    assert g2.connected_components() == [[0, 1, 2]], "Test 2 Failed"

    # Тест 3: Пустой граф
    g3 = Graph()
    assert g3.connected_components() == [], "Test 3 Failed"

    # Тест 4: Граф с одной вершиной
    g4 = Graph()
    g4.add_edge(0, 0)  # Петля
    assert g4.connected_components() == [[0]], "Test 4 Failed"

    # Тест 5: Граф с многократными рёбрами между вершинами
    g5 = Graph()
    g5.add_edge(0, 1)
    g5.add_edge(0, 1)  # Дублирующееся ребро
    g5.add_edge(1, 2)
    assert g5.connected_components() == [[0, 1, 2]], "Test 5 Failed"

    print("Все тесты прошли успешно!")


# Пример использования
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(5, 6)

    print(g)  # Вывод графа
    components = g.connected_components()
    print("Компоненты связности:", components)

    test_connected_components()
