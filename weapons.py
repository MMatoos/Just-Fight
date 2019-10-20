import classes

mace = classes.Weapon()
mace.name = "Mace"
mace.minimum_damage = 10
mace.maximum_damage = 20

sword = classes.Weapon()
sword.name = "Sword"
sword.minimum_damage = 5
sword.maximum_damage = 25

magic_staff = classes.Weapon()
magic_staff.name = "Magic Staff"
magic_staff.minimum_damage = 0
magic_staff.maximum_damage = 40

claws = classes.Weapon()
claws.name = "Claws"
claws.minimum_damage = 5
claws.maximum_damage = 15

stick = classes.Weapon()
stick.name = "Stick"
stick.minimum_damage = 1000
stick.maximum_damage = 5000

bow = classes.Weapon()
bow.name = "Bow"
bow.minimum_damage = 15
bow.maximum_damage = 15

player_weapons = [mace, sword, magic_staff, stick, bow]
