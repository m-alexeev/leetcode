from typing import List


def minimumHealth(damage: List[int], armor: int) -> int:
    total_dmg = 0
    max_attack = 0  # Track the highest attack

    for d in damage:
        total_dmg += d  # Accumulate total damage
        max_attack = max(max_attack, d)  # Update the highest attack seen so far

    # Apply armor to the highest attack (but not exceeding its value)
    total_dmg -= min(max_attack, armor)

    return total_dmg + 1  # +1 to ensure survival


print(minimumHealth([2, 7, 4, 3], 4))
print(minimumHealth([2, 5, 3, 4], 7))
print(minimumHealth([3, 3, 3], 0))
print(minimumHealth([5, 5, 5, 5], 5))
