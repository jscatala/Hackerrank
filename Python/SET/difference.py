def clean_students(students):
    return set(students.split(' '))


def intersect(eng, fr):
    eng = clean_students(eng)
    fr = clean_students(fr)
    return eng.difference(fr)  # also -


if __name__ == '__main__':
    n_eng = input()
    eng_students = str(input())
    n_fr = input()
    fr_students = str(input())
    print(intersect(eng_students, fr_students))
