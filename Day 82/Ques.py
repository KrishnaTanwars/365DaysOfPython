# Ques : Read `N` student records into a dictionary `{name: [marks]}` and input `query_name`; then print `sum(marks[query_name])/3` rounded to 2 decimals.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ave = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{ave:.2f}")