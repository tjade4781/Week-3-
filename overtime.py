#calculating gross pay to incllude overtime
hours = input('Enter Hours:')
rate = input("Enter pay rate:")
fh = float(hours)
fr = float(rate)
if fh > 40.00 :
    ot = fh - 40
    otp = fr * 1.5
    gross = ((fh - ot) * fr) + (ot * otp)
else: gross = fh * fr
print("pay:", gross)
