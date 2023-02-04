#HVL calculation

kV = 1
while kV > 0:
    kV = float(input("\nWhat is the measured kV (Enter 0 to exit)? "))
    if kV <= 0:
        break
    HVL = round(kV * 0.0444 - 0.6556, 2)
    print("\nMinimum allowed HVL: " + str(HVL))
