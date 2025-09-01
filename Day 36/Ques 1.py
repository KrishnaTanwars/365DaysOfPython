# Question: You are given information about N people (first name, last name, age, and sex). Use decorators to print their names in a specific format, sorted by their age in ascending order.
# Example Format: "Mr. Henry Davids" or "Ms. Mary George"

import operator

def person_lister(f):
    def inner(people):
        # Sort people by age (the 3rd element, index 2)
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner

@person_lister
def name_format(person):
    # Format the name with "Mr." or "Ms." based on sex (the 4th element, index 3)
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')