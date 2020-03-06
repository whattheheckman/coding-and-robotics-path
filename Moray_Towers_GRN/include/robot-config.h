using namespace vex;

extern brain Brain;

using signature = vision::signature;

// VEXcode devices
extern controller Controller1;
extern motor LeftDrive;
extern motor RightDrive;
extern motor RightLift;
extern motor Clamp;
extern motor LeftLift;
extern signature VisSense__PURPUR;
extern signature VisSense__ORG;
extern signature VisSense__GRN;
extern signature VisSense__SIG_4;
extern signature VisSense__SIG_5;
extern signature VisSense__SIG_6;
extern signature VisSense__SIG_7;
extern vision VisSense;
extern limit LimitSwitchA;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Text.
 * 
 * This should be called at the start of your int main function.
 */
void  vexcodeInit( void );