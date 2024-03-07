#Write a Python program that invoke square root function after specific milliseconds.
import time
import math 
n1=int(input())
tim=int(input())
def calculating_root(n1, tim):
    time.sleep(tim/1000)
    result=math.sqrt(n1)
    print(f"Square root of {n1} after {tim} milliseconds is {result}")

calculating_root(n1, tim)