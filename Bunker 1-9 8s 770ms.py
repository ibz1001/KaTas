# Bunker 1-9 8.77 made by Bar0ti https://www.youtube.com/watch?v=o9p3WielzR0

from katas import Controller, Scripter

potato = Scripter()
potato.Button(Controller.left_shoulder, duration=0)
potato.Wait(2)
potato.Button(Controller.dpad_down, duration=22)
potato.Roll()
potato.Wait(22)
potato.Roll()
potato.Wait(18)
#ricky slash
potato.Button(Controller.X, duration=0)
potato.Wait(4)
potato.Button(Controller.dpad_down, duration=0)
potato.Roll()
potato.Wait(12)
#door slash
potato.Button(Controller.X, duration=0)
potato.Wait(10)
potato.Button(Controller.dpad_down, duration=2)
potato.Wait(1)
potato.Roll()
potato.Wait(15)
#dropping down slash
potato.MoveLeftStick(220)
potato.Button(Controller.X, duration=0)
potato.Wait(1)
potato.Button(Controller.dpad_down, duration=38)
potato.Button(Controller.dpad_left, duration=16)
potato.Wait(14)
potato.Roll()
potato.Wait(18)
#double gunner slash
potato.MoveLeftStick(180)
potato.Button(Controller.X, duration=0)
potato.Wait(1)
potato.Button(Controller.dpad_right, duration=10)
potato.Wait(5)
potato.Roll()
potato.Wait(14)
#deflect to gain height
potato.MoveLeftStick(90)
potato.Button(Controller.X, duration=0)
potato.Wait(8)
potato.Button(Controller.A, duration=20)
potato.Wait(8)
#last gunner slash onto the platform
potato.MoveLeftStick(145)
potato.Button(Controller.X, duration=0)
potato.Wait(6)
potato.Button(Controller.dpad_down, duration=66)
potato.Roll()
potato.Wait(22)
potato.Button(Controller.dpad_down, duration=1)
potato.Roll()
potato.Wait(22)
potato.MoveLeftStick(180)
potato.Button(Controller.X, duration=0)
potato.Wait(14)
potato.Button(Controller.dpad_down, duration=1)
potato.Roll()
potato.Wait(15)
potato.Button(Controller.Y, duration=0)
potato.Wait(7)
potato.Roll()
potato.Wait(7)
potato.save()
