import random
def game_environment():
    list_of_darkness_creatures = ["Orc", "Goblin", "Uruk-hai", "Nazgul", "Balrog", "Shelob", "Troll", "Warg", "Giant Spider", "Gollum", "Sauron", "Saruman", "Witch-king of Angmar", "Grishnakh", "Lurtz", "Gothmog", "Gorbag", "Shagrat", "Snaga", "Grima Wormtongue", "Mouth of Sauron", "Khamul", "Gothmog"]
    ring_power = 100
    steps_to_mordor = 0
    total_steps_to_mordor = 17000
    step_per_mile = total_steps_to_mordor/17000
    proximity_to_darkness_creature = total_steps_to_mordor/500



def carry_ring(bearer_name):
    return f"{bearer_name} carries the One Ring."




print(carry_ring())

def form_fellowship(warrior,wizard, elf, dwarf, hobbit):
    return f"The Fellowship is formed with {warrior}, {wizard}, {elf}, {dwarf}, and {hobbit}."


locations = ["Moria", "Lothlorien", "Rivendell", "Mordor", "Isengard", "Minas Tirith", "Helm's Deep", "The Shire", "Mount Doom", "Fangorn Forest"]

for location in locations:
    if location == "Moria":
        print(f"Danger! The Followship of the Ring faces trouble in {location}!")
    else:
        print(f"The Fellowship of the Ring travels safely through {location}.")

game_environment.ring_power = 100
steps_to_mordor = 0


while game_environment.ring_power > 0:
    print(f"The Ring's power is at {game_environment.ring_power}.")
    game_environment.ring_power -= 10
    steps_to_mordor += 1

print(f"The Ring's power is at {game_environment.ring_power}.")
print(f"After {steps_to_mordor} steps, the Fellowship of the Ring has yet to reach Mordor.")


