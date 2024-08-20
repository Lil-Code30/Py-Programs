def main():
    print("===========================")
    print("===== Unit Conversion =====")
    print("===========================")
    conversion_available = [(1, "km", "m"),
                            (2, "m", "km"),
                            (3, "km", "mi"),
                            (4, "mi", "km"),
                            (5, "kg", "lbs"),
                            (6, "lbs", "kg"),
                            (7, "°F", "°C"),
                            (8, "°C", "°F")]

    print("Conversions Available:")
    print()
    for conversion_number, from_unit, to_unit in conversion_available:
        print(f"{conversion_number}) {from_unit} -> {to_unit}")

main()