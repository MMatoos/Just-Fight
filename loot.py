import weapons
import classes

small_animal = ['hide', 'claws', 'teeth']
weapons = [weapons.claws, weapons.mace, weapons.sword, weapons.magic_staff]

hide = classes.Item()
hide.name = "Hide"
hide.type = "craft" #tablice jesli ma wiecej niz jeden typ
hide.price = 1

claws = classes.Item()
claws.name = "Claws"
claws.type = "weapon"
claws.price = 2

teeth = classes.Item()
teeth.name = "Teeth"
claws.type = "miscellaneous"
teeth.price = 0

