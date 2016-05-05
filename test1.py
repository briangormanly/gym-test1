import gym
import numpy

# What gets called
def act(observation, reward, done):
    
    #debugging
    #print observation
    myAction = 0
    if(observation[3] < -.000002):
        myAction = 0
    
    if(observation[3] > .000002):
        myAction = 1
    
    #print myAction
    action = myAction
    
    #print(action)

    return action

env = gym.make('CartPole-v0')

# store results to average
timestamps = [];

#env.monitor.start('tmp/cartpole-experiment-1')
for i_episode in xrange(20):
    observation = env.reset()
    reward = 0
    done = False
    
    for t in xrange(200):
        env.render()
        #print observation
        #print env.action_space
        action = act(observation, reward, done)
        observation, reward, done, info = env.step(action)
        
        if done:
            timestamps.append(t+1) 
            print "Episode finished after {} timesteps ".format(t+1)
            print "Episode mean timestamp was: {}".format(numpy.mean(timestamps))
            break

#env.monitor.close()
