distro = "fedora"
# string is immutable in python

distro2 = distro[1]
distro3 = distro[1:4]
print(distro2)
print(distro3)
print(len(distro))
print(distro.endswith("sna"))
print(distro.startswith("fe"))
print(distro.capitalize())
print(distro.upper())
