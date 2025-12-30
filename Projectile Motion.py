import math
import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(velocity,angle,height = 0, g = 9.81 ):
    angle = math.radians(angle)
    flight_time = round((2 * velocity * math.sin(angle))/g,2)
    range_of_flight = round(velocity * math.cos(angle) * flight_time,2)
    maximum_height = round(((velocity*math.sin(angle))**2)/(2*g),2)


    if height != 0:
        maaximum_height += height
#To be finished

    stats_text = (
        f"Max height: {maximum_height:.2f}\n"
        f"Range: {range_of_flight:.2f}\n"
        f"Flight time: {flight_time:.2f}\n"
                  )




    def x(t):
        return (velocity * math.sin(angle))*t
    def y(t):
        return (velocity * math.cos(angle))*t - 1/2*g*(t**2)

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


projectile_motion(10,45)

#to implement height arguement

