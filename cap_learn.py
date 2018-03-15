import time
import gym
import gym_cap
import numpy as np

env = gym.make("cap-v0")
#observation = env.reset(0) # debug if you don't want random generated map

start_time = time.time()
done = False
step = 0
iteration = 0


while iteration < 100:
    
    ## list of randomly generated actions can be generated like that
#    action = env.action_space.sample()  # choose random action
    
    ## to make only one unit doing action use that
    action = [np.random.randint(0,5),4,4,4,4,4]
    
    ## actions 0=Up, 1=Right, 2=Down, 3=Left, 4=Stay
#    print("Actions selected:",action) 
    
    observation, reward, done, info = env.step(action)  # feedback from environment
    
    ## example of the data that you may use to solve the problem
#    print(observation) # print observation as a matrix (coded map)
    
#    xa, ya = env.team1[0].get_loc() #location of unit 0 in list of friendly units
#    print("Unit 0 location:",xa,ya)
#    print("Unit 0 is a UAV:", env.team1[0].air)
#    print("Unit 0 on the map is given by:",observation[ya][xa])
        
    ## ANIMATION (if you want to see what is going on)
    env.render(mode="obs") #obs, obs2,  or env
    ##watch the complete environment (you cannot use it to find a solution)
#    env.render(mode="env") 
    time.sleep(0.5) #remove sleep if you don't want to watch the animation
    
    step += 1
    if step == 1000 or done:
        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        env.reset()
        step = 0
        iteration += 1        
