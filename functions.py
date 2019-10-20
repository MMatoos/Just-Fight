import classes
import weapons
import time
import monsters
import loot
import messages as ms
import random


def attack(player, enemy, win):
    a = player.attack(player.weapon)
    enemy.hp -= a
    ms.smessage_display(win, 755, 525, "Player dealt "+str(a)+" damage!", 40)
    ms.hp_clear(win)
    if enemy.hp < 0:
        enemy.hp = 0
    hp_display(player, enemy, win)


def sp_attack(player, enemy, win):
    a = player.sp_attack()
    enemy.hp -= a
    if a > 0:
        ms.smessage_display(win, 755, 525, "Player dealt " + str(a) + " damage!", 40)
        ms.hp_clear(win)
        if enemy.hp < 0:
            enemy.hp = 0
        hp_display(player, enemy, win)
    else:
        ms.smessage_display(win, 755, 525, "Special attack failed!", 40)


def defend(player, win):
    d = player.defend()
    if d:
        ms.smessage_display(win, 755, 525, "Player is defending himself!", 40)
        return True
    else:
        ms.smessage_display(win, 755, 525, "Enemy broke the defense!", 40)
        return False


def laugh(win):
    laughs = ("LOSER", "POOR BABY", "PUPCIU", "FOOL", "DONKEY", "STUPID")
    ms.smessage_display(win, 755, 525, "Haha, you can't beat me "+random.choice(laughs)+"!", 40)


def hp_display(player, enemy, win):
    ms.smessage_display(win, 550, 525,"Player hp  "+str(player.hp), 40)
    ms.smessage_display(win, 550, 625, enemy.name+" hp  "+str(enemy.hp), 40)


def enemy_attack(player, enemy, win):
    a = enemy.attack(enemy.weapon)
    player.hp -= a
    ms.smessage_display(win, 755, 525, enemy.name+" dealt "+str(a)+" damage!", 40)
    ms.hp_clear(win)
    if player.hp < 0:
        player.hp = 0
    hp_display(player, enemy, win)

def enemy_attackh(player, enemy, win):
    a = (enemy.attack(enemy.weapon)//4)*3
    enemy.hp -= a
    ms.smessage_display(win, 755, 525, enemy.name + " attacked himself for "+str(a)+" damage!", 40)
    ms.hp_clear(win)
    if enemy.hp < 0:
        enemy.hp = 0
    hp_display(player, enemy, win)


def death_check(player, enemy):
    if player.hp <= 0:
        return 2
        # ms.message_display()
    elif enemy.hp <= 0:
        return 1
    else:
        return 0


def heal(player, type, win):
    heal_amount = lambda x: x * 5
    if type == 1:
        print(player.hp)
        player.hp += heal_amount(5)
        print(heal_amount(5))
        print(player.hp)
    elif type == 2:
        player.hp += heal_amount(10)
    elif type == 3:
        player.hp += heal_amount(15)
    ms.smessage_display(win, 755, 525, "You are healed now!", 40)


#################
# STRZAŁKI DO PRZEWIJANIA EKWIPUNKU LEWO PRAWO, PO SRODKU WYSWIETLA SIE FOTA I NAZWA + STATY
#################