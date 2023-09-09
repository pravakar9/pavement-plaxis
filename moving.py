import math


from plxscripting.easy import *

input_port_i = '10000'
input_port_o = '10001'
input_password = 'MfDgR%~%4~?>rSiG'  # PUT YOUR PLAXIS 3D INPUT PASSWORD HERE
save_path = r'C:\Users\TUF\Desktop'
s_i, g_i = new_server('localhost', 10000, password='MfDgR%~%4~?>rSiG')
s_i.new()
g_i.gotostructures()
pointload1=g_i.pointload( 1, 5, 0, "Fz" , -20 )

line1=g_i.line(0, 5, 0 ,10 ,5 ,0 ,)

dec1=g_i.movementfunction()
dec1.setproperties (
    "Name", "dec1",
    "Signal", "Linear",
    "Initialvelocity", 30,
    
    
)

Pointmovement_1=g_i.pointmovement(pointload1)
Pointmovement_1.setproperties(
    "MovementFunction", dec1,
    
)
dec1.setproperties (
    "Acceleration", -2,)