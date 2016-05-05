import gym


# What gets called
def act(observation, reward, done):
    
    #debugging
    print observation
    myAction = 0
    if(observation[3] < -.15):
        myAction = 0
    
    if(observation[3] > .15):
        myAction = 1
    
    print myAction
    action = myAction
    
    #print(action)

    return action

env = gym.make('CartPole-v0')
#env.monitor.start('tmp/cartpole-experiment-1')
for i_episode in xrange(20):
    observation = env.reset()
    reward = 0
    done = False
    
    for t in xrange(100):
        env.render()
        #print observation
        action = act(observation, reward, done)
        observation, reward, done, info = env.step(action)
        if done:
            print "Episode finished after {} timesteps ".format(t+1)
            break

#env.monitor.close()
