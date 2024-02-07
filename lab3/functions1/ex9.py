#Finding volume of sphere
import math
def vol():
    r=int(input())
    volume= 4/3 * (r**3) * math.pi
    return volume

print(vol())