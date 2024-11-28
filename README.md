# Call Tools Test

# Установка
```
git clone https://github.com/nekrulya/CallToolsTest.git
cd CallToolsTest
```

## Задание 1 ([ссылка на решение](https://onecompiler.com/postgresql/42zetmdn7))
Так как при большом количестве записей использование JOIN будет занимать много времени - поступим хитрее :)

1. Сначала получим из таблицы comment все article_id статей, у которых комментарии **есть**. 
2. Затем из таблицы article получим все статьи кроме полученных на предыдущем шаге.

```
WITH articles_with_comment AS
  (SELECT article_id
   FROM comment)
SELECT id
FROM article
WHERE id NOT IN
    (SELECT article_id
     FROM articles_with_comment)
```

[Интерактивная версия](https://onecompiler.com/postgresql/42zetmdn7)

## Задание 2 ([ссылка на решение](https://replit.com/@IliaNiekrasov1/CooperativeCornsilkEvaluations)
Решение достаточно много:
* Разделить по символу пробела, получить имя и число.
* Получить индекс последнего символа пробела, считать значения до него - именем, после него - числом.
* Использовать регулярное выражение и его группы (используем данный вариант)

В процессе решения была обнаружена неточность - в строке "X Æ A-12 45" указано 45 рабочих часов в сутки, что невозможно. 

Добавил обработку данной ошибки и исправил тестовые данные :)

``` 
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
```
