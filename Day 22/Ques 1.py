# Question: The National University conducts an examination of N students in X subjects. Your task is to compute the average scores of each student.

# Input Format:
# The first line contains N (number of students) and X (number of subjects), separated by a space.
# The next X lines each contain N space-separated scores for a subject.

# Output Format:
# Print the average score for each student on a new line.

if __name__ == "__main__":
    n, x = map(int, input().split())

    marks = []
    for _ in range(x):
        marks.append(list(map(float, input().split())))

    for student in zip(*marks):
        print("{:.1f}".format(sum(student) / x))