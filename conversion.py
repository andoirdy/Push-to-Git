import sys

def conversion (one, two, three):
    # Conversion factors
    factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    meters = three * factors[one]
    result = meters / factors[two] #conversion to meters before converting to target unit
    
    print (f"{three} {one} is equal to {result} {two}")

if len(sys.argv) == 4:
    one = sys.argv [1]
    two = sys.argv [2]
    three = float(sys.argv [3]) 
    conversion (one, two, three)
elif "help" in sys.argv:
    print ("""This program takes in 3 arguments: the unit you convert from, the unit you convert into, and the value of the first unit.
           It supports the following units:
                km, m, cm, mm, in, ft, yd, mi
           Please input your arguments in (unit, unit, value) format.
           """)
else:
    print ("""Invalid argumen. Please use the "help" argument for instructions. """)
