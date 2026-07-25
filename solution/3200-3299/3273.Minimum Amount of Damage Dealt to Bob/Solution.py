class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:

        total_damage, damage_per_sec = 0, sum(damage)

        secs = map(lambda x: ceil(x/power), health)         # <-- 1)

        order = sorted(zip(damage, secs), 
                      key = lambda x: -x[0] / x[1])         # <-- 2)
        
        for enemy_damage, secs_to_kill in order:            # <-- 3)
            
            total_damage+= secs_to_kill * damage_per_sec
            damage_per_sec-= enemy_damage

        return total_damage                                 # <-- 4)
