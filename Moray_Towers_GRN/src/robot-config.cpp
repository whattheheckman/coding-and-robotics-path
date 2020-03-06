#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
controller Controller1 = controller(primary);
motor LeftDrive = motor(PORT1, ratio18_1, false);
motor RightDrive = motor(PORT2, ratio18_1, true);
motor RightLift = motor(PORT3, ratio18_1, false);
motor Clamp = motor(PORT4, ratio18_1, false);
motor LeftLift = motor(PORT5, ratio18_1, true);
/*vex-vision-config:begin*/
signature VisSense__PURPUR = signature (1, 1353, 2657, 2005, 7519, 11377, 9448, 3.5, 0);
signature VisSense__ORG = signature (2, 8837, 10281, 9559, -2133, -1607, -1870, 2.5, 0);
signature VisSense__GRN = signature (3, -8623, -5461, -7042, -3277, -1833, -2555, 3, 0);
vision VisSense = vision (PORT6, 62, VisSense__PURPUR, VisSense__ORG, VisSense__GRN);
/*vex-vision-config:end*/
limit LimitSwitchA = limit(Brain.ThreeWirePort.A);

// VEXcode generated functions
// define variable for remote controller enable/disable
bool RemoteControlCodeEnabled = true;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Text.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  // nothing to initialize
}