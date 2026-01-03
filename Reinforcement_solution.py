import numpy as np
import random
from Reinforcement_leanrning_QTable import Field
class Solution:
    def reinforcement_solution(self):
        field_size = 10
        item_pickup = (0, 0)
        item_drop_off = (9, 9)
        start_position = (0, 9)
        epsilon = 0.1
        alpha = 0.1
        gamma = 0.6
        steps = 0
        field = Field(field_size, item_pickup, item_drop_off, start_position)
        done = False    
        steps = 0
        q_table = np.load("q_table.npy")
        number_of_actions=6


        while not done:
            state = field.getstate()

            # epsilon-greedy action selection
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, number_of_actions - 1)  # 0..5
            else:
                action = int(np.argmax(q_table[state]))

            reward, done = field.make_action(action)
            next_state = field.getstate()
            new_state_max = np.max(q_table[next_state])

            old_value = q_table[state, action]

            if done:
                target = reward
            else:
                target = reward + gamma * new_state_max

            # Q-learning update
            q_table[state, action] += alpha * (reward + gamma*new_state_max - q_table[state, action])


            steps += 1


            print(f"Step: {steps}, Action: {action}, Reward: {reward}, New State: {next_state}, Done: {done}")  
        return steps

if __name__ == "__main__":
    solution = Solution()
    total_steps = solution.reinforcement_solution()
    print("Total steps taken to complete the task:", total_steps)        
