#calculate gross pay with overtime with non numeric values
hours = input("Enter Hours: ")

try:
    fh = float(hours)
    rate = input("Enter pay rate: ")
    try:
        fr = float(rate)
        if fh > 40.00 :
            ot= fh - 40
            otp = fr * 1.5
            gross = ((fh-ot) * fr) + (ot * otp)
        else: gross = fh * fr
        print("Pay:", gross)
    except:
        print("Please enter numeric input")

except:
        print("Please enter numeric input")
