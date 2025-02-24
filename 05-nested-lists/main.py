# def get_lowest_grades(grades, lowest_grades):
#     for i, grade in enumerate(grades):
#         if i + 1 >= len(grades) or grades[0] != grades[i + 1]:
#             break
#         lowest_grades.append(grade)


# if __name__ == "__main__":
#     # records = []
#     # for _ in range(int(input())):
#     #     name = input()
#     #     score = float(input())
#     #     records.append([name, score])

#     records = [
#         ["Harry", 37.21],
#         ["Berry", 37.21],
#         ["Tina", 37.2],
#         ["Anel", 37.2],
#         ["Gabi", 37.21],
#         ["Akriti", 41],
#         ["Harsh", 39],
#     ]
#     # Sort list by grande and name
#     records.sort(key=lambda x: (x[1], x[0]))

#     # Get grades
#     grades = [record[1] for record in records]
#     lowest_grades = [grades[0]]
#     get_lowest_grades(grades, lowest_grades)

#     # Remove lowest grades
#     grades = grades[len(lowest_grades) :]

#     second_lowest_grades = [grades[0]]
#     get_lowest_grades(grades, second_lowest_grades)

#     start_index = len(lowest_grades)
#     final_index = len(lowest_grades) + len(second_lowest_grades)

#     for i in range(start_index, final_index):
#         print(records[i][0])

records = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Anel", 37.2],
    ["Gabi", 37.21],
    ["Akriti", 41],
    ["Harsh", 39],
]

grades = [grade for name, grade in records]

unique_grades = sorted(list(set(grades)))

second_lowest_grade = unique_grades[1]

names = [name for name, grade in records if grade == second_lowest_grade]

names.sort()
