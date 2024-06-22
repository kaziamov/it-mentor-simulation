class Entity:
    pass


class Grass(Entity):
    pass


class Rock(Entity):
    pass


class Tree(Entity):
    pass


class Creature(Entity):
    default_health: int

    def __init__(self, hp):
        self._hp = hp or self.default_health

    def _make_move(self):
        raise NotImplementedError

    def make_move(self):
        self._make_move()

    def is_alive(self):
        return self._hp > 0

    def damage(self, damage: int):
        self._hp - damage


class Herbivore(Creature):
    pass


class Predator(Creature):
    default_damage: int

    def __init__(self, hp, damage):
        super().__init__(hp)
        self._damage = damage

    def attack(self, creature):
        creature.damage()



class Map:
    def __init__(self):
        self._creatures = set()

    @property
    def creatures(self):
        return self._creatures

    def add_creature(self, creature):
        self._creatures.add(creature)

    def kill_creature(self, creature):
        self._creatures.remove(creature)


class Simulation:
    def __init__(self, map, renderer):
        self._map = map
        self._renderer = renderer
        self._turns_count = 0

    def next_turn(self):
        pass

    def start_simulation(self):
        pass

    def pause_simulation(self):
        pass
