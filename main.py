import timeit
import numpy as np
import maze
import policyiteration
import time
import valueiteration

test_maze = maze.Maze(w=4, h=4, num_exits=2)
print("_____Policy Iteration_____")
print("_____Iterations_____")
start_time = time.time()
test_policy = policyiteration.policy_iteration(test_maze.grid, 0.9)
end_time = time.time()
test_policy_str = policyiteration.prettify_policy(test_policy)

start_position = (1, 1)  # Specify the starting position

optimal_path_cost = policyiteration.calculate_optimal_path_cost_from_start(test_maze.grid, test_policy, start_position)

print("_____Exit Points_____")
print(test_maze.exit_points)
print("_____Maze_____")
print(test_maze)
print("_____Optimal Policy_____")
print(test_policy_str)
print("_____Path Cost_____")
print(f"Optimal Path Cost from {start_position}: {optimal_path_cost} with time = {end_time - start_time} seconds")
print("____________________________________________________________________________________________________")
print("_____Value Iteration_____")
start_time_V = time.time()
test_policy = valueiteration.value_iteration(test_maze.grid, .9)
end_time_V = time.time()
test_policy_str = valueiteration.prettify_policy(test_policy)
start_position = (1, 1)  # Specify the starting position
optimal_path_cost = valueiteration.calculate_optimal_path_cost_from_start(test_maze.grid, test_policy, start_position)
print("_____Exit Points_____")
print(test_maze.exit_points)
print("_____Maze_____")
print(test_maze)
print("_____Optimal Policy_____")
print(test_policy_str)
print("_____Path Cost_____")
print(f"Optimal Path Cost from {start_position}: {optimal_path_cost} with time = {end_time_V - start_time_V} seconds")
