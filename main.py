import pygame as pg
import interface
import time
import messages as ms
import classes
import monsters
import functions as fun
import weapons

pg.init()

win_w = 1280
win_h = 720
rect_but = ()
black = (0, 0, 0)
white = (255, 255, 255)

win = pg.display.set_mode((win_w, win_h))
pg.display.set_caption("Game")
clock = pg.time.Clock()

fight_background_img = pg.image.load('background.png')
menu_background_img = pg.image.load('menu_background.jpg')
alchemist_background_img = pg.image.load('doctor1.png')
inventory_background_img = pg.image.load('camp.png')
menu_background_img = pg.transform.scale(menu_background_img, (1280, 720))
alchemist_background_img = pg.transform.scale(alchemist_background_img, (1280, 720))

hx = 420
hy = 380
hero = classes.Hero(hx, hy, 150, 111)
hero.weapon = weapons.mace

opponent = monsters.skeleton
fight = False
end_fight = False
menu = True
win1 = False
alchemist = False
inventory = False


def use_attack():
    if hero.hp <= 0 or opponent.hp <= 0: return
    if (attack_button.clicked + sp_attack_button.clicked + defend_button.clicked + laugh_button.clicked) >= 1 and attack_button.used == 0:
        attack_button.clicked = 1
    elif attack_button.used == 0 and attack_button.clicked == 0:
        attack_button.clicked = 1
        attack_button.used = 1
        attack_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "Player is attacking!", 40)
    if attack_button.clicked == 1 and attack_button.used == 0:
        attack_button.clicked = 0


def use_sp_attack():
    if hero.hp <= 0 or opponent.hp <= 0: return
    if (attack_button.clicked + sp_attack_button.clicked + defend_button.clicked + laugh_button.clicked) >= 1 and sp_attack_button.used == 0:
        sp_attack_button.clicked = 1
    elif sp_attack_button.used == 0 and sp_attack_button.clicked == 0:
        sp_attack_button.clicked = 1
        sp_attack_button.used = 1
        sp_attack_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "Player is using special attack", 40)
    if sp_attack_button.clicked == 1 and sp_attack_button.used == 0:
        sp_attack_button.clicked = 0


def use_defend():
    if hero.hp <= 0 or opponent.hp <= 0: return
    if (attack_button.clicked + sp_attack_button.clicked + defend_button.clicked + laugh_button.clicked) >= 1 and defend_button.used == 0:
        defend_button.clicked = 1
    elif defend_button.used == 0 and defend_button.clicked == 0:
        defend_button.clicked = 1
        defend_button.used = 1
        defend_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "Player is preparing defend", 40)
    if defend_button.clicked == 1 and defend_button.used == 0:
        defend_button.clicked = 0


def use_laugh():
    if hero.hp <= 0 or opponent.hp <= 0: return
    if (attack_button.clicked + sp_attack_button.clicked + defend_button.clicked + laugh_button.clicked) >= 1 and laugh_button.used == 0:
        laugh_button.clicked = 1
    elif laugh_button.used == 0 and laugh_button.clicked == 0:
        laugh_button.clicked = 1
        laugh_button.used = 1
        laugh_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "Player is laughing", 40)
    if laugh_button.clicked == 1 and laugh_button.used == 0:
        laugh_button.clicked = 0


def go_menu():
    if end_fight:
        back_menu_button.clicked = 1
    elif alchemist:
        to_menu_button.clicked = 1
    elif inventory:
        to_menu_button.clicked = 1


def go_fight():
    fight_button.clicked = 1


def go_inventory():
    inventory_button.clicked = 1


def go_alchemist():
    alchemist_button.clicked = 1


def go_quit():
    quit_button.clicked = 1


def use_heal1():
    if (alch_heal1_button.clicked + alch_heal2_button.clicked + alch_heal3_button.clicked) >= 1 and alch_heal1_button.used == 0:
        alch_heal1_button.clicked = 1
    elif alch_heal1_button.used == 0 and alch_heal1_button.clicked == 0:
        alch_heal1_button.clicked = 1
        alch_heal1_button.used = 1
        alch_heal1_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "OK! I can heal you!", 40)
    if alch_heal1_button.clicked == 1 and alch_heal1_button.used == 0:
        alch_heal1_button.clicked = 0


def use_heal2():
    if (alch_heal1_button.clicked + alch_heal2_button.clicked + alch_heal3_button.clicked) >= 1 and alch_heal2_button.used == 0:
        alch_heal2_button.clicked = 1
    elif alch_heal2_button.used == 0 and alch_heal2_button.clicked == 0:
        alch_heal2_button.clicked = 1
        alch_heal2_button.used = 1
        alch_heal2_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "OK! I can heal you!", 40)
    if alch_heal2_button.clicked == 1 and alch_heal2_button.used == 0:
        alch_heal2_button.clicked = 0


