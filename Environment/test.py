import gym
import gym_duckietown
from IPython.display import display, clear_output
from PIL import Image

# Create the environment
env = gym.make('Duckietown-loop_obstacles-v0')
env.reset()


# Helper function to display an image in Jupyter notebook
def show_array(arr):
    img = Image.fromarray(arr, 'RGB')
    # Make the image smaller to increase the FPS of the notebook
    img = img.resize((320, 240))
    display(img)


# Run the simulation until we're done
done = False
while not done:
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    frame = env.render(mode='rgb_array')

    # Clear the previous output and display the new frame
    clear_output(wait=True)
    show_array(frame)

    if done:
        env.reset()

env.close()