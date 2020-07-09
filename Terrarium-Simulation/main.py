import random
import terrain_cell
import animal

# Greeting and getting user input for the simulation parameters
while True:
    try:
        print('Hello!\nPlease enter the required information below...')
        world_size = int(input('Enter world size (Positive number): '))
        days = int(input('How many days would you like the simulation to run for (Positive number): '))

        if world_size <= 0:
            raise ValueError
        break
    except ValueError:
        print('Please enter a positive number!')


# Creating the animal objects that will be a part of the simulation
carnivore_X = random.randint(0, world_size - 1)
carnivore_Y = random.randint(0, world_size - 1)
carnivore = animal.Animal('Carnivore', 'alive', 10, [carnivore_X, carnivore_Y])

herbivore_X = random.randint(0, world_size - 1)
herbivore_Y = random.randint(0, world_size - 1)
herbivore = animal.Animal('Herbivore', 'alive', 10, [herbivore_X, herbivore_Y])

scavenger_X = random.randint(0, world_size - 1)
scavenger_Y = random.randint(0, world_size - 1)
scavenger = animal.Animal('Scavenger', 'alive', 10, [scavenger_X, scavenger_Y])

terrain_cell.TerrainCell.animals = []

# Terrain variables needed
terrain_type = ['WATER', 'DESERT', 'MOUNTAIN', 'GRASS']
terrain = []
terrain_row = []

# Generating the world grid
terrain_row_counter = 1
while terrain_row_counter <= world_size:
    terrain_row = []

    terrain_row_elements_counter = 1
    while terrain_row_elements_counter <= world_size:
        random_terrain = random.randint(0, 3)

        terrain_row.append(terrain_cell.TerrainCell(terrain_type[random_terrain], []))
        
        terrain_row_elements_counter += 1

    terrain.append(terrain_row)
    terrain_row_counter += 1

# Adding the animals into the world and printing it into the console
print('This is how the world looks like:')
for i in range(len(terrain)):
    print('')

    for j in range(len(terrain_row)):
        if (i == carnivore_X and j == carnivore_Y):
            terrain[i][j].animals.append(carnivore.kind)
        if (i == herbivore_X and j == herbivore_Y):
            terrain[i][j].animals.append(herbivore.kind)
        if (i == scavenger_X and j == scavenger_Y):
            terrain[i][j].animals.append(scavenger.kind)
        
        print(terrain[i][j].cell_type, end = ' ')
        print(', ', end = '')
        print(terrain[i][j].animals, end = ' ')
        print('|', end = ' ')

def carnivore_move(direction):
    for i in range(len(terrain)):
        for j in range(len(terrain_row)):
            if len(terrain[i][j].animals) != 0:
                if ('Carnivore' in terrain[i][j].animals):
                    carnivore_X = i
                    carnivore_Y = j

    # Going up a cell
    # Making sure there is no index out of range error
    if (carnivore_X - 1 <= 0):
        direction += 1
    else:
        if (direction == 1):
            terrain[carnivore_X][carnivore_Y].animals.clear()
            terrain[carnivore_X - 1][carnivore_Y].animals.append(carnivore.kind)
            print('The ' + carnivore.kind + ' moved to: ' + str((carnivore_X - 1)), str(carnivore_Y) + ' from ' + str(carnivore_X), str(carnivore_Y))
            carnivore.location = [carnivore_X - 1, carnivore_Y]
        
    # Going down a cell
    # Making sure there is no index out of range error
    if (carnivore_X + 1 >= world_size):
        direction += 1
    else:
        if (direction == 2):
            terrain[carnivore_X][carnivore_Y].animals.clear()
            terrain[carnivore_X + 1][carnivore_Y].animals.append(carnivore.kind)
            print('The ' + carnivore.kind + ' moved to: ' + str((carnivore_X + 1)), str(carnivore_Y) + ' from ' + str(carnivore_X), str(carnivore_Y))
            carnivore.location = [carnivore_X + 1, carnivore_Y] 
        
    # Going left a cell
    # Making sure there is no index out of range error
    if (carnivore_Y - 1 <= 0):
        direction += 1
    else:
        if (direction == 3):
            terrain[carnivore_X][carnivore_Y].animals.clear()
            terrain[carnivore_X][carnivore_Y - 1].animals.append(carnivore.kind)
            print('The ' + carnivore.kind + ' moved to: ' + str(carnivore_X), str((carnivore_Y - 1)) + ' from ' + str(carnivore_X), str(carnivore_Y))
            carnivore.location = [carnivore_X, carnivore_Y - 1] 
        
    # Going up a cell
    # Making sure there is no index out of range error
    if (carnivore_Y + 1 >= world_size):
        direction -= 1
    else:
        if (direction == 4):
            terrain[carnivore_X][carnivore_Y].animals.clear()
            terrain[carnivore_X][carnivore_Y + 1].animals.append(carnivore.kind)
            print('The ' + carnivore.kind + ' moved to: ' + str(carnivore_X), str((carnivore_Y + 1)) + ' from ' + str(carnivore_X), str(carnivore_Y))
            carnivore.location = [carnivore_X, carnivore_Y + 1]

    if (terrain[carnivore_X][carnivore_Y].cell_type == 'WATER'):
        carnivore.status = 'dead'
        print('The Carnivore drowned')

