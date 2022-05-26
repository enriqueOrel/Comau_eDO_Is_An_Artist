# Comau_eDO_Is_An_Artist
This is a project, which consists of generating from any svg image a path which is followed by a robotic arm
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
I would like to start by saying:

Thank you very much for your interest in this project, We wanted to share it with the community

I am new in the programming world and this is one of our first projects in python. If you have any suggestions on how to improve it We would be very grateful for your collaboration!

this section contains a python script, based on the API RoboDK which through is possible to simulate the movements of the robotic Arm, you can find an example of the simulation in this repository, an is possible to try it online right here:

https://web.robodk.com/web

Just open the script with a text editor add the path of the svg file, adjust the position of the Uframe and Tool in the simulator if the robot is able to execute the  movements, the generated .txt file is ready to post-process.

In the post processor file you find a script which generates the coordinates for the robot movements in PDL2 language of the Comau robots, 
is necessary to add the tool a UFrame according to the position in the simulation

