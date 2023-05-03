'''
Julian Patterson 2131249
420-LCU Computer Programming
May 5th, 2023
S. Hilal, instructor
Assignment 4
'''
import matplotlib.pyplot as plt

# First graph of desktop environments:
Desktop_Environments = ["Gnome", "KDE5", "Unknown","KDE4","XFCE", "X-Cinnamon", "MATE", "KDE", "Cinnamon", "LXQt"]  
Amount_of_Users = [72974, 34405,22909,18297,11979,10867,4855,4483,2433,2096]

plt.bar(Desktop_Environments, Amount_of_Users)
plt.xlabel("Desktop Environment")
plt.ylabel("Amount of Computers")
plt.title("Amount of Users per Different Desktop Environments")
plt.show()

# Second graph of desktop operating system market share:
Operating_System = ["Windows", "OS X", "Linux", "Unknown", "ChromeOS", "iOS", "Android", "Playstation", "Other"]
Percentages = [88.12,8.7,1.19,1.18,0.33,0.29,0.1,0.05,0.03]

plt.pie(x=Percentages, labels=Operating_System, autopct="%1.1f%%")
plt.title("Desktop Operating System Market Share")
plt.show()
# problem with titles being too close