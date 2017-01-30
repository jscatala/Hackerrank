def clean_students(students):
    return set(students.split(' '))


def count_students(eng, fr):
    eng = clean_students(eng)
    fr = clean_students(fr)
    all_students = eng.union(fr)
    return len(all_students)


if __name__ == '__main__':
    n_english = int(input())
    eng_students = str(input())
    n_french = int(input())
    fr_students = str(input())
    print(count_students(eng_students, fr_students))
