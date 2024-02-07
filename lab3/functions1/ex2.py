#convert fahrenheit to celcius
def conv_celc(x):
    return (5/9)*(x-32)

f=float(input())
print(conv_celc(f))