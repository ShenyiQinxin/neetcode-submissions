class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        stack = []

        for pos, speed in cars:
            time = (target-pos) / speed
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
         
        return len(stack)
                





        