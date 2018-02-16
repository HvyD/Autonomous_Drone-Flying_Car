
# coding: utf-8

# In[1]:


from udacidrone import Drone
from udacidrone.connection import MavlinkConnection
conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded=True)
drone = Drone(conn)
drone.start()


# In[2]:


drone.take_control()
drone.arm()


# In[3]:


drone.set_home_position(drone.global_position[0], 
                        drone.global_position[1], 
                        drone.global_position[2])


# In[5]:


drone.takeoff(30)


# In[7]:


drone.cmd_position(5,5,5,5)


# In[9]:


drone.stop()

