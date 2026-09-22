class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for succ, pre in prerequisites:
            graph[succ].append(pre)

        can_finish, path = set(), set()
        def dfs(i):
            if i in can_finish:
                return True
            if i in path:
                return False
            
            path.add(i)
            for pre in graph[i]:
                if not dfs(pre):
                    return False
            path.remove(i)

            can_finish.add(i)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        