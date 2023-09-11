class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase


    def gname(self):
        return f'name: {self.name}'
    def health(self):
        return f'multiplied health: {self.health_points * 2}'

    def __str__(self):
       return f'nickname: {self.nickname}\n' \
              f'superpower: {self.superpower}\n' \
              f'health: {self.health_points}\n'

    def __len__(self):
       return f'length of catchphrase: {len(self.catchphrase)}'

name = SuperHero('Homelander', 'John', 'CompoundV', 10, 'You guys are the real heroes')


# print(name.gname())
# print(name)
# print(name.health())
# print(name.__len__())

class Sidekick(SuperHero):
    role = 'second'
    fly = False
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def health(self):
        return f'squared health: {self.health_points ** 2}'

    def truth(self):
        return True
    def crit(self):
        return f'damage is {self.damage ** 2}'


class AntiHero(SuperHero):
    costume = 'yes'
    fly = True
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
    def health(self):
        return f'multiplied health: {self.health_points ** 2}'


class Villain(AntiHero):
    people = 'monster'
    def gen_x(self):...
    def crit(self):
        return f'damage is {self.damage ** 2}'


sidekick = Sidekick('Kevin', 'The Deep', 'fish', 8, 'fuck fresca', 1)
antihero = AntiHero('Hugh', 'Hughie Campbell', 'tempV', 6, 'lier', 9)
print(sidekick)
print(antihero)
# print(sidekick.health())
# print((sidekick.truth()))
villain = Villain('Billy Butcher', 'Butcher', 'tempV', 1, 'cunt', 100)
print(villain)
print(sidekick.crit())