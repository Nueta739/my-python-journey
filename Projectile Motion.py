import math

def projectile_motion(velocity,angle,height = 0, g = 9.81 ):
    angle = math.radians(angle)
    flight_time = round((2 * velocity * math.sin(angle))/g,2)
    range_of_flight = round(velocity * math.cos(angle) * flight_time,2)
    maximum_height = round(((velocity*math.sin(angle))**2)/(2*g),2)


    if height != 0:
        maaximum_height += height
#To be finished

    print(f"Time of flight: {flight_time}s")
    print(f"Range of flight: {range_of_flight}m/s")
    print(f"Maximum height: {maximum_height}m")



#to implement height arguement
