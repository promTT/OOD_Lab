class translator:
    roman_numerals = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    def deciToRoman(self, num):
        roman = ""
        for i in reversed(self.roman_numerals):
                if num >= self.roman_numerals[i]:
                    r = num // self.roman_numerals[i]
                    num %= self.roman_numerals[i]
                    roman += i*r
        return roman


    def romanToDeci(self, s):
        num = 0
        prev_value = 0
        for char in reversed(s): 
            value = self.roman_numerals[char]
            if value < prev_value:
                num -= value 
            else:
                num += value
                prev_value = value
        return num
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))