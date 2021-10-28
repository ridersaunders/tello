from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_up(182)

sleep(2)
tello.move_foward(304)

sleep(2)
tello.move_left(304)

sleep(2)
tello.move_back(304)

sleep(2)
tello.move_right(304)

sleep(2)
tello.flip_back()

sleep(2)
tello.land()
