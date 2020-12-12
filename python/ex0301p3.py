hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r1 = float(rate)
except:
    print("Error,please enter numeric value")
    quit()
    
p1 = h*r1
p2 = 0
if h>40:
    p1 = 40*r1
    r2 = r1*1.5
    p2 = (h-40)*r2
pt = p1+p2
print(pt)
