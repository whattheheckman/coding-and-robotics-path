/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       Nathan Brown                                              */
/*    Created:      Wed Feb 12 2020                                           */
/*    Description:  Group 3 Competition Code                                  */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// LeftDrive            motor         1               
// RightDrive           motor         2               
// RightLift            motor         3               
// LeftLift             motor         5               
// Clamp                motor         4               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"
using namespace vex;
competition Competition;

int liftSpeedPCT = 40;   // Lift lift speed
int clampPCT = 50;       // how fast the clamp moves
float joyspeedMod = .80; // joystick modifier

void pre_auton(void) { vexcodeInit(); }

void autonomous(void) {
  LeftDrive.spin(vex::directionType::rev, 60, vex::velocityUnits::pct);
  RightDrive.spin(vex::directionType::rev, 60, vex::velocityUnits::pct);
  vex::this_thread::sleep_for(3000);
  LeftDrive.spin(vex::directionType::fwd, 60, vex::velocityUnits::pct);
  RightDrive.spin(vex::directionType::fwd, 60, vex::velocityUnits::pct);
  vex::this_thread::sleep_for(1500);
}

void usercontrol(void) {
  // User control code here, inside the loop
  while (1) {
    LeftDrive.spin(
        vex::directionType::fwd,
        ((Controller1.Axis3.value() * joyspeedMod) + Controller1.Axis1.value()),
        vex::velocityUnits::pct); //(Axis3+Axis1)/2
    RightDrive.spin(
        vex::directionType::fwd,
        ((Controller1.Axis3.value() * joyspeedMod) - Controller1.Axis1.value()) ,
        vex::velocityUnits::pct);

    if (Controller1.ButtonL2.pressing()) {
      LeftLift.spin(vex::directionType::fwd, liftSpeedPCT,
                    vex::velocityUnits::pct);
      RightLift.spin(vex::directionType::fwd, liftSpeedPCT,
                     vex::velocityUnits::pct);

    } else if (Controller1.ButtonL1.pressing()) {
      LeftLift.spin(vex::directionType::rev, liftSpeedPCT,
                    vex::velocityUnits::pct);
      RightLift.spin(vex::directionType::rev, liftSpeedPCT,
                     vex::velocityUnits::pct);
    } else {
      LeftLift.stop(vex::brakeType::hold);
      RightLift.stop(vex::brakeType::hold);
    }
    // CLAMP
    if (Controller1.ButtonR1.pressing()) {
      Clamp.spin(vex::directionType::fwd, clampPCT, vex::velocityUnits::pct);
    } else if (Controller1.ButtonR2.pressing()) {
      Clamp.spin(vex::directionType::rev, clampPCT, vex::velocityUnits::pct);
    } else {
      Clamp.stop(vex::brakeType::hold);
    }
  }
}

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
