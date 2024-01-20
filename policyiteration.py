import maze
import re



def policy_iteration(grid, gamma):
    """
    Performs policy iteration on a given grid of MDPState objects.
    """
    
    is_policy_changed = True
    
    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]
    actions = ['up', 'down', 'left', 'right']
    
    iterations = 0
    
    # Policy iteration
    while is_policy_changed:
        print(f"Iteration : {iterations}")
        print(prettify_policy(policy))
        is_policy_changed = False
        # Policy evaluation
        # Transition probabilities not shown due to deterministic setting
        is_value_changed = True
        while is_value_changed:
            is_value_changed = False
            # Run value iteration for each state
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '#':
                        policy[i][j] = '#'
                    else:
                        neighbor = getattr(grid[i][j], policy[i][j])
                        v = grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value
                        # Compare to previous iteration
                        if v != grid[i][j].value:
                            is_value_changed = True
                            grid[i][j].value = v
                                
        # Once values have converged for the policy, update policy with greedy actions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '#':
                    # Dictionary comprehension to get value associated with each action
                    action_values = {a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value for a in actions}
                    best_action = max(action_values, key=action_values.get)
                    # Compare to previous policy
                    if best_action != policy[i][j]:
                        is_policy_changed = True
                        policy[i][j] = best_action
                        
        iterations += 1
                    
    return(policy)
    
def prettify_policy(policy):
    policy_str = '\n'.join([''.join(row) for row in policy])
    policy_str = re.sub('up', '↑', policy_str)
    policy_str = re.sub('down', '↓', policy_str)
    policy_str = re.sub('right', '→', policy_str)
    policy_str = re.sub('left', '←', policy_str)
    return(policy_str)


def calculate_optimal_path_cost_from_start(grid, policy, start_position):
    """
    Calculate the cost of the optimal path from the given start position based on the policy and grid.
    """
    cost = 0
    current_position = start_position
    path_to_goal = []
    if grid[start_position[0]][start_position[1]] == '#':
        print("_____Starting point is already an Obstacle_____")
        return -1
    while True:
        action = policy[current_position[0]][current_position[1]]
        path_to_goal.append(action)
        #print(action)

        # If the action is '#' (blocked cell), break the loop
        if action == '#':
            break

        # Update the cost with the reward of the current state
        cost += grid[current_position[0]][current_position[1]].reward

        # Move to the next state based on the action
        if action == 'up':
            current_position = (current_position[0] - 1, current_position[1])
        if action == 'down':
            current_position = (current_position[0] + 1, current_position[1])
        if action == 'right':
            current_position = (current_position[0], current_position[1] + 1)
        if action == 'left':
            current_position = (current_position[0], current_position[1] - 1)
        #current_position = getattr(grid[current_position[0]][current_position[1]], action)
        #print(current_position)
    print("_____Path to Goal_____")
    print(path_to_goal)
    return cost


if __name__ == '__main__':
    test_maze = maze.Maze(w=20, h=20, num_exits=2)
    print("_____Iterations_____")
    test_policy = policy_iteration(test_maze.grid, 0.9)
    test_policy_str = prettify_policy(test_policy)

    start_position = (1, 1)  # Specify the starting position

    optimal_path_cost = calculate_optimal_path_cost_from_start(test_maze.grid, test_policy, start_position)

    print("_____Exit Points_____")
    print(test_maze.exit_points)
    print("_____Maze_____")
    print(test_maze)
    print("_____Optimal Policy_____")
    print(test_policy_str)
    print("_____Path Cost_____")
    print(f"Optimal Path Cost from {start_position}: {optimal_path_cost}")

