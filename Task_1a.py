#input starting coordinates x and y of rover
xi = int(input("Enter the initial coordinates x : "))
yi = int(input("Enter the initial coordinates y : "))

#input final coordinates x and y of rover
xf = int(input("Enter the final coordinates x : "))
yf = int(input("Enter the final coordinates y : "))

#caculate the distance covered by the rover using the distance formula
distance =  ((yf-yi)**2+((xf-xi)**2))**0.5
print("The total distance covered by the rover : " ,distance)



