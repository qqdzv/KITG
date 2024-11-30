class UnionFind:
    """
    Класс Union-Find (объединить-найти) для управления группами объектов.
    Поддерживает операции объединения и поиска с использованием оптимизаций:
    - Сжатие пути: ускоряет операцию find().
    - Учет рангов: минимизирует высоту дерева при объединении.
    """

    def __init__(self, size):
        """
        Инициализирует Union-Find для заданного количества элементов.

        Аргументы:
        size -- количество элементов в структуре
        """
        self.parent = list(range(size))  # Каждый элемент — свой родитель
        self.rank = [0] * size  # Ранги всех деревьев изначально равны 0

    def find(self, p):
        """
        Находит корневой элемент (представителя) множества, которому принадлежит элемент p.
        Использует сжатие пути для оптимизации.

        Аргументы:
        p -- элемент для поиска

        Возвращает:
        int -- представитель множества
        """
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Сжатие пути
        return self.parent[p]

    def union(self, p, q):
        """
        Объединяет множества двух элементов p и q.

        Аргументы:
        p, q -- элементы для объединения
        """
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return  # Они уже в одном множестве

        # Объединяем деревья по рангу
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

    def connected(self, p, q):
        """
        Проверяет, находятся ли два элемента в одном множестве.

        Аргументы:
        p, q -- элементы для проверки

        Возвращает:
        bool -- True, если элементы в одном множестве, иначе False
        """
        return self.find(p) == self.find(q)

    def groups(self):
        """
        Возвращает текущие группы элементов.

        Возвращает:
        dict -- словарь, где ключи — представители, а значения — элементы группы
        """
        groups = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        return groups


# Тесты
def test_union_find():
    """Тест базовых операций union-find."""
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 3)
    assert uf.connected(1, 4)  # Все элементы объединены
    assert not uf.connected(1, 5)  # 5 не связано с остальными
    print("Базовые тесты прошли успешно")


def test_large_union_find():
    """Тест на производительность для большого количества элементов."""
    import time
    uf = UnionFind(100000)
    start_time = time.time()
    for i in range(1, 100000):
        uf.union(i, i - 1)
    end_time = time.time()
    print(f"Объединение 100000 элементов выполнено за {end_time - start_time:.2f} секунд")


def visualize_groups(uf):
    """Печатает текущие группы."""
    print("Текущие группы:", uf.groups())


# Основной блок
if __name__ == "__main__":
    uf = UnionFind(10)
    test_union_find()
    visualize_groups(uf)

    # Проверка большого графа
    test_large_union_find()
