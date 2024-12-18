import random
import numpy as np

# Define constants
MAP_HEIGHT = 48
MAP_WIDTH = 48
POPULATION_SIZE = 20
GENERATIONS = 100
MUTATION_RATE = 0.1

# Terrain types
EMPTY = '0'
WALL = '1'
RIVER = '4'
TREE = '3'

# Fitness weights
FITNESS_WEIGHTS = {
    "river": 5,
    "valley": 3,
    "barriers": 2
}

# Generate a random map
def generate_random_map():
    return [[random.choice([EMPTY, WALL]) for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

# Add a river to the map
def add_river(map_data):
    river_x = random.randint(0, MAP_WIDTH - 1)
    for y in range(MAP_HEIGHT):
        map_data[y][river_x] = RIVER
        # Slightly shift river's x-coordinate
        if random.random() < 0.5:
            river_x = max(0, min(MAP_WIDTH - 1, river_x + random.choice([-1, 1])))

# Calculate fitness of a map
def calculate_fitness(map_data):
    river_score = sum(row.count(RIVER) for row in map_data)
    valley_score = sum(row.count(EMPTY) for row in map_data)
    barriers_score = sum(row.count(WALL) for row in map_data)
    
    return (
        FITNESS_WEIGHTS["river"] * river_score +
        FITNESS_WEIGHTS["valley"] * valley_score +
        FITNESS_WEIGHTS["barriers"] * barriers_score
    )

# Mutate a map
def mutate(map_data):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if random.random() < MUTATION_RATE:
                map_data[y][x] = random.choice([EMPTY, WALL, RIVER, TREE])

# Crossover two maps
def crossover(map1, map2):
    child = []
    for y in range(MAP_HEIGHT):
        row = []
        for x in range(MAP_WIDTH):
            row.append(map1[y][x] if random.random() < 0.5 else map2[y][x])
        child.append(row)
    return child

# Generate initial population
population = [generate_random_map() for _ in range(POPULATION_SIZE)]

# Add rivers to initial population
for map_data in population:
    add_river(map_data)

# Evolution process
for generation in range(GENERATIONS):
    # Calculate fitness for each map
    fitness_scores = [calculate_fitness(map_data) for map_data in population]

    # Select parents based on fitness
    parents = random.choices(population, weights=fitness_scores, k=POPULATION_SIZE // 2)

    # Generate next generation
    next_generation = []
    while len(next_generation) < POPULATION_SIZE:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        mutate(child)
        next_generation.append(child)

    population = next_generation

# Find the best map in the final population
best_map = max(population, key=calculate_fitness)

# Print the best map
for row in best_map:
    print(''.join(row))
