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
print (env.actions.getAttacks(1,1))

print (time.time()-t)