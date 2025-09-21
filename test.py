import time
import random
from polytopia import PolytopiaEnv

# Initialize environment
env = PolytopiaEnv()
#obs, info = env.reset()

# Render initial state
env.render()

# Run a few random steps
# for step in range(10):
#     action = env.action_space.sample()
#     obs, reward, done, truncated, info = env.step(action)
#     print(f"Step {step+1}: Action={action}, Reward={reward}")
#     env.render()
t = time.time()
print (env.actions.getMoves(1,1))
print (env.actions.move(1,1,2,2))
print (env.actions.move(2,2,3,3))
print (env.actions.move(3,3,4,4))

print (env.actions.move(7,7,6,6))
print (env.actions.move(6,6,5,5))


env.actions.attack(4,4,5,5)

print(env.board[4][4].unit.health)
print(env.board[5][5].unit.health)

env.actions.attack(4,4,5,5)
print(env.board[4][4].unit.health)
print(env.board[5][5].unit.health)

env.actions.attack(4,4,5,5)
print(env.board[4][4].unit.health)

env.render()
print (time.time()-t)