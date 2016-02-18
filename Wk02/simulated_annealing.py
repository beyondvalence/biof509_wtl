"""Module to find shortest path connecting series of points

    simluated_annealing_optimizer accepts a set of coordinates,
    cost function, new path function, start and minimum temp, and
    number of steps to return the optimized path, optimized distance,
    and the other paths and distances.
"""

def distance(coords):
    """Calculates the distance of a path between multiple points
    
    Arguments:
    coords -- List of coordinates, e.g. [(0,0), (1,1)]
    
    Returns: Total distance as a float
    """
    distance = 0
    for p1, p2 in zip(coords[:-1], coords[1:]):
        distance += ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance


def new_path(existing_path):
	"""Reorders list of coordinates
    
    Arguments:
    existing_path -- List of coordinates, e.g. [(0,0), (1,1)]
        
    Returns:
    path -- List of reordered coordinates, e.g. [(0,0), (1,1)]
	"""
    path = existing_path[:]
    point = random.randint(0, len(path)-2)
    path[point+1], path[point] = path[point], path[point+1]
    # print(point)
    return path


def simulated_annealing_optimizer(starting_path, cost_func, new_path_func, start_temp, min_temp, steps):
	"""Finds optimized route with given list of coordinates, and uses randomness to avoid local minimums
	
    Arguments:
    starting_path -- List of coordinates, e.g. [(0,0), (2,2)]
    cost_func -- Optimization metric calculator, e.g. distance()
    new_path_func -- Returns reordered coordinates, e.g. new_path()
    start_temp -- Upper temperature range for temperature factor, e.g. 1000
    min_temp -- Lower temperature range for temperature factor, e.g. 0.01
    steps -- Number of route iterations e.g. 1000
    
    Returns:
    current_path -- Optimized coordinate order
    current_cost -- Optimized distance
    history -- Dictionary of iterated coordinate orders and corresponding distances
	"""
    current_path = starting_path[:]
    current_cost = cost_func(current_path)
    temp_factor = -np.log(start_temp / min_temp)
    history = []
    for s in range(0, steps):
        temp = start_temp * np.exp(temp_factor * s / steps)
        new_path = new_path_func(current_path)
        new_cost = cost_func(new_path)
        if (new_cost < current_cost) or (random.random() <= np.exp(-(new_cost - current_cost)/temp)):
            current_path = new_path
            current_cost = new_cost
        record = {'step':s, 'temperature':temp, 'current_cost':current_cost, }
        history.append(record)
    return (current_path, current_cost, history)

best_path, best_cost, history = simulated_annealing_optimizer(coords, distance, new_path, 1000, 0.01, 1000)
print(best_cost)
plt.plot([i['current_cost'] for i in history])
plt.show()

plt.plot([i['temperature'] for i in history])
plt.show()

plt.plot([i[0] for i in best_path], [i[1] for i in best_path])
plt.show()