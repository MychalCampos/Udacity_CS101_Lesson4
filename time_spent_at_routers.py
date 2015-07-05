# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 18:00:45 2015
# how long does the data spend at the routers?
@author: Mychal
"""

# Information given in question
total_time = 75  # in milliseconds (ms)
one_way_distance = 2500.0  # in km 
optic_speed = 200000  # in km/s
ms_per_second = 1000  # number of milliseconds per second


# in ms
time_spent_on_wires = (2 * one_way_distance / optic_speed) * (ms_per_second)  
print time_spent_on_wires
time_spent_on_routers = total_time - time_spent_on_wires
print time_spent_on_routers  
