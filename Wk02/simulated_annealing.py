def new_path(existing_path):
	"""
	"""
    path = existing_path[:]
    point = random.randint(0, len(path)-2)
    path[point+1], path[point] = path[point], path[point+1]
    # print(point)
    return path

# generate a large and random walk to traverse the search space with randomness
# in order to avoid staying in local minimums
# with temp_factor
def simulated_annealing_optimizer(starting_path, cost_func, new_path_func, start_temp, min_temp, steps):
	"""
	Creates simulated annealing algorithm
	
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