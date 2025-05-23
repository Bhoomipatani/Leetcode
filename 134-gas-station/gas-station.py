class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1