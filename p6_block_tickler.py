"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":0},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":null,"bufferIndex":1}]}"""
import vex
import sys

#region config
brain         = vex.Brain()
left_Wheel    = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
right_Wheel   = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, False)
lyft          = vex.Motor(vex.Ports.PORT3, vex.GearSetting.RATIO18_1, False)
top_Left      = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, False)
top_Right     = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO18_1, True)
left_Tickler  = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO18_1, False)
right_Tickler = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO18_1, False)
dt            = vex.Drivetrain(top_Left, top_Right, 319.1764, 292.1, vex.DistanceUnits.MM)
con           = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

# main thread
while True:
  right_Wheel.spin(vex.DirectionType.FWD, (con.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
  left_Wheel.spin(vex.DirectionType.FWD, (con.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
  if con.buttonUp.pressing():
    lyft.spin(vex.DirectionType.FWD, 40, vex.VelocityUnits.RPM)
  lyft.stop(vex.BrakeType.BRAKE)
  if con.buttonDown.pressing():
    lyft.spin(vex.DirectionType.REV, 40, vex.VelocityUnits.RPM)
  lyft.stop(vex.BrakeType.BRAKE)
  if con.buttonX.pressing():
    dt.drive(vex.DirectionType.FWD)
  if con.buttonR2.pressing():
    left_Tickler.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
    right_Tickler.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
  left_Tickler.stop(vex.BrakeType.BRAKE)
  right_Tickler.stop(vex.BrakeType.BRAKE)


