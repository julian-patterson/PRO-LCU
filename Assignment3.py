'''
Julian Patterson 2131249
420-LCU Computer Programming
May 5th, 2023
S. Hilal, instructor
Assignment 4
'''
import matplotlib.pyplot as plt

# First graph of desktop environments:
Desktop_Environments = ["Gnome", "KDE5", "Unknown", "KDE4",
                        "XFCE", "X-Cinnamon", "MATE", "KDE", "Cinnamon", "LXQt"]
Amount_of_Users = [72974, 34405, 22909, 18297,
                   11979, 10867, 4855, 4483, 2433, 2096]

plt.bar(Desktop_Environments, Amount_of_Users)
plt.xlabel("Desktop Environment")
plt.ylabel("Amount of Computers")
plt.title("Amount of Users per Different Desktop Environments")
plt.show()

# Second graph of desktop operating system market share:
Operating_System = ["Windows", "OS X", "Linux", "Unknown",
                    "ChromeOS", "iOS", "Android", "Playstation", "Other"]
Percentages = [88.12, 8.7, 1.19, 1.18, 0.33, 0.29, 0.1, 0.05, 0.03]

plt.pie(x=Percentages, labels=None)
plt.title("Desktop Operating System Market Share")
plt.legend(loc="lower center", ncol=5, frameon=True, labels=Operating_System)
plt.show()
# problem with titles being too close

# Third graph of supercomputer operating systems:
Operating_System2 = ["Linux", "Mixed",
                     "BSD Based", "MacOS", "N/A", "Unix", "Windows"]
Dates = ["November 1st 2001", "June 1st 2008", "November 1st 2021"]
November1st2001 = [39, 0, 12, 0, 5, 443, 1]
June1st2008 = [427, 40, 1, 2, 0, 26, 4]
November1st2021 = [500, 0, 0, 0, 0, 0, 0]
Linux = [39, 427, 500]
Mixed = [0, 40, 0]
BSD_Based = [12, 1, 0]
MacOS = [0, 2, 0]
nA = [5, 0, 0]
Unix = [443, 26, 0]
Windows = [1, 4, 0]

fig, ax = plt.subplots()
ax.plot(Dates, Linux, label="Linux")
ax.plot(Dates, Mixed, label="Mixed")
ax.plot(Dates, BSD_Based, label="BSD Based")
ax.plot(Dates, MacOS, label="MacOS")
ax.plot(Dates, nA, label="N/A")
ax.plot(Dates, Unix, label="Unix")
ax.plot(Dates, Windows, label="Windows")
ax.legend()

plt.show()
