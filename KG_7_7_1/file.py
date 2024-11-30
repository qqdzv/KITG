from collections import deque

def bfs(graph, start):
    """
    Выполняет поиск в ширину (BFS) в заданном графе.

    Аргументы:
    graph -- словарь, представляющий граф (ключи — узлы, значения — списки соседей)
    start -- начальный узел для поиска

    Возвращает:
    distance -- словарь расстояний от начального узла до всех других узлов
    """
    # Проверка на пустой граф
    if not graph:
        raise ValueError("Граф не должен быть пустым")

    # Проверка, существует ли начальный узел
    if start not in graph:
        raise ValueError(f"Начальный узел '{start}' отсутствует в графе")

    visited = {node: False for node in graph}
    distance = {node: float('inf') for node in graph}
    queue = deque([start])
    
    visited[start] = True
    distance[start] = 0

    while queue:
        current = queue.popleft()
        print(f"Обработка узла: {current}")  # Лог для отслеживания процесса

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                print(f"Узел {neighbor} на расстоянии {distance[neighbor]}")
                queue.append(neighbor)
    
    return distance


import unittest

class TestBFS(unittest.TestCase):
    def test_linear_graph(self):
        """Тест линейного графа"""
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D'],
            'D': []
        }
        expected = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        self.assertEqual(bfs(graph, 'A'), expected)

    def test_cyclic_graph(self):
        """Тест циклического графа"""
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        expected = {'A': 0, 'B': 1, 'C': 2}
        self.assertEqual(bfs(graph, 'A'), expected)

    def test_disconnected_graph(self):
        """Тест несвязного графа"""
        graph = {
            'A': ['B'],
            'B': [],
            'C': ['D'],
            'D': []
        }
        expected = {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')}
        self.assertEqual(bfs(graph, 'A'), expected)

    def test_empty_graph(self):
        """Тест пустого графа"""
        graph = {}
        with self.assertRaises(ValueError):
            bfs(graph, 'A')

    def test_missing_start_node(self):
        """Тест с отсутствующим стартовым узлом"""
        graph = {'A': ['B'], 'B': ['C']}
        with self.assertRaises(ValueError):
            bfs(graph, 'Z')


if __name__ == "__main__":
    unittest.main()
