class Solution:

    def validate_roman_number_lenth(self, number: str) -> bool:
        if len(number) < 1 or len(number) > 15:
            return False
        return True

    def validate_roman_number_caracters(self, roman_number: str) -> bool:
        valid_caracters = ["I", "V", "X", "L", "C", "D", "M"]
        if not roman_number:
            return False
        if all(letter in valid_caracters for letter in roman_number):
            return True
        return False

    def get_number(self, letter: str) -> int:
        symbols = (
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
        )

        number = [value for symbol, value in symbols if letter == symbol]

        return number[0]

    def sum_numbers(self, lst_numbers: list) -> int:
        number = 0
        for i, value in enumerate(lst_numbers):
            if i < len(lst_numbers) - 1:
                next_value = lst_numbers[i + 1]
                if value < next_value:
                    number -= value
                    continue
            number += value

        return number

    def roman_to_integer(self, s: str) -> int:

        is_valid_lenth = self.validate_roman_number_lenth(s)

        if not is_valid_lenth:
            raise Exception("La longitud del numero romano es invalida")

        is_valid_caracters = self.validate_roman_number_caracters(s)

        if not is_valid_caracters:
            raise Exception("El número romano tiene caracters invalidos")

        values = [self.get_number(letter) for i, letter in enumerate(s)]
        number = self.sum_numbers(values)

        return number


if __name__ == "__main__":
    solution = Solution()
    print(solution.roman_to_integer("III"))
