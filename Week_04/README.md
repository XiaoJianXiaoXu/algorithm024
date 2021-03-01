学习笔记

# 深度优先搜索、广度优先搜索的实现和特性

搜索 - 遍历

* 每个节点都要访问一次
* 每个节点仅仅访问一次
* 对于节点的访问顺序不限
    * 深度优先： depth first search
    * 广度优先： breadth first search

### 深度优先：
···
# 二叉树
def dfs(node):
    if node is visited:
        # already visited
        return
    visited.add(node)

    # process current node
    # ... # logic here
    dfs(node.left)
    dfs(node.right)
···
···
# 多叉树
visited = set()
def dfs(node, visited):
    visited.add(node)
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
···

### 广度优先：
···
def BFS(graph, start, end):
    queue = []
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing work
    ...
···


### 贪心算法 Greedy
是一种在每一步选择中都采取在当前状态下最好或最优（最有利）的选择，从而希望导致结果是全局最好或最优的算法

贪心： 当下做局部最优判断
回溯： 能够回退
动态规划： 最优判断 + 回退


### 二分查找

前提：
1. 目标函数单调性（单调递增或者递减）
2. 存在上下界（bounded）
3. 能够通过索引访问

代码模板

left, right = 0, len(array)-1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    