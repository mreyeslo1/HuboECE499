#!/usr/bin/env python


import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

# Get the current feed-forward (state) 
[statuss, framesizes] = s.get(state, wait=False, last=False)

#move hips and ankles to shift center of mass to left side 
for i in range(0,11):
	#hips 
	ref.ref[ha.RHR] = 0 - (0.02*i)
	ref.ref[ha.LHR] = 0 - (0.02*i)
	#ankeles 
	ref.ref[ha.RAR] = 0 + (0.02*i)
	ref.ref[ha.LAR] = 0 + (0.02*i)
	r.put(ref)
	time.sleep(1)

time.sleep(5)

#lift the right leg up
for i in range(0,10):
	#whole leg curls up 
	ref.ref[ha.RHP] = -0 - (0.1*i)
	ref.ref[ha.RKN] = 0 + (0.2*i)
	ref.ref[ha.RAP] = -0 - (0.1*i)

	r.put(ref)
	time.sleep(3)

time.sleep(5)

#loop for making hubo go up and down 
while True:
	for i in range(0,7):
#left leg down
		ref.ref[ha.LHP] = -0 - (0.1*i)
		ref.ref[ha.LKN] = 0 + (0.2*i)
		ref.ref[ha.LAP] = -0 - (0.1*i)
		r.put(ref)
		time.sleep(2)
#left leg up 
	for i in range(0,7):
	
		ref.ref[ha.LHP] = -0.7 + (0.1*i)
		ref.ref[ha.LKN] = 1.4 - (0.2*i)
		ref.ref[ha.LAP] = -0.7 + (0.1*i)
		r.put(ref)
		time.sleep(2)

r.close()
s.close()

