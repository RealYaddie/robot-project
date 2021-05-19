# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox

# The Robolink() module is what is used to interact and communicate with RoboDK
RDK = Robolink()

# Assigning the robot item to a variable
robot = RDK.Item('ABB IRB 1200-5/0.9')

# Using the Robolink module we can get the Home target and the welding target(s)
# from RoboDK and assign them both to a variable
home = RDK.Item('Home')
target = RDK.Item('Target 1')

# Using the Robolink module we are able to get the position of the target in space
# from the RoboDK simulation environment
# in the form of a 4x4 matrix and then we save this to a variable
# get the pose of the target in the form of a 4x4 matrix <- REMOVE
poseref = target.Pose()

# Using the Robolink module we first move the robot arm to the 'Home' position
# and then to the 'Target 1' position
# move the robot to the home position, and then to the center <- REMOVE
robot.MoveJ(home)
robot.MoveJ(target)

# From the RoboDK module we're able to use a message box
# to collect the desired amount of vertices the shape should have from the user
# This can be used to make different shapes including a circle, triangle, square etc.
# Using message box to get number of vertices of the shape <- REMOVE
num_vertices = mbox("Enter then number of vertices", entry=True)
num_vertices = int(num_vertices)

# Using both the RoboDK and the Robolink  module we're able to 
# make a hexagon shape around the center of the selected target:
for i in range(num_vertices+1):
    ang = i*2*pi/num_vertices      # angle: 0, 60, 120, ..., 360
    posei = poseref*rotz(ang)*transl(300, 0, 0)*rotz(-ang)
    robot.MoveL(posei)

# Finally we move the robot arm back to the target position and then to the home
# position and the program ends here.
robot.MoveL(target)
robot.MoveJ(home)
