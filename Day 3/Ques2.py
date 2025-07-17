# From a list of students and their grades, print names of students who have the second lowest grade, sorted alphabetically.

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input().strip()
        score = float(input())
        students.append([name, score])

    # Get sorted unique scores
    unique_scores = sorted(set(score for name, score in students))

    # Find second lowest score
    second_lowest = unique_scores[1]

    # Get names with second lowest score
    result = [name for name, score in students if score == second_lowest]

    # Print sorted names
    for name in sorted(result):
        print(name)
