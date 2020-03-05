"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"1","name":"rearLeft","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":0},{"hwid":"2","name":"rearRight_","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":1},{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":2},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"1","rightMotorHwId":"2","wheelTravel":319.1764,"trackWidth":320.675},"bufferIndex":3},{"hwid":"controller","name":"con","typeName":"controller_one","extraConfig":null,"bufferIndex":4},{"hwid":"Axis1","name":"axis1","typeName":"controller_axis","extraConfig":null,"bufferIndex":5},{"hwid":"Axis2","name":"axis2","typeName":"controller_axis","extraConfig":null,"bufferIndex":6},{"hwid":"Axis3","name":"axis3","typeName":"controller_axis","extraConfig":null,"bufferIndex":7},{"hwid":"Axis4","name":"axis4","typeName":"controller_axis","extraConfig":null,"bufferIndex":8},{"hwid":"ButtonL1","name":"buttonL1","typeName":"controller_button","extraConfig":null,"bufferIndex":9},{"hwid":"ButtonL2","name":"buttonL2","typeName":"controller_button","extraConfig":null,"bufferIndex":10},{"hwid":"ButtonR1","name":"buttonR1","typeName":"controller_button","extraConfig":null,"bufferIndex":11},{"hwid":"ButtonR2","name":"buttonR2","typeName":"controller_button","extraConfig":null,"bufferIndex":12},{"hwid":"ButtonUp","name":"buttonUp","typeName":"controller_button","extraConfig":null,"bufferIndex":13},{"hwid":"ButtonDown","name":"buttonDown","typeName":"controller_button","extraConfig":null,"bufferIndex":14},{"hwid":"ButtonLeft","name":"buttonLeft","typeName":"controller_button","extraConfig":null,"bufferIndex":15},{"hwid":"ButtonRight","name":"buttonRight","typeName":"controller_button","extraConfig":null,"bufferIndex":16},{"hwid":"ButtonX","name":"buttonX","typeName":"controller_button","extraConfig":null,"bufferIndex":17},{"hwid":"ButtonB","name":"buttonB","typeName":"controller_button","extraConfig":null,"bufferIndex":18},{"hwid":"ButtonY","name":"buttonY","typeName":"controller_button","extraConfig":null,"bufferIndex":19},{"hwid":"ButtonA","name":"buttonA","typeName":"controller_button","extraConfig":null,"bufferIndex":20}]}"""
# VEX V5 Python Project
import sys
import vex
from vex import *

#region config
brain      = vex.Brain()
rearLeft   = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, True)
rearRight_ = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, False)
dt         = vex.Drivetrain(rearLeft, rearRight_, 319.1764, 320.675, vex.DistanceUnits.MM)
con        = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

#code
rearLeft.stop(vex.BrakeType.COAST)
rearRight_.stop(vex.BrakeType.COAST)
dt.drive_for(vex.DirectionType.FWD, 100, vex.DistanceUnits.CM, 90, vex.VelocityUnits.PCT)
rearLeft.stop(vex.BrakeType.COAST)
rearRight_.stop(vex.BrakeType.BRAKE)
rearLeft.rotate_for_time(vex.DirectionType.FWD, 1.5, vex.TimeUnits.SEC, 75,vex.VelocityUnits.PCT)
dt.drive_for(vex.DirectionType.FWD, 50, vex.DistanceUnits.CM, 75, vex.VelocityUnits.PCT)
rearRight_.rotate_for_time(vex.DirectionType.FWD, 1.5, vex.TimeUnits.SEC, 75,vex.VelocityUnits.PCT)
rearLeft.stop(vex.BrakeType.COAST)
dt.drive_for(vex.DirectionType.FWD, 40, vex.DistanceUnits.CM, 75, vex.VelocityUnits.PCT)
rearLeft.stop(vex.BrakeType.COAST)
rearRight_.stop(vex.BrakeType.BRAKE)
rearLeft.rotate_for_time(vex.DirectionType.FWD, .75, vex.TimeUnits.SEC, 75,vex.VelocityUnits.PCT)
dt.drive_for(vex.DirectionType.FWD, 40, vex.DistanceUnits.CM, 75, vex.VelocityUnits.PCT)
rearLeft.stop(vex.BrakeType.COAST)
rearRight_.stop(vex.BrakeType.BRAKE)
rearLeft.rotate_for_time(vex.DirectionType.FWD, 1, vex.TimeUnits.SEC, 50,vex.VelocityUnits.PCT)
dt.drive_for(vex.DirectionType.FWD, 125, vex.DistanceUnits.CM, 80, vex.VelocityUnits.PCT)
rearLeft.stop(vex.BrakeType.COAST)
rearRight_.stop(vex.BrakeType.BRAKE)
rearLeft.rotate_for_time(vex.DirectionType.FWD, .75, vex.TimeUnits.SEC, 75,vex.VelocityUnits.PCT)
dt.drive_for(vex.DirectionType.FWD, 110, vex.DistanceUnits.CM, 85, vex.VelocityUnits.PCT)
rearLeft.stop(vex.BrakeType.BRAKE)
rearRight_.stop(vex.BrakeType.BRAKE)
rearLeft.rotate_for_time(vex.DirectionType.FWD, .75, vex.TimeUnits.SEC, 50,vex.VelocityUnits.PCT)
dt.drive_for(vex.DirectionType.FWD, 75, vex.DistanceUnits.CM, 100, vex.VelocityUnits.PCT)






 
 
 
 
 
 
