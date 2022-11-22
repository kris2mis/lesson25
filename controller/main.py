# from model.player import FootballPlayer - перенесли в __init__(модуля!), а не контроллера
# from model.manager import Manager

from model import *  # - это написали вместо 2ух верхних импортов


def main():
    leo = FootballPlayer("Leo", "Messi", 910, 450)
    cristiano = FootballPlayer("Cristiano", "Ronaldo", 840, 300)
    alex = FootballPlayer("Alessandro", "Del Piero", 750, 800)
    ivan = FootballPlayer("Ivan", "Ivanov")

    players = (leo, cristiano, alex, ivan)

    for player in players:
        print(player)

    best_player = Manager.give_golden_ball(players)
    print(f"\nBest player: {best_player}")


if __name__ == "__main__":
    main()
