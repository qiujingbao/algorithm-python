
class UnionFindQuickUnion(object):
    def __init__(self, N: int):
        """
        初始化并查集，初始化为-1，代表每个都是根结点
        当前结点指向的元素为父元素，例如3号元素的父亲为element[3]
        :param N: 元素的个数
        """
        self.count = N
        self.sets = N
        self.elements = []
        for i in range(0, N):
            self.elements.append(-1)

    def get_count(self) -> int:
        """
        返回当前元素个数
        :return:
        """
        return self.count

    def get_sets(self) -> int:
        """
        返回分量的个数
        :return:
        """
        return self.sets

    def is_connect(self, i: int, j: int) -> bool:
        """
        判断两个元素是否连通
        :param i: 第一个元素的索引
        :param j: 第二个元素的索引
        :return: 布尔值表示是否连通
        """
        if i > (self.count - 1) or j > (self.count - 1) or i < 0 or j < 0: return False  # 避免越界
        if self.find(i) == self.find(j):
            return True
        else:
            return False

    def find(self, i: int) -> int:
        """
        找到根结点，就是当前元素指向-1的元素
        :param i:
        :return:
        """
        if i < 0 or i > self.count - 1:
            return -2
        while self.elements[i] != -1:
            i = self.elements[i]
        return i

    def union(self, i: int, j: int) -> bool:
        """
        进行连接，两个连通分量。由j指向i
        :param i:
        :param j:
        :return:
        """
        if i > (self.count - 1) or j > (self.count - 1) or i < 0 or j < 0: return False  # 避免越界
        if self.is_connect(i, j): return True
        self.elements[i] = j  # i指向j
        self.sets = self.sets - 1

    def print_union(self) -> None:
        """
        采用dfs思想进行递归打印
        """
        flags = []
        for i in range(0, self.get_count()):
            flags.append(0)
        sets = self.get_sets()
        for i in range(0, sets):
            point = 0
            for j in range(0, self.get_count()):
                if self.elements[j] == -1 and flags[j] != 1:
                    point = j
                    print("\n集合：", end=" ")
                    print(str(j), end=" ")
                    flags[j] = 1
                    self.DFS(point, flags)

    def DFS(self, point, flags):
        """
        递归打印
        :param point: 当前欲访问结点
        :param flags: flags代指元素访问列表
        :return:
        """
        queen = []
        for i in range(self.get_count()):
            if self.elements[i] == point and flags[i] != 1:
                print(str(i), end=" ")
                flags[i] = 1
                queen.append(i)
        for i in range(0, len(queen)):
            self.DFS(queen[i], flags)
        return None


