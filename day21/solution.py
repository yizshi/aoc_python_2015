#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in")
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

weapons = [
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0],
]

armor = [
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 5],
    [102, 0, 5],
]

rings = [
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3],
]

player = {
    "hp": 100,
    "damage": 4,
    "armor": 0,
}

boss = {
    "hp": 104,
    "damage": 8,
    "armor": 1,
}

def day21_part1():
    total_gold = 8
    while battle(player, boss):
        min_gold = 200
        min_weapons = weapons[0][0]
        min_armor = armor[0][0]
        min_ring = rings[0][0]
        
        new_weapon = weapons.pop()
        player["damage"] = new_weapon[1]
        total_gold = total_gold + new_weapon[0]
    print(total_gold)
    return 0

def day21_part2():
    return 0

def battle(player, boss):
    boss_round = boss["hp"] // (player["damage"] - boss["armor"])
    player_round = player["hp"] // (boss["damage"] - player["armor"])
    if boss_round > player_round:
        return False
    else:
        return True
