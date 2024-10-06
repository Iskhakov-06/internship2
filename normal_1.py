import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, incoming_damage):
        return incoming_damage * (1 - self.armor / 100)

    def take_damage(self, incoming_damage):
        actual_damage = self._calculate_damage(incoming_damage)
        self.health -= actual_damage
        print(f"{self.name} получил {actual_damage} урона. Осталось здоровья: {self.health}")
        if self.health <= 0:
            print(f"{self.name} был побежден!")
            return True
        return False

    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}!")
        enemy_dead = enemy.take_damage(self.damage)
        return enemy_dead


class Player(Person):
    def __init__(self, name, health=100, damage=30, armor=20):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health=500, damage=15, armor=10):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def battle(self):
        attacker, defender = (self.player, self.enemy) if random.choice([True, False]) else (
            self.enemy, self.player)  # тут БОГ рандом решает кто, ходит первым

        while self.player.health > 0 and self.enemy.health > 0:
            print("\nНовый раунд:")
            defender_is_dead = attacker.attack(defender)
            if defender_is_dead:
                break

            attacker, defender = defender, attacker

        print("Бой завершён!")


# Пример
player = Player("Хороший")
enemy = Enemy("Плохой")

game = Game(player, enemy)
game.battle()
