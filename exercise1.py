hrs = float(input("Enter Hours:"))
h = float(hrs)
rate = float(input("Enter Rate:"))
r = float(rate)
if hrs > 40.0:
    reg = (rate * hrs)
    otp = (hrs - 40.0) * (rate * 0.5)
    xp = reg + otp
else:
    xp = hrs * fr
print ("Pay:", xp)
