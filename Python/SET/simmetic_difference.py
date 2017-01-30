def clean_students(students):
    return set(students.split(' '))


def difference(eng, fr):
    eng = clean_students(eng)
    fr = clean_students(fr)
    # A + B - intersect(A, B)
    return eng.symmetric_difference(fr)  # also ^


if __name__ == '__main__':
    n_eng = input()
    eng_students = str(input())
    n_fr = input()
    fr_students = str(input())
    print(difference(eng_students, fr_students))
