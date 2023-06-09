# 깊이 우선
# 동작원리: 스택
# 구현 방법: 재귀 함수 이용
# DFS 메서드 정의
def dfs(graph, v, visted):
    # 현재 노드를 방문 처리
    visted[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visted[i]:
            dfs(graph, i, visted)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

dfs(graph, 1, visited)
