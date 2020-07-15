import random

class EatErorr(Exception):
    pass

class Creature:
    def __init__(self, cell):
        self.hunger = 10
        self.status = 1
        self.cell = cell

    @property
    def id(self):
        return id(self)

    @property
    def klass(self):
        return self.__class__.__name__

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, value):
        del self.cell
        self._cell = value
        self._cell.creatures.append(self)

        if self.cell.is_water:
            self.die("Drawn in cell: %s, %s" % self.cell.coordinates)

    @cell.deleter
    def cell(self):
        if hasattr(self, '_cell'):
            self._cell.creatures.remove(self)
            del self._cell

    @property
    def is_hungry(self):
        if self.hunger == 0: #
            self.is_dead #added by me
        return self.hunger < 5
    
    @property
    def is_alive(self):
        return self.status
    
    @property
    def is_dead(self):
        return self.status == 0

    @property
    def is_eaten(self):
        return self.status == -1

    def play(self):
        assert self.is_alive, "Im dead"
        if self.is_hungry:
            try:
                self.eat()
            except EatErorr:
                self.move()

    def move(self):
        assert self.is_alive, "Im dead"
        new_cell = random.choice(self.cell.neighbours)
        self.cell = new_cell

    def eat(self):
        assert self.is_alive, "Im dead"
        self._eat()

    def _eat(self):
        raise EatErorr('not implemented')

    def die(self, reason):
        assert self.is_alive, "Im dead"
        self.status = 0
        print("Creature %s died: %s" % (self.id, reason))

    def get_eaten(self, scavenger):
        assert self.is_dead
        self.status = -1
        print("Dead creature: %s got eaten by %s" % (self.id, scavenger.id))

class Carnivore(Creature):
    def _eat(self):
        for creature in self.cell.creatures:
            if creature is self:
                continue
            if not creature.is_alive:
                continue
            if not self.hunger > creature.hunger:
                continue
            
            creature.die("Eaten by %s" % self.id)
            self.hunger += creature.hunger
            return

        raise EatErorr('Nothing to Eat')    

class Herbivore(Creature):
    def _eat(self):
        if not self.cell.is_grass:
            raise EatErorr("No grass")

        self.hunger += random.randint(1,5)

class Scavenger(Creature):
    def _eat(self):
        for creature in self.cell.creatures:
            if creature is self:
                continue
            if not creature.is_dead:
                continue
            
            self.hunger += int(creature.hunger/2)
            creature.get_eaten(self)
            return

        raise EatErorr('Nothing to Eat')

class Cell:
    def __init__(self, terrain, x, y, nature):
        self.terrain = terrain
        self.x = x
        self.y = y
        self.nature = nature
        self.creatures = []

    @property
    def coordinates(self):
        return (self.x, self.y)
    
    @property
    def is_grass(self):
        return self.nature == 'GRASS'
        
    @property
    def is_water(self):
        return self.nature == 'WATER'

    @property
    def num_creatures(self):
        return len(self.creatures)
    
    @property
    def neighbours(self):
        min_x = max(0, self.x-1)
        max_x = min(self.terrain.width, self.x+1)
        min_y = max(0, self.y-1)
        max_y = min(self.terrain.height, self.y+1)

        return [cell for cell in self.terrain.cells if (
                cell is not self) 
                and (max_x >= cell.x >= min_x) 
                and (max_y >= cell.y >= min_y)
        ]

class Terrain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.days = 0
        self.cells = self.create_cells()

    @property
    def days_passed(self):
        return self.days

    @property
    def has_creatures_alive(self):
        return any(creature.is_alive for creature in self.creatures)

    @property
    def creatures(self):
        creatures = []

        for cell in self.cells:
            creatures.extend(cell.creatures)
        
        return creatures

    def create_cells(self):
        cells = []
        natures = ['WATER', 'GRASS', 'MOUNTAIN', 'DESERT']

        for x in range(self.width):
            for y in range(self.height):
                nature = random.choice(natures)
                cell = Cell(self, x, y, nature)
                cells.append(cell)
        
        return cells

    def create_creatures(self, num):
        creature_classes = [Carnivore, Herbivore, Scavenger]

        for _ in range(num):
            klass = random.choice(creature_classes)
            cell = random.choice(self.cells)
            klass(cell)

    def simulate(self):
        for creature in self.creatures:
            if creature.is_alive:
                creature.hunger -= 1 # added by me
                creature.play()
        
        self.days += 1

    def render_status(self):
        print('=========================== Day %s ===========================' % self.days)
        for cell in self.cells:
            print("Cell %s, type: %s, %s creatures" % (cell.coordinates, cell.nature, cell.num_creatures))
            for creature in cell.creatures:
                print("-----  Creature: %s, type: %s, status: %s" % (creature.id, creature.klass, creature.status))
        print('==============================================================')

def main():
    terrain = Terrain(3, 4)
    terrain.create_creatures(10)

    while terrain.has_creatures_alive and terrain.days_passed < 100:
        terrain.simulate()
        terrain.render_status()

    print('done')

if __name__ == "__main__":
    main()
