#input motion parameters initial velocity, acceleration, maximum velocity

while True: #loop to obtain only valid input for motion parameters
    try :
        while True: #loop to obtain only positive input for motion parameters
            vi = float(input("Enter the initial velocity of the rover : "))
            a = float(input("Enter the acceleration of the rover : "))
            vmax = float(input("Enter the maximum velocity of the rover : "))
            if a <= 0 or vmax <= 0 or vi < 0:
                print("motion parameters must  must be positive. Please enter valid values.")
            else:
                break
        break
    except ValueError:
        print("Invalid input. Please enter correct values for motion parameters")


#input coordinates of the rover

while True: #loop to obtain only valid input for coordinates
    try:
            #input starting coordinates x and y of rover
            xi = float(input("Enter the initial coordinates x : "))
            yi = float(input("Enter the initial coordinates y : "))
            #input final coordinates x and y of rover
            xf = float(input("Enter the final coordinates x : "))
            yf = float(input("Enter the final coordinates y : "))
            break
    except ValueError:
        print("Invalid input. Please enter correct values for coordinates")

#caculating the distance covered by the rover using the distance formula
distance =  ((yf-yi)**2+((xf-xi)**2))**0.5
print("The total distance covered by the rover : " ,distance)

#cacluating the final velocity of the rover
vf = (vi**2 + 2*a*distance)**0.5

#checking if the final velocity exceeds the maximum velocity
if vf > vmax:
    vf = vmax
    dmax = (vf**2 - vi**2) / (2*a)  #calculating the distance at which final velocity  becomes maximum velocity
    t1 = (vf - vi) / a #time taken to reach maximum velocity
    t2 = (distance - dmax) / vf #after reaching maximum velocity , no more accelaration so the time =  distance/speed
    t= t1 + t2 #calculating the time taken to reach the destination

else:
    t = (vf - vi) / a #calculating the time taken to reach the 

print("The time taken to reach the destination : " ,t)
print("The final velocity of the rover : " ,vf)
