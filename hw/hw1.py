from random import randint, choice
import argparse
import logging

FORMAT = "%(levelname)s: %(asctime)s - %(message)s"
LOG_FILE_NAME = "warriors.log"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

handler = logging.FileHandler(LOG_FILE_NAME, encoding="UTF-8")
handler.setFormatter(logging.Formatter(FORMAT))
handler.setLevel(logging.INFO)
logger.addHandler(handler)


class Warrior:
    __START_HP = 100

    def __init__(self, name):
        self.name = name
        self.hp = self.__START_HP
        self.level = 1
        self.min_damage = 10
        self.max_damage = 15

    def __str__(self):
        return f"{self.name}[lvl:{self.level: >2}, hp:{self.hp: >3}]"

    def attack(self, other):
        if isinstance(other, Warrior):
            damage = randint(self.min_damage, self.max_damage)
            other.hp -= damage
            info = f"{self} ударил на {damage} -> {other}"
            # print(info)
            logger.info(info)
            if other.hp <= 0:
                self.level_up()
                logger.info(f"{self} получил уровень!")
        else:
            raise TypeError("Не работает с этим типом")

    def level_up(self):
        self.level += 1
        self.min_damage += 5
        self.max_damage += 5


def fight(list_warriors: list[Warrior]):
    if not all(isinstance(obj, Warrior) for obj in list_warriors):
        error_text = "В списке должны быть только ВОИНЫ!"
        logger.error(error_text)
        raise TypeError(error_text)
    while True:
        if len(list_warriors) == 1:
            return list_warriors[0]
        random_attacker = choice(list_warriors)
        random_defender = choice([war for war in list_warriors if war != random_attacker])
        random_attacker.attack(random_defender)
        if random_defender.hp <= 0:
            list_warriors.remove(random_defender)


def out_parser() -> int:
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-c', '--count', metavar='count', default='5')
    result = parser.parse_args()
    return int(result.count)


if __name__ == '__main__':
    warriors = []
    for i in range(1, out_parser() + 1):
        warriors.append(Warrior(str(i)))
    print(f"Победил воин {fight(warriors)}")
