# Ques : Given names and grades of students, print the names of those who have the second lowest grade. If multiple students have that grade, print their names alphabetically, each on a new line.

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second_lowest = sorted(list(set([s[1] for s in students])))[1]
    names = sorted([s[0] for s in students if s[1] == second_lowest])
    for name in names:
        print(name)
