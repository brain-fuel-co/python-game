# Here are our basic definitions

class Monster:
    def __init__(self, level):
        self.health = level * 10
        self.attack_dmg = level * 2

    def receive_damage(self, damage):
        self.health = self.health - damage
        print(f"Monster took {damage} damage")
        if self.health <= 0:
            print("Monster died")
        else:
            print(f"Monster health: {self.health}")

    def deal_damage(self):
        return self.attack_dmg

monster = Monster(1)

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_dmg = 10
    def __str__(self):
        return f'''Character:
  Name:   {self.name}
  Health: {self.health}'''

    def receive_damage(self, damage):
        self.health = self.health - damage
        print(f"{self.name} took {damage} damage")
        if self.health <= 0:
            print(f"{self.name} died")
        else: 
            print(f"Current Health: {self.health}")

    def deal_damage(self):
        return self.attack_dmg

    def rest(self, rest_type):
        missing_health = 100 - self.health
        if rest_type == "long":
            self.health = 100
        if rest_type == "short":
            self.health = 100 - (missing_health / 2)
        print(f"{self.name} rested and now has {self.health} health")

def skirmish(player, monster):
    dmg_taken_by_monster = player.deal_damage()
    dmg_taken_by_player  = monster.deal_damage()
    monster.receive_damage(dmg_taken_by_monster)
    player.receive_damage(dmg_taken_by_player)

def setup_game():
    print("Welcome to the game. We still don't know what we're doing, lol")

    name_in = input("Please input your name: ")
    print(f"Hello, {name_in}")
    player = Player(name_in.upper())
    return player

def exit_game():
    quit()

def game_loop(game_status):
    while True:
        print(game_status)
        print("Type 's' to skirmish with monster")
        print("Type 'r' to rest")
        print("Type 'q' to quit")
        game_input = input("Take your action: ")
        if game_input == 's':
            skirmish(game_status, monster)
        elif game_input == 'r':
            rest_type = input("Enter 'short' for short rest, 'long' for long rest: ")
            game_status.rest(rest_type)
        elif game_input == 'q':
            exit_game()

# Here we put all the definitions together into a program
def main():
    game_status = setup_game()
    game_loop(game_status)

# This is what actually runs the program
if __name__ == "__main__":
    main()

