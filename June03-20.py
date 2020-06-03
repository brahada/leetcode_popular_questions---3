class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
            costs.sort(key=lambda cost: cost[0] - cost[1])
            costA = sum([cost[0] for cost in costs[:len(costs) // 2]])
            costB = sum([cost[1] for cost in costs[len(costs) // 2:]])
            return costA + costB
