from robolink import *	# API to communicat with RoboDK
from robodk import * 	# basic matrix operations

# Any interaction with RoboDK must be done through
# Robolink()
RL = Robolink()

# get the robot item:
robot = RL.Item("KUKA KR 6 R900 sixx")

# get the home target and the welding target(s):
home = RL.Item('Home')
target = RL.Item('Target')

# get the pose of the target in the form of a 4x4 matrix:
poseref = target.Pose()

# move the robot to home, then to the center:
robot.MoveJ(home)
robot.MoveJ(target)

# make a hexagon around the center of the target:
for i in range(7):
	ang = i*2*pi/6 # angle: 0, 60, 120, ..., 360
	posei = poseref*rotz(ang)*transl(200, 0, 0)*rotz(-ang)
	robot.MoveL(posei)

# moveb ack to the center of the target and then finally back to the home position:
robot.MoveL(target)
robot.MoveJ(home)