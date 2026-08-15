class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visited = set()
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[b].append(a)

        def dfs(course):
            if course in visiting:
                return False # a cycle
            if course in visited:
                return True # explored this course 

            visiting.add(course)
         
            for nei in adj_list[course]:
                if not dfs(nei):
                    return False    
            visiting.remove(course)
            visited.add(course)  
            return True   


            

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

                

        
        