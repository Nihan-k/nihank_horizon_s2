#input motion parameters : initial velocity, acceleration,  max velocity
vi = int(input("Enter the initial velocity of the rover : "))
a = int(input("Enter the acceleration of the rover : "))
vmax = int(input("Enter the maximum velocity of the rover : "))

#input starting coordinates x and y of rover
xi = int(input("Enter the initial coordinates x : "))
yi = int(input("Enter the initial coordinates y : "))

#input starting coordinates x and y of rover
xf = int(input("Enter the final coordinates x : "))
yf = int(input("Enter the final coordinates y : "))

#caculate the distance covered by the rover using the distance formula
distance =  ((yf-yi)**2+((xf-xi)**2))**0.5
print("The total distance covered by the rover : " ,distance)

#calculating the final velocity of the rover
vf = (vi**2 + 2*a*distance)**0.5

#checking if the final velocity exceeds the maximum velocity
if vf > vmax:
    vf=vmax
print("The final velocity of the rover is : ",vf)

#calculating the time taken by the rover to cover the distance
t = (vf-vi)/a
print("The time taken by the rover to cover the distance is : ",t)

