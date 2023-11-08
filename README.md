# # Import the gym module
import gym
# required to display the environment in the notebook
from IPython.display import display, clear_output
from PIL import Image

# Helper function to display an image in Jupyter notebook
def show_array(arr):
img = Image.fromarray(arr, 'RGB')
display(img)

# Create the environment
env = gym.make('CartPole-v1')

# Reset the environment
observation = env.reset()

done = False
# Run the simulation for x steps
num_steps = 1000
for i in range(num_steps):
# Take a random action
action = env.action_space.sample()

    # Get the new state and reward from the environment
    observation, reward, done, info = env.step(action)

    # Render the current frame as an rgb array
    frame = env.render(mode='rgb_array')
    # Clear the previous output and display the new frame
    clear_output(wait=True)
    show_array(frame)

    # If the episode is done, reset the environment
    if done:
        observation = env.reset()

# close the environment
env.close()

