# Webots-ACC
Implementation of adaptive cruise control on Webots for automobile 

python version >= 3.10 required

------------------------------------------------------------

Scenario of the simulation: 

We have 2 vehicles: 
- a red car with keyboard control 
- a grey car that integrates the ACC system 

The user has the control of the red car with the directional keys of the keyboard and he can also increase the speed with the numeric pad (1 for 10km/h, 2 for 20 km/h, etc...)
The goal is to accelerate and see the reactivity of the regulator at different speeds.  

------------------------------------------------------------
The system is implemented on a Tesla Model 3 PROTO using a controller coded in python that a simple PID regulator to keep the car at a certain distance while keeping constant speed set by the user 

The second car in the simulation is controlled using keyboard with the follwing keys :
- UP Arrow : Go Forward 
- DOWN Arrow : Go Backward 
- LEFT Arrow : Turn Left
- RIGHT Arrow : Turn Right
      
you can select the speed of the car using numpad keys (1 for 10km/h, 2 for 20km/h and so on up to 6)


----------------------------------------------------------------
<iframe width="1280" height="720" src="https://www.youtube.com/embed/ihZa0MVYdrQ" title="Adaptatif Cruise Control ( ACC ) - Webots for Automobile" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      
