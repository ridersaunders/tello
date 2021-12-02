from djitellopy import Tello
from time import sleep
from djitellopy import tello
from time import sleep

tello = tello.Tello()

tello.connect()


tello.takeoff()
tello.send_rc_control(0, 50, 0, 0)
sleep(2)
tello.send_rc_control(0, 0, 0, 30)
sleep(2)
tello.send_rc_control(0, 0, 0, 0)
tello.land()

