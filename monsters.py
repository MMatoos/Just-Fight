import classes
import weapons

skeleton = classes.Monster(725, 370, 10, 10)
skeleton.name = "Skeleton"
skeleton.max_hp = 50
skeleton.hp = 50
skeleton.weapon = weapons.claws

bandit = classes.Monster(725, 370, 10, 10)
bandit.name = "Bandit"
bandit.max_hp = 75
bandit.hp = 75
bandit.weapon = weapons.mace

gladiator = classes.Monster(725, 370, 10, 10)
gladiator.name = "Gladiator"
gladiator.max_hp = 90
gladiator.hp = 90
gladiator.weapon = weapons.sword

dead_body = classes.Monster(1000, 400, 10, 10)
dead_body.hp = -1
dead_body.status = False

monsters = [skeleton, bandit, gladiator]
