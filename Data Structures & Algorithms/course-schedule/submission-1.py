class Solution:
    # successer course, prerequisite course
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        curr_path, finished = set(), set()

        def dfs(course):
            if course in curr_path:
                return False
            if course in finished:
                return True

            curr_path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            curr_path.remove(course)
            finished.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True





        