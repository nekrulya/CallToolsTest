import re
from collections import defaultdict


def calculate_statistics(data: list[str], pattern: str) -> dict[str, list[int]]:
    calculated_data = defaultdict(list)
    for string in data:
        match = re.match(pattern, string)

        if not match:
            raise ValueError(f'Строка "{string}" не соответствует шаблону "{pattern}"')

        name = match.group(1).strip()
        number = match.group(2)

        if int(number) > 24:
            raise ValueError(f"Работник {name} работает {number} - больше 24 часов сутки")

        calculated_data[name].append(int(number))
    return calculated_data

def print_statistics(calculated_data: dict[str, list[int]]) -> None:
    for key, value in calculated_data.items():
        print(f"{key}: {", ".join(map(str, value))}, sum: {sum(value)}")


def main():
    data = ["Андрей 9", "Василий 11", "Роман 7", "X Æ A-12 5", "Иван Петров 3", "Андрей 6", "Роман 11"]
    pattern = r"^(.*\S)\s+(\d+)$"
    calculated_data = calculate_statistics(data, pattern)
    print_statistics(calculated_data)


if __name__ == '__main__':
    main()
