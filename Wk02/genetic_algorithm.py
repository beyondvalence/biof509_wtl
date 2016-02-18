"""Module to find shortest path connecting series of points

    genetic_algorithm_optimizer accepts a set of coordinates,
    cost function, new path function, population size, and
    number of generations to return the optimized path, optimized distance,
    and the other paths and distances.
    20160218 Wayne Liu
"""


def select_best(population, cost_func, num_to_keep):
    """Selects best specified population based on the cost function
    
    Arguments:
    population -- List of shuffled coordinates
    cost_func -- Function deriving optimized metric
    num_to_keep -- Number of best population to keep
    
    Returns:
    List of best optimized  specified number of coordinates
    """
    scored_population = [(i, cost_func(i)) for i in population]
    scored_population.sort(key=lambda x: x[1])
    return [i[0] for i in scored_population[:num_to_keep]]


def new_path(existing_path):
	"""Reorders list of coordinates
    
    Arguments:
    existing_path -- List of coordinates, e.g. [(0,0), (1,1)]
        
    Returns:
    path -- List of reordered coordinates, e.g. [(0,0), (1,1)]
	"""
    path = existing_path[:]
    # switches three points instead of two, marginally better
    point = random.randint(0, len(path)-3)
    path[point+2], path[point+1], path[point] = path[point], path[point+2], path[point+1]
    # print(point)
    return path


def recombine(population):
    """Recombines random two halves of two random sets of coordinates
    
    Argument:
    population -- List of coordinates, e.g. [(0,0), (1,1)]
    
    Returns:
    child -- A set of coordinates, recombined from two random sets of coordinates, e.g. [(9,9), (2,3)]
    """
    # Randomly choose two parents
    options = list(range(len(population)))
    random.shuffle(options)
    partner1 = options[0]
    partner2 = options[1]
    # Choose a split point, take the first parents order to that split point, 
    # then the second parents order for all remaining points
    split_point = random.randint(0, len(population[0])-1)
    child = population[partner1][:split_point]
    for point in population[partner2]:
        if point not in child:
            child.append(point)
    return child


def genetic_algorithm_optimizer(starting_path, cost_func, new_path_func, pop_size, generations):
    """Selects best path from set of coordinates by randomly joining two sets of coordinates
    
    Arguments:
    starting_path -- List of coordinates, e.g. [(0,0), (1,1)]
    cost_func -- Optimization metric calculator, e.g. distance()
    new_path_func -- Returns reordered coordinates, e.g. new_path()
    pop_size -- Number of each set of coordinates in each generation, 500
    generations -- Number of iterations, 100
    
    Returns:
    population -- A list of optimized coordinates, e.g. [(2,3), (5,6)]
    cost_func -- The optimized least distance
    history -- Dictionary of generation and distance metrics
    """
    # Create a starting population by randomly shuffling the points
    population = []
    for i in range(pop_size):
        new_path = starting_path[:]
        random.shuffle(new_path)
        population.append(new_path)
    history = []
    # Take the top 25% of routes and recombine to create new routes, repeating for generations
    for i in range(generations):
        pop_best = select_best(population, cost_func, int(pop_size / 4))
        new_population = []
        for i in range(pop_size):
            new_population.append(new_path_func(recombine(pop_best))) # use new path to scramble the order
        population = new_population
        record = {'generation':i, 'current_cost':cost_func(population[0]),}
        history.append(record)
    return (population[0], cost_func(population[0]), history)


best_path, best_cost, history = genetic_algorithm_optimizer(coords, distance, new_path, 500, 100)
print(best_cost)
plt.plot([i['current_cost'] for i in history])
plt.show()        
    
plt.plot([i[0] for i in best_path], [i[1] for i in best_path])
plt.show()