import math
import numpy as np
import matplotlib.pyplot as plt

v = float(input('Enter the projectiles initial speed: '))
while v <= 0:
    v = float(input('Enter a speed greater than 0: '))
ang = float(input('Enter the projectiles initial angle: '))
while ang > 90 or ang <-90:
    ang = float(input('Enter an initial angle above -90 and below 90 degrees: '))
h = float(input('Enter the projectiles initial height: '))
while h < 0:
    h = float(input('Enter a height above 0 Metres: '))

def projectile_motion(v,ang,h,g = 9.81 ):
    ang = math.radians(ang)

    flight_time = (1/g)*((v * math.sin(ang))+math.sqrt((v*math.sin(ang))**2+(2*g*h)))
    range_of_flight = v * math.cos(ang) * flight_time
    maximum_height = (((v*math.sin(ang))**2)/(2*g))+ h

    stats_text = (
        f"Max height: {maximum_height:.2f}m\n"
        f"Range: {range_of_flight:.2f}m\n"
        f"Flight time: {flight_time:.2f}s\n"
                  )
    def x(t):
        return (v * math.cos(ang))*t
    def y(t):
        return (v * math.sin(ang))*t - 1/2*g*(t**2) + h

    t=np.linspace(0,flight_time,400)

    plt.plot(x(t),y(t))
    plt.xlabel('Horizontal displacement')
    plt.ylabel('Vertical displacement')
    plt.title('Projectile Motion')
    plt.grid(True)
    plt.ylim(bottom = 0,top = maximum_height + 1)
    plt.xlim(left = 0)
    plt.text(0,maximum_height + 1,stats_text)
    plt.show()


projectile_motion(v,ang,h)

