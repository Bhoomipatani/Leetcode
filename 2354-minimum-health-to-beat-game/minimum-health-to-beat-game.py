class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxdamage=0
        totaldamage=0
        for i in range(len(damage)):
            totaldamage+=damage[i]
            maxdamage=max(maxdamage,damage[i])
                
        return totaldamage-min(armor,maxdamage)+1