def herbivore_move(direction):
    for i in range(len(terrain)):
        for j in range(len(terrain_row)):
            if len(terrain[i][j].animals) != 0:
                if ('Herbivore' in terrain[i][j].animals):
                    herbivore_X = i
                    herbivore_Y = j

    # Going up a cell
    # Making sure there is no index out of range error
    if (herbivore_X - 1 <= 0):
        direction += 1
    else:
        if (direction == 1):
            terrain[herbivore_X][herbivore_Y].animals.clear()
            terrain[herbivore_X - 1][herbivore_Y].animals.append(herbivore.kind)
            print('The ' + herbivore.kind + ' moved to: ' + str((herbivore_X - 1)), str(herbivore_Y) + ' from ' + str(herbivore_X), str(herbivore_Y))
            herbivore.location = [herbivore_X - 1, herbivore_Y]
        
    # Going down a cell
    # Making sure there is no index out of range error
    if (herbivore_X + 1 >= world_size):
        direction += 1
    else:
        if (direction == 2):
            terrain[herbivore_X][herbivore_Y].animals.clear()
            terrain[herbivore_X + 1][herbivore_Y].animals.append(herbivore.kind)
            print('The ' + herbivore.kind + ' moved to: ' + str((herbivore_X + 1)), str(herbivore_Y) + ' from ' + str(herbivore_X), str(herbivore_Y))
            herbivore.location = [herbivore_X + 1, herbivore_Y]
        
    # Going left a cell
    # Making sure there is no index out of range error
    if (herbivore_Y - 1 <= 0):
        direction += 1
    else:
        if (direction == 3):
            terrain[herbivore_X][herbivore_Y].animals.clear()
            terrain[herbivore_X][herbivore_Y - 1].animals.append(herbivore.kind)
            print('The ' + herbivore.kind + ' moved to: ' + str(herbivore_X), str((herbivore_Y - 1)) + ' from ' + str(herbivore_X), str(herbivore_Y))
            herbivore.location = [herbivore_X, herbivore_Y - 1]
        
    # Going up a cell
    # Making sure there is no index out of range error
    if (herbivore_Y + 1 >= world_size):
        direction -= 1
    else:
        if (direction == 4):
            terrain[herbivore_X][herbivore_Y].animals.clear()
            terrain[herbivore_X][herbivore_Y + 1].animals.append(herbivore.kind)
            print('The ' + herbivore.kind + ' moved to: ' + str(herbivore_X), str((herbivore_Y + 1)) + ' from ' + str(herbivore_X), str(herbivore_Y))
            herbivore.location = [herbivore_X, herbivore_Y + 1]

    if (terrain[herbivore_X][herbivore_Y].cell_type == 'WATER'):
        herbivore.status = 'dead'
        print('The Herbivore drowned')

