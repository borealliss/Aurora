print("PAYMENT COMPUTATION FOR EMPLOYEES")
print("----------------------------------")
def pay(hour, rate):

    if hour>10:
        print ((hour*rate)+200)
    elif hour< 10:
        print (hour*rate)

hour= int(input("Enter Hours:"))
rate = int(input("Enter Rate:"))

pay(hour,rate)
print (f'Bayaran kamu adalah {pay}')
