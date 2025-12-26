class roman_version:
    def __init__(self, number):
        self.number = number

    def convert_roman(self):
        roman_numerals = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""
        num = self.number

        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value

        return result


def main():
    original_number = int(input("Enter a number between 1 and 3999: "))

    if original_number < 1 or original_number > 3999:
        print("Number must be between 1 and 3999.")
        return

    converter = roman_version(original_number)
    print(f"Roman numeral: {converter.convert_roman()}")


if __name__ == "__main__":
    main()