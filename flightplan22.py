from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()
print(tello.get_battery())

tello.takeoff()
tello.move_up(161)
sleep(2)

tello.move_forward(152)
sleep(2)
tello.rotate_counter_clockwise(90)
sleep(2)
tello.move_forward(182)
sleep(2)
tello.rotate_clockwise(90)
sleep(2)
tello.move_down(91)
sleep(2)
tello.move_forward(91)
sleep(2)
tello.rotate_clockwise(90)
sleep(2)
tello.move_up(30)
sleep(2)
tello.move_forward(91)
sleep(2)
tello.rotate_counter_clockwise(90)
sleep(2)
tello.move_forward(182)
sleep(2)
