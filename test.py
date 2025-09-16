import random
from polytopia.polytopia import PolytopiaEnv

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
print (env.grid[1][1].troop.getMoves(1,1))