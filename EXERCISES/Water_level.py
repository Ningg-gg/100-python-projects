water_level = input ("What's the water level? ")
water_level_as_int = int(water_level)

if water_level_as_int > 50:
    print("Drain water")
else:
    print("Continue")