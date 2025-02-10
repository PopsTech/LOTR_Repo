# Stats
# Predefined statistical categories for Lord of the Rings character classes.
#Character Level will be determinate of character_stat_category * multiplier

import random #for randomly generating statistics
import pandas as pd #for data manipulation

# Define level range
CHARACTER_LEVEL_MAX = 100
CHARACTER_LEVEL_MIN = 1

# Define base character stats
character_stat_category = {
    'Strength': 10,    # Physical power and melee damage
    'Agility': 8,      # Speed and dexterity
    'Cunning': 7,      # Stealth and tactical ability
    'Wisdom': 9,       # Magic power and resistance
    'Endurance': 6,    # Health and stamina
    'Leadership': 5,   # Party buffs and morale
    'Brutality': 12    # Critical damage and intimidation
}

# Create level progression
character_levels = range(CHARACTER_LEVEL_MIN, CHARACTER_LEVEL_MAX + 1)

# Create empty array to store character stats data
stats_data = []

# Generate stats for each level
for level in character_levels:
    level_stats = {}
    level_stats['Level'] = level
    for stat, base_value in character_stat_category.items():
        stats_multiplier = random.uniform(1.0, 1.5)
        level_stats[stat] = base_value * stats_multiplier * (level / CHARACTER_LEVEL_MAX)
    stats_data.append(level_stats)

df_stats = pd.DataFrame(stats_data)

print(df_stats.head(100))