#HVL calculation

kV = float(input("What is the measured kV? "))
HVL = round(kV * 0.0444 - 0.6556, 2)
print("\nMinimum allowed HVL: " + str(HVL))
print("\nPress ENTER to exit")

while kV > 0:
    kV = input("\nWhat is the measured kV? (Press 'q' to quit): ")
    if kV == 'q':
        quit()
    kV = float(kV)
    HVL = round(kV * 0.0444 - 0.6556, 2)
    print("\nMinimum allowed HVL: " + str(HVL))
    print("\nPress ENTER to exit")
