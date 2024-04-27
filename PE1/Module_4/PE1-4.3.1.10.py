def liters_100km_to_miles_gallon(liters):
    mile_km = 1.609344
    gallon_liter = 3.785411784
    miles_gallon = (100/mile_km)/(liters/gallon_liter)
    return miles_gallon

def miles_gallon_to_liters_100km(miles):
    mile_km = 1.609344
    gallon_liter = 3.785411784
    liters_100km = (100*gallon_liter)/(miles*mile_km)
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))