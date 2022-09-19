### Computational Robotics 2022

# Warmup Project
#### Han Vakil and Ally Bell

In this project, we began our journey towards familiarity with ROS, in-person Neatos, and how to make these all work together through a series of executable tasks. We created the following behaviors for our robot: teleoperation, driving in a square, following the wall, following a person, and avoiding obstacles. We took a range of approaches to these problems individually, and brought them together through a finite state machine that allows the user to specify behavior.

## Debugging
Throughout this proccess, we needed tools to see what we were doing

## Teleop
Our first contoller for the Neato was a way for us to drive it from our laptops. This mechanism allows a user to input keys that translate to the robots rotation and driving. 


## Square
The first autonomous behavior we developed for our robot was to drive in a square. The Neato drove this square based on a timer, in which a timer would start on initialization, drive the robot straight for a set amount of time, rotate the Neato ninety degrees, reset the timer, and begin again.

## Wall Following
In this behavior, the Neato drives parallel to a wall. It does this by looking for the nearest point (which we assume to be a wall) and adjust its heading to be perpendicular to the heading of this point. When it is aligned with the wall (the point closest to it) within a set margin of error, it drives straight along the wall.


## Person Following
Person following works very simillarly to wall following, where the Neato assumes the closest point to be the person it's supposed to follow.

## Obstacle Avoidance

## Finite State Machine
A classic way to bring seperate robot states together is through a finite state machine, which serves as a mechanism to switch the robot between discrete behaviors.  


## Code Structure

## Challenges

## Potential Improvements

## Key Takeaways