def use_heal3():
    if (alch_heal1_button.clicked + alch_heal2_button.clicked + alch_heal3_button.clicked) >= 1 and alch_heal3_button.used == 0:
        alch_heal3_button.clicked = 1
    elif alch_heal3_button.used == 0 and alch_heal3_button.clicked == 0:
        alch_heal3_button.clicked = 1
        alch_heal3_button.used = 1
        alch_heal3_button.timex = time.time() + 2
        ms.smessage_display(win, 755, 525, "OK! I can heal you!", 40)
    if alch_heal3_button.clicked == 1 and alch_heal3_button.used == 0:
        alch_heal3_button.clicked = 0


attack_button = interface.Button(rect=(50, 525, 200, 75), text_button='ATTACK', use=use_attack)
sp_attack_button = interface.Button(rect=(275, 525, 200, 75), text_button='POWER', use=use_sp_attack)
defend_button = interface.Button(rect=(50, 625, 200, 75), text_button='DEFEND', use=use_defend)
laugh_button = interface.Button(rect=(275, 625, 200, 75), text_button='LAUGH', use=use_laugh)
back_menu_button = interface.Button(rect=(540,260, 200, 75), text_button='MENU', use=go_menu)
fight_button = interface.Button(rect=(540,240, 200, 75), text_button='ARENA', use=go_fight)
inventory_button = interface.Button(rect=(540, 315, 200, 75), text_button='INVENTORY', use=go_inventory)
alchemist_button = interface.Button(rect=(540, 385, 200, 75), text_button='ALCHEMIST', use=go_alchemist)
quit_button = interface.Button(rect=(540,460, 200, 75), text_button='QUIT', use=go_quit)
alch_heal1_button = interface.Button(rect=(50, 525, 200, 75), text_button='HERBS', use=use_heal1)
alch_heal2_button = interface.Button(rect=(275, 525, 200, 75), text_button='BANDAGE', use=use_heal2)
alch_heal3_button = interface.Button(rect=(50, 625, 200, 75), text_button='POTION', use=use_heal3)
to_menu_button = interface.Button(rect=(275, 625, 200, 75), text_button='LEAVE', use=go_menu)


def fight_update():
    win.blit(fight_background_img, (0, -200))
    hero.draw(win)
    opponent.draw(win)
    sp_attack_button.draw(win)
    attack_button.draw(win)
    defend_button.draw(win)
    laugh_button.draw(win)
    pg.display.update()

def end_fight_update():
    win.blit(fight_background_img, (0, -200))
    hero.draw(win)
    back_menu_button.draw(win)
    pg.display.update()

def menu_update():
    win.blit(menu_background_img, (0, 0))
    fight_button.draw(win)
    inventory_button.draw(win)
    alchemist_button.draw(win)
    quit_button.draw(win),
    pg.display.update()

def alchemist_update():
    win.blit(alchemist_background_img, (0, -200))
    alch_heal1_button.draw(win)
    alch_heal2_button.draw(win)
    alch_heal3_button.draw(win)
    to_menu_button.draw(win)
    pg.display.update()

def inventory_update():
    win.blit(inventory_background_img, (0, -30))
    to_menu_button.draw(win)
    pg.display.update()


