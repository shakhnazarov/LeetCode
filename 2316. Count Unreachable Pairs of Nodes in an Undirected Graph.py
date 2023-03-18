def dfs(graph, visited, now, component):
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            dfs(graph, visited, neigh, component)
    component.add(now)


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for v_1, v_2 in edges:
            graph[v_1].append(v_2)
            graph[v_2].append(v_1)

        visited = [False for _ in range(n)]

        components = []
        for i in range(n):
            if not visited[i]:
                component = set()
                dfs(graph, visited, i, component)
                components.append(component)

        ans = 0
        sum_all = sum([len(x) for x in components])
        for i, comp in enumerate(components):
            sum_all -= len(comp)
            ans += len(comp) * sum_all

        return ans