import pygame as pg
import random

hero_stand = [pg.image.load('images/stand1.png'), pg.image.load('images/stand2.png'),
              pg.image.load('images/stand3.png')]
hero_attack = [pg.image.load('images/attack0.png'), pg.image.load('images/attack1.png'),
               pg.image.load('images/attack2.png'), pg.image.load('images/attack3.png'),
               pg.image.load('images/attack4.png'), pg.image.load('images/attack5.png'),
               pg.image.load('images/attack6.png'), pg.image.load('images/attack7.png'),
               pg.image.load('images/attack8.png'), pg.image.load('images/attack9.png'),
               pg.image.load('images/attack10.png'), pg.image.load('images/attack11.png'),
               pg.image.load('images/attack12.png'), pg.image.load('images/attack13.png'),
               pg.image.load('images/attack14.png'), pg.image.load('images/attack15.png'),
               pg.image.load('images/attack16.png')]
hero_sp_attack = [pg.image.load('images/fire1.png'), pg.image.load('images/fire2.png'),
                  pg.image.load('images/fire3.png'), pg.image.load('images/fire4.png'),
                  pg.image.load('images/fire5.png')]
hero_defend = [pg.image.load('images/crouch1.png'), pg.image.load('images/crouch2.png'),
               pg.image.load('images/crouch3.png'), pg.image.load('images/crouch4.png')]
enemy_stand = [pg.image.load('images/tile000.png'), pg.image.load('images/tile001.png'),
               pg.image.load('images/tile002.png'), pg.image.load('images/tile003.png'),
               pg.image.load('images/tile004.png'), pg.image.load('images/tile005.png'),
               pg.image.load('images/tile006.png'), pg.image.load('images/tile007.png'),
               pg.image.load('images/tile008.png'), pg.image.load('images/tile009.png'),
               pg.image.load('images/tile010.png')]

transform = lambda x, y, sprite : pg.transform.scale(sprite, (x, y))
for i in range(3):
    hero_stand[i] = transform(150, 111, hero_stand[i]) 
stand_count = 0
for i in range(17):
    hero_attack[i] = transform(150, 111, hero_attack[i])
attack_count = 0
for i in range(5):
    hero_sp_attack[i] = transform(300, 222, hero_sp_attack[i])
sp_attack_count = 0
for i in range(4):
    hero_defend[i] = transform(150, 111, hero_defend[i])
defend_count = 0
for i in range(11):
    enemy_stand[i] = transform(160, 120, enemy_stand[i])
enemy_stand_count = 0


class Character():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_hp = 100
        self.hp = 100
        self.weapon = Weapon()
        self.status = True
        self.standing = True
        self.attacking = False
        self.sp_attacking = False
        self.defending = False

    def attack(self, weapon):
        damage = random.randint((weapon.minimum_damage-1), weapon.maximum_damage)
        return damage


class Hero(Character):
    def __init__(self, x, y, width, height):
        Character.__init__(self, x, y, width, height)

    def sp_attack(self):
        if random.randint(0, 10) <= 5:
            return random.randint(29, 40)
        else:
            return 0

    def defend(self):
        if random.randint(0,100) <= 65:
            return True
        else:
            return False

    def draw(self, win):
        global stand_count
        global attack_count
        global sp_attack_count
        global defend_count
        if stand_count + 1 >= 9:
            stand_count = 0
        if attack_count + 1 >= 51:
            attack_count = 0
        if sp_attack_count + 1 >= 15:
            sp_attack_count = 0
        if defend_count + 1 >= 12:
            defend_count = 0
        blit_anim = lambda x, y, count, sprite : win.blit(sprite[count//3], (x, y))
        if self.standing:
            #win.blit(hero_stand[stand_count//3], (self.x, self.y))
            blit_anim(self.x, self.y, stand_count, hero_stand)
            stand_count += 1
        elif self.attacking:
            blit_anim(self.x, self.y, attack_count, hero_attack)
            attack_count += 1
        elif self.sp_attacking:
            blit_anim(self.x-70, self.y-111, sp_attack_count, hero_sp_attack)
            sp_attack_count += 1
            blit_anim(self.x, self.y, attack_count, hero_attack)
            attack_count += 1
        elif self.defending:
            blit_anim(self.x, self.y, defend_count, hero_defend)
            defend_count += 1



        # win.blit(hero_right, (self.x, self.y))


class Monster(Character):

    def __init__(self, x, y, width, height):
        Character.__init__(self, x, y, width, height)
        self.loot_type = Item().type[0]

    def attack(self, weapon):
        damage = random.randint((weapon.minimum_damage-1), weapon.maximum_damage) - 1
        return damage

    def loot(self, loot_type):
        return random.choice(loot_type)

    def draw(self, win):
        blit_anim = lambda x, y, count, sprite : win.blit(sprite[count//3], (x, y))
        global enemy_stand_count
        if enemy_stand_count + 1 >= 33:
            enemy_stand_count = 0
        blit_anim(self.x, self.y, enemy_stand_count, enemy_stand)
        enemy_stand_count += 1



class Item():

    def __init__(self):
        self.name = "Stick"
        self.type = ["miscellaneous", "weapon", "book", "craft"]
        self.price = 0

    def get_name(self):
        return self.name


class Weapon(Item):

    def __init__(self):
        Item.__init__(self)
        self.minimum_damage = 0
        self.maximum_damage = 10