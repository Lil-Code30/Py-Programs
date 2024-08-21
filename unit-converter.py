def main():
    print("===========================")
    print("===== Unit Conversion =====")
    print("===========================")
    conversion_list()

    conversion = input("Enter the number of the conversion to use --> ")
    conversion_index = int(conversion) - 1
    
    global conversion_number, from_unit, to_unit, from_value
  
    conversion_number, from_unit, to_unit = conversion_available[conversion_index]
    from_value = float(input(f"Enter the value in {from_unit} to convert to {to_unit}: "))
    unit_converter(from_value)

def conversion_list():
    global conversion_available
    conversion_available = [(1, "km", "m"),
                            (2, "m", "km"),
                            (3, "km", "mi"),
                            (4, "mi", "km"),
                            (5, "kg", "lbs"),
                            (6, "lbs", "kg"),
                            (7, "°F", "°C"),
                            (8, "°C", "°F")]
    
    print("Conversions Available:")
    for conversion_number, from_unit, to_unit in conversion_available:
        print(f"{conversion_number}) {from_unit} -> {to_unit}")
    print()

def unit_converter(user_value):  
    if conversion_number == 1:
        to_value = user_value * 1000
        print(f"{user_value}{from_unit} -> {to_value}{to_unit}") 

    






main()