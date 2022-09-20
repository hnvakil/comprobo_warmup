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

In this project, we began our journey towards familiarity with ROS, in-person Neatos, and how to make these all work together through a series of executable tasks. We created the following behaviors for our robot: teleoperation, driving in a square, following the wall, following a person, and avoiding obstacles. We took a range of approaches to these problems individually, and brought them together through a finite state machine that allows the user to specify behavior.

## Debugging
@hnvakil
Throughout this proccess, we needed tools to see what we were doing

// screenshots of visualization

## Behaviors
### Teleop

@allybbell
Our first contoller for the Neato was a way for us to drive it from our laptops. This mechanism allows a user to input keys that translate to the robots rotation and driving. 


### Square
@allybbell
The first autonomous behavior we developed for our robot was to drive in a square. The Neato drove this square based on a timer, in which a timer would start on initialization, drive the robot straight for a set amount of time, rotate the Neato ninety degrees, reset the timer, and begin again.

### Wall Following
@allybbell
In this behavior, the Neato drives parallel to a wall. It does this by looking for the nearest point (which we assume to be a wall) and adjust its heading to be perpendicular to the heading of this point. When it is aligned with the wall (the point closest to it) within a set margin of error, it drives straight along the wall.

// maybe logic diagram
// maybe viz for wall follow @hnvakil


### Person Following
Person following works very simillarly to wall following, where the Neato assumes the closest point to be the person it's supposed to follow.

//maybe logic diagram
//maybe viz for person follow @hnvakil

### Obstacle Avoidance
@hnvakil

## Finite State Machine
@allybbell
A classic way to bring seperate robot states together is through a finite state machine, which serves as a mechanism to switch the robot between discrete behaviors. To explore this approach, we made a finite state machine that 


## Code Structure


## Challenges

## Potential Improvements

## Key Takeaways
As we neared the end of this project, we wanted to combine all of our behaviors into one Node that could switch between the modes we had created based on key inputs.