a1 = True
a2 = True
a3 = True
a4 = True
hpdis = True
end = False
game_exit = False
astart = True
beg = True
while not game_exit:
    clock.tick(30)
   # print(pg.mouse.get_pos())

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

    if fight:
        attack_button.get_event(event)
        sp_attack_button.get_event(event)
        defend_button.get_event(event)
        laugh_button.get_event(event)

        if hpdis:
            fun.hp_display(hero, opponent, win)
            pg.mixer.music.load("fight.mp3")
            pg.mixer.music.play(-1)
            hpdis = False

        if attack_button.used == 1:
            if astart:
                hero.standing = False
                hero.attacking = True
                astart = False
            if attack_button.timex < time.time() and a1:
                ms.message_clear(win)
                a1 = False
            elif not a1 and a2 and hero.hp > 0:
                fun.attack(hero, opponent, win)
                attack_button.timex += 2
                a2 = False
            elif attack_button.timex < time.time() and not a2 and a3:
                hero.attacking = False
                hero.standing = True
                ms.message_clear(win)
                if opponent.hp > 0:
                    attack_button.timex += 2
                    ms.smessage_display(win, 755, 525, opponent.name + " is attacking!", 40)
                a3 = False
            elif attack_button.timex < time.time() and not a3 and a4:
                if opponent.hp > 0:
                    attack_button.timex += 2
                    ms.message_clear(win)
                    fun.enemy_attack(hero, opponent, win)
                a4 = False
            elif attack_button.timex < time.time() and not a4:
                attack_button.clicked = 0
                ms.message_clear(win)
                attack_button.used = 0
                a1=True
                a2=True
                a3=True
                a4=True
                astart=True
                if fun.death_check(hero, opponent) == 1 or fun.death_check(hero, opponent) == 2:
                    end = True

        if sp_attack_button.clicked == 1:
            if astart:
                hero.standing = False
                hero.sp_attacking = True
                astart = False
            if sp_attack_button.timex < time.time() and a1:
                ms.message_clear(win)
                a1 = False
            elif not a1 and a2 and hero.hp > 0:
                fun.sp_attack(hero, opponent, win)
                sp_attack_button.timex += 2
                a2 = False
            elif sp_attack_button.timex < time.time() and not a2 and a3:
                hero.sp_attacking = False
                hero.standing = True
                ms.message_clear(win)
                if opponent.hp > 0:
                    sp_attack_button.timex += 2
                    ms.smessage_display(win, 755, 525, opponent.name + " is attacking!", 40)
                a3 = False
            elif sp_attack_button.timex < time.time() and not a3 and a4:
                if opponent.hp > 0:
                    sp_attack_button.timex += 2
                    ms.message_clear(win)
                    fun.enemy_attack(hero, opponent, win)
                a4 = False
            elif sp_attack_button.timex < time.time() and not a4:
                sp_attack_button.clicked = 0
                ms.message_clear(win)
                sp_attack_button.used = 0
                a1=True
                a2=True
                a3=True
                a4=True
                astart = True
                if fun.death_check(hero, opponent) == 1 or fun.death_check(hero, opponent) == 2:
                    end = True

        if defend_button.clicked == 1:
            if astart:
                hero.standing = False
                hero.defending = True
                astart = False
            if defend_button.timex < time.time() and a1:
                ms.message_clear(win)
                a1 = False
            elif not a1 and a2 and hero.hp > 0:
                d = fun.defend(hero, win)
                defend_button.timex += 2
                a2 = False
            elif defend_button.timex < time.time() and not a2 and a3:
                hero.defending = False
                hero.standing = True
                ms.message_clear(win)
                if opponent.hp > 0:
                    defend_button.timex += 2
                    ms.smessage_display(win, 755, 525, opponent.name + " is attacking!", 40)
                a3 = False
            elif defend_button.timex < time.time() and not a3 and a4:
                if opponent.hp > 0:
                    defend_button.timex += 2
                    ms.message_clear(win)
                    if d:
                        fun.enemy_attackh(hero, opponent, win)
                    else:
                        fun.enemy_attack(hero, opponent, win)
                a4 = False
            elif defend_button.timex < time.time() and not a4:
                defend_button.clicked = 0
                ms.message_clear(win)
                defend_button.used = 0
                a1=True
                a2=True
                a3=True
                a4=True
                astart=True
                if fun.death_check(hero, opponent) == 1 or fun.death_check(hero, opponent) == 2:
                    end = True

        if laugh_button.clicked == 1:
            if laugh_button.timex < time.time() and a1:
                ms.message_clear(win)
                a1 = False
            elif not a1 and a2 and hero.hp > 0:
                fun.laugh(win)
                laugh_button.timex += 2
                a2 = False
            elif laugh_button.timex < time.time() and not a2 and a3:
                ms.message_clear(win)
                if opponent.hp > 0:
                    laugh_button.timex += 2
                    ms.smessage_display(win, 755, 525, opponent.name + " is attacking!", 40)
                a3 = False
            elif laugh_button.timex < time.time() and not a3 and a4:
                if opponent.hp > 0:
                    laugh_button.timex += 2
                    ms.message_clear(win)
                    fun.enemy_attack(hero, opponent, win)
                a4 = False
            elif laugh_button.timex < time.time() and not a4:
                laugh_button.clicked = 0
                ms.message_clear(win)
                laugh_button.used = 0
                a1=True
                a2=True
                a3=True
                a4=True
                if fun.death_check(hero, opponent) == 1 or fun.death_check(hero, opponent) == 2:
                    end = True

        if opponent.hp <= 0 or hero.hp <= 0:
            win.blit(fight_background_img, (0, -200))
            hero.draw(win)
            pg.display.update()
        if fun.death_check(hero, opponent) == 0:
            fight_update()
        if fun.death_check(hero, opponent) == 1 and end:
            ms.down_clear(win)
            ms.message_display(win, 0, 510, 1280, 210, "YOU WIN !!!", 150)
            pg.mixer.music.load("win.wav")
            pg.mixer.music.play(0)
            win1 = True
            fight = False
            end_fight = True
        elif fun.death_check(hero, opponent) == 2 and end:
            ms.down_clear(win)
            ms.message_display(win, 0, 510, 1280, 210, "YOU LOSE !!!", 150)
            fight = False
            end_fight = True

    if end_fight:
        back_menu_button.get_event(event)
        if back_menu_button.clicked == 1:
            menu = True
            end_fight = False
            beg = True
            end = False
            hpdis = True
            if win1:
                opponent = monsters.bandit
            back_menu_button.clicked = 0
        end_fight_update()

    if menu:
        pg.mixer.music.stop()
        if beg:
            tm = time.time() + 0.1
            beg = False
        if tm <= time.time():
            fight_button.get_event(event)
            inventory_button.get_event(event)
            alchemist_button.get_event(event)
            quit_button.get_event(event)

        if quit_button.clicked == 1:
            game_exit = True

        if fight_button.clicked == 1:
            if hero.hp > 0:
                menu = False
                fight = True
                ms.down_clear(win)
            fight_button.clicked = 0

        if alchemist_button.clicked == 1:
            menu = False
            alchemist = True
            alchemist_button.clicked = 0
            ms.down_clear(win)

        if inventory_button.clicked == 1:
            menu = False
            inventory = True
            inventory_button.clicked = 0
            ms.down_clear(win)

        if menu:
            menu_update()

    if alchemist:
        alch_heal1_button.get_event(event)
        alch_heal2_button.get_event(event)
        alch_heal3_button.get_event(event)
        to_menu_button.get_event(event)
        if astart:
            ms.smessage_display(win, 550, 525, "Player hp  " + str(hero.hp), 40)
            astart = False
        if alch_heal1_button.clicked == 1:
            if alch_heal1_button.timex < time.time() and a1:
                ms.message_clear(win)
                alch_heal1_button.timex += 2
                if hero.hp == 100:
                    ms.hp_clear(win)
                    ms.smessage_display(win, 755, 525, "You are healed already! Get out joker!", 40)
                else:
                    fun.heal(hero, 1, win)
                    if hero.hp > 100:
                        hero.hp = 100
                ms.hp_clear(win)
                ms.smessage_display(win, 550, 525, "Player hp  " + str(hero.hp), 40)
                a1 = False
            elif not a1 and alch_heal1_button.timex < time.time():
                ms.message_clear(win)
                alch_heal1_button.used = 0
                alch_heal1_button.clicked = 0
                a1 = True
        if alch_heal2_button.clicked == 1:
            if alch_heal2_button.timex < time.time() and a1:
                ms.message_clear(win)
                alch_heal2_button.timex += 2
                if hero.hp == 100:
                    ms.hp_clear(win)
                    ms.smessage_display(win, 755, 525, "You are healed already! Get out joker!", 40)
                else:
                    fun.heal(hero, 1, win)
                    if hero.hp > 100:
                        hero.hp = 100
                ms.hp_clear(win)
                ms.smessage_display(win, 550, 525, "Player hp  " + str(hero.hp), 40)
                a1 = False
            elif not a1 and alch_heal2_button.timex < time.time():
                ms.message_clear(win)
                alch_heal2_button.used = 0
                alch_heal2_button.clicked = 0
                a1 = True
        if alch_heal3_button.clicked == 1:
            if alch_heal3_button.timex < time.time() and a1:
                ms.message_clear(win)
                alch_heal3_button.timex += 2
                if hero.hp == 100:
                    ms.hp_clear(win)
                    ms.smessage_display(win, 755, 525, "You are healed already! Get out joker!", 40)
                else:
                    fun.heal(hero, 1, win)
                    if hero.hp > 100:
                        hero.hp = 100
                ms.hp_clear(win)
                ms.smessage_display(win, 550, 525, "Player hp  " + str(hero.hp), 40)
                a1 = False
            elif not a1 and alch_heal3_button.timex < time.time():
                ms.message_clear(win)
                alch_heal3_button.used = 0
                alch_heal3_button.clicked = 0
                a1 = True
        if to_menu_button.clicked == 1:
            alchemist = False
            menu = True
            beg = True
            astart = True
            to_menu_button.clicked = 0

        alchemist_update()

    if inventory:
        to_menu_button.get_event(event)
        if to_menu_button.clicked == 1:
            inventory = False
            menu = True
            beg = True
            to_menu_button.clicked = 0
        inventory_update()


pg.quit()
