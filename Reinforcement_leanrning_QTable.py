import random
import numpy as np

class Field:
    def __init__(self, size, item_pickup, item_drop_off, start_position):
        self.size = size
        self.item_pickup = item_pickup
        self.item_drop_off = item_drop_off
        self.position = start_position
        self.item_in_car = False

    def make_action(self, action):
        (x, y) = self.position

        if action == 0:  # up
            if x == 0:
                return -10, False
            else:
                self.position = (x - 1, y)
                return -1, False

        elif action == 1:  # down
            if x == self.size - 1:
                return -10, False
            else:
                self.position = (x + 1, y)
                return -1, False

        elif action == 2:  # left
            if y == 0:
                return -10, False
            else:
                self.position = (x, y - 1)
                return -1, False

        elif action == 3:  # right
            if y == self.size - 1:
                return -10, False
            else:
                self.position = (x, y + 1)
                return -1, False

        elif action == 4:  # pickup
            # invalid pickup locations / states
            if self.position != self.item_pickup:
                return -10, False
            if self.item_in_car:
                return -10, False
            if self.position == self.item_drop_off:
                return -10, False

            # valid pickup
            self.item_in_car = True
            return 20, False   # continue episode after pickup

        elif action == 5:  # dropoff
            # invalid dropoff locations / states
            if self.position != self.item_drop_off:
                return -10, False
            if self.position == self.item_pickup:
                return -10, False
            if not self.item_in_car:
                return -10, False

            # successful dropoff
            self.item_in_car = False
            return 20, True    # end episode

        # just in case some invalid action sneaks in
        return -10, False

    def get_number_of_states(self):
        return self.size * self.size * self.size * self.size * 2

    def getstate(self):
        state = self.position[0] * self.size * self.size * self.size * 2
        state += self.position[1] * self.size * self.size * 2
        state += self.item_pickup[0] * self.size * 2
        state += self.item_pickup[1] * 2

        if self.item_in_car:
            state += 1

        return state


if __name__ == "__main__":
    field_size = 10
    item_pickup = (0,0)
    item_drop_off = (9,9)
    start_position = (0, 9)

    field = Field(field_size, item_pickup, item_drop_off, start_position)

    number_of_states = field.get_number_of_states()
    number_of_actions = 6

    q_table = np.zeros((number_of_states, number_of_actions))

    epsilon = 0.1
    alpha = 0.1
    gamma = 0.6
    steps = 0
    total_episodes = 100000
    iteration = 0
    for _ in range(100000):
        field = Field(field_size, item_pickup, item_drop_off, start_position)
        done = False
        
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
        iteration += 1
        percentage = (iteration / total_episodes) * 100

        if iteration % (total_episodes // 100) == 0:
            print(f"Training Completed: {percentage:.2f}%")    

    print("Training completed in Total", steps, "steps")

    print("Final Q-Table Values")
    print(q_table)
    np.save("q_table.npy", q_table)