def scavenger_move(direction):
    for i in range(len(terrain)):
        for j in range(len(terrain_row)):
            if len(terrain[i][j].animals) != 0:
                if ('Scavenger' in terrain[i][j].animals):
                    scavenger_X = i
                    scavenger_Y = j

    # Going up a cell
    # Making sure there is no index out of range error
    if (scavenger_X - 1 <= 0):
        direction += 1
    else:
        if (direction == 1):
            terrain[scavenger_X][scavenger_Y].animals.clear()
            terrain[scavenger_X - 1][scavenger_Y].animals.append(scavenger.kind)
            print('The ' + scavenger.kind + ' moved to: ' + str((scavenger_X - 1)), str(scavenger_Y) + ' from ' + str(scavenger_X), str(scavenger_Y))
            scavenger.location = [scavenger_X - 1, scavenger_Y]
        
    # Going down a cell
    # Making sure there is no index out of range error
    if (scavenger_X + 1 >= world_size):
        direction += 1
    else:
        if (direction == 2):
            terrain[scavenger_X][scavenger_Y].animals.clear()
            terrain[scavenger_X + 1][scavenger_Y].animals.append(scavenger.kind)
            print('The ' + scavenger.kind + ' moved to: ' + str((scavenger_X + 1)), str(scavenger_Y) + ' from ' + str(scavenger_X), str(scavenger_Y)) 
            scavenger.location = [scavenger_X + 1, scavenger_Y]
        
    # Going left a cell
    # Making sure there is no index out of range error
    if (scavenger_Y - 1 <= 0):
        direction += 1
    else:
        if (direction == 3):
            terrain[scavenger_X][scavenger_Y].animals.clear()
            terrain[scavenger_X][scavenger_Y - 1].animals.append(scavenger.kind)
            print('The ' + scavenger.kind + ' moved to: ' + str(scavenger_X), str((scavenger_Y - 1)) + ' from ' + str(scavenger_X), str(scavenger_Y))
            scavenger.location = [scavenger_X, scavenger_Y - 1]
        
    # Going up a cell
    # Making sure there is no index out of range error
    if (scavenger_Y + 1 >= world_size):
        direction -= 1
    else:
        if (direction == 4):
            terrain[scavenger_X][scavenger_Y].animals.clear()
            terrain[scavenger_X][scavenger_Y + 1].animals.append(scavenger.kind)
            print('The ' + scavenger.kind + ' moved to: ' + str(scavenger_X), str((scavenger_Y + 1)) + ' from ' + str(scavenger_X), str(scavenger_Y))
            scavenger.location = [scavenger_X, scavenger_Y + 1]

def animal_move(direction, moving_animal):
    if (moving_animal.kind == 'Carnivore'):
        carnivore_move(direction)
    if (moving_animal.kind == 'Herbivore'):
        herbivore_move(direction)
    if (moving_animal.kind == 'Scavenger'):
        scavenger_move(direction)
    

def eat(eating_animal):
    if (eating_animal.kind == 'Carnivore'):
        if(carnivore.location == herbivore.location):
            herbivore.status = 'eaten'
            print('The Carnivore ate the Herbivore')
            carnivore.hunger = 10
    if (eating_animal.kind == 'Herbivore'):
        hx = herbivore.location[0]
        hy = herbivore.location[1]

        if(terrain[hx][hy].cell_type == 'GRASS'):
            print('The Herbivore ate some grass')
            herbivore.hunger = 10
    if (eating_animal.kind == 'Scavanger'):
        if ((scavenger.location == herbivore.location and herbivore.status == 'dead' or herbivore.status == 'eaten') or (scavenger.location == carnivore.location and carnivore.status == 'dead')):
            print('The Scavenger ate carrion')
            scavenger.hunger = 10

# Simulation
days_counter = 0
while (days_counter <= days):
    print('Day: ' + str(days_counter))

    if (carnivore.hunger <= 5 and carnivore.status == 'alive'):
        random_direction = random.randint(1, 4)
        eat(carnivore)
        animal_move(random_direction, carnivore)

        if (carnivore.hunger == 0):
            carnivore.status = 'dead'
            print('The ' + carnivore.kind + ' just died')

    if (herbivore.hunger <= 5 and herbivore.status == 'alive'):
        random_direction = random.randint(1, 4)
        eat(herbivore)
        animal_move(random_direction, herbivore)

        if (herbivore.hunger == 0):
            herbivore.status = 'dead'
            print('The ' + herbivore.kind + ' just died')

    if (scavenger.hunger <= 5 and scavenger.status == 'alive'):
        random_direction = random.randint(1, 4)
        eat(scavenger)
        animal_move(random_direction, scavenger)

        if (scavenger.hunger == 0):
            scavenger.status = 'dead'
            print('The ' + scavenger.kind + ' just died')
    
    days_counter += 1
    carnivore.hunger -= 1
    herbivore.hunger -= 1
    scavenger.hunger -= 1
