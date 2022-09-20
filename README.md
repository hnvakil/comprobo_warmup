### Computational Robotics 2022

# Warmup Project
#### Han Vakil and Ally Bell

For each behavior, describe the problem at a high-level. Include any relevant diagrams that help explain your approach.  Discuss your strategy at a high-level and include any tricky decisions that had to be made to realize a successful implementation.
For the finite state controller, what was the overall behavior. What were the states? What did the robot do in each state? How did you combine and how did you detect when to transition between behaviors?  Consider including a state transition diagram in your writeup.
How was your code structured? Make sure to include a sufficient detail about the object-oriented structure you used for your project.
What if any challenges did you face along the way?
What would you do to improve your project if you had more time?
What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.

@allybbell

In this project, we began our journey towards familiarity with ROS, in-person Neatos, and how to make these all work together through a series of executable tasks. We created the following behaviors for our robot: teleoperation, driving in a square, following the wall, following a person, and avoiding obstacles. We took a range of approaches to these problems individually, and implemented a finite state machine using some of the autonomous behavious we had developed.

## Code Structure

![Node Structure](https://docs.ros.org/en/foxy/_images/Nodes-TopicandService.gif)

## Debugging
@hnvakil
The project was complicated enough we needed tools to interpret and visualize the effect of the code we wrote. We used a combination of rviz and print-based debugging for this purpose. Print-based debugging was incredibly useful before we were able to get the neato to move or even the environment fully working. We were able to read data from the sensors and interpret it with the neato in place, and drive the neato around with teleop once we got that working and read the sensor input and the results of our logic. Once we had the robot moving, we used rviz to see what the sensors were seeing, as well as just running the robot in a sim. Running rviz let us see how noisy real world data was, and let us know some of our issues were due to faulty sensor input and not bad code.

Print-based debugging was especially helpful when we were doing several layers of interpretation on the sensor input, such as when we listened to a scan, found the closest point and its direction, then had to figure out which way to turn to go the right way. Each step had a different issue to work out, and being able to sit the neato in an area that should generate a certain behavior and print out the direction it wanted to go based on the current code let us troubleshoot and fix errors.

// screenshots of visualization

## Behaviors
### Teleop

@allybbell
Our first contoller for the Neato was a way for us to drive it from our laptops. This mechanism allows a user to input keys that translate to the robots rotation and driving. 


### Square
@allybbell
The first autonomous behavior we developed for our robot was to drive in a square. The Neato drove this square based on a timer, in which a timer would start on initialization, drive the robot straight for a set amount of time, rotate the Neato ninety degrees, reset the timer, and begin again. This autonomous control was simple in the sense that the robot did not have to respond to any inputs from a person or any sensors, and operated on this loop as time as the only state-deciding factor. 

### Wall Following
@allybbell
In this behavior, the Neato drives parallel to a wall. It does this by looking for the nearest point (which we assume to be a wall) and adjust its heading to be perpendicular to the heading of this point. When it is aligned parallel to what we are assuming to be the wall within an allowed margin of error, it drives straight along it. As it drives, it rechecks __, which handles 

// maybe logic diagram
// maybe viz for wall follow @hnvakil


### Person Following
Person following works very simillarly to wall following, where the Neato assumes the closest point to be the person it's supposed to follow. The logic works simillarly, where the bot wants to shift its heading based on the heading of it's closest point. 

//maybe logic diagram
//maybe viz for person follow @hnvakil

### Obstacle Avoidance
@hnvakil

We kept our obstacle avoidance behavior pretty simple, and followed the "potential fields" example in the project description. We started by taking a Lidar scan, then doing some preliminary filtering by setting any reading less than 0.1m or greater than 4m to 200m - large enough the later algorithm would essentially ignore it. Once we'd filtered the data, we took each distance reading and corresponding angle measurement, and used trigonometry to find an "x" and "y" weight for each reading. A smaller distance reading resulted in a larger "pressure" in the opposite direction, and adding up all the pressures gave us a "direction of least resistance". We had the robot turn towards that direction, and once it was within a few degrees of that heading, start driving forward. Since we checked the desired direction every time our run_loop ran, if we overshot we'd immediately stop and start turning towards the next direction of least resistance. In practice, this ended up with the robot slightly overshooting the point furthest from obstacles, and slowly driving around that point, overshooting each time.

We didn't incorporate a "goal direction" like we could have, for the sake of time. To add that, we'd have to implement odometry to an extend we hadn't before, which would take a significantly increased time input. However, we feel we have the concept down from the robotics unit of QEA2.

## Finite State Machine
@allybbell
A classic way to bring seperate robot states together is through a finite state machine, which serves as a mechanism to switch the robot between discrete behaviors. To explore this approach, we made a finite state machine that 


## Challenges

## Potential Improvements
As we neared the end of this project, we wanted to combine all of our behaviors into one Node that could switch between the modes we had created based on key inputs. At first glance, it seemed to us like we could create a node that worked simillarly to the teleop node, and call to the different behaviors we had created for different keys that the user pressed. 

## Key Takeaways
