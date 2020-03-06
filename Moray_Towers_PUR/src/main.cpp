/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       Nathan Brown                                              */
/*    Created:      Wed Feb 12 2020                                           */
/*    Description:  Group 3 Two Minute Autonomous Purple Cubes                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// LeftDrive            motor         1               
// RightDrive           motor         2               
// RightLift            motor         3               
// Clamp                motor         4               
// LeftLift             motor         5               
// VisSense             vision        6               
// LimitSwitchA         limit         A               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"
using namespace vex;
competition Competition;

int liftSpeedPCT = 50; // Lift lift speed
int clampPCT = 65;     // how fast the clamp moves
float joyspeedMod = 1; // joystick modifier

void pre_auton(void) { vexcodeInit(); }

void autonomous(void) {
  int centerFOV = 158;
  int offsetX =
      15; // Increase or decrease this balue to adjust precision of the turn

  while (true) {
    Brain.Screen.clearLine();
    VisSense.takeSnapshot(VisSense__PURPUR); // Change Based on the name of the
                                         // block

    // If there is a matching color
    if (VisSense.largestObject.exists) {
      if (VisSense.largestObject.centerX > centerFOV + offsetX) {
        LeftDrive.spin(directionType::rev, 20,
                     velocityUnits::pct); // Please Change Motor Name based on
                                          // your motor name
        RightDrive.spin(directionType::fwd, 20, velocityUnits::pct);

      } else if (VisSense.largestObject.centerX < centerFOV - offsetX) { 
        LeftDrive.spin(directionType::fwd, 20, velocityUnits::pct);
        RightDrive.spin(directionType::rev, 20, velocityUnits::pct);
      } else {
        LeftDrive.stop(brakeType::brake);
        RightDrive.stop(brakeType::brake);
      }
    }
  }

}

void usercontrol(void) {}

//
// Main will set up the competition functions and callbacks.
//
int main() {
  // Set up callbacks for autonomous and driver control periods.
  Competition.autonomous(autonomous);
  Competition.drivercontrol(usercontrol);
  pre_auton();

  // Prevent main from exiting with an infinite loop.
  while (true) {
    wait(100, msec);
  }
}
