# First import the gym
import gym
env = gym.make('CartPole-v1')


action = env.action_space.sample() # take a random action
print(action)