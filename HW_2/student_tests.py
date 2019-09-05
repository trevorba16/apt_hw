from student import Student


# Prints out the students sorted in alphabetical order
def sort_test(stdnt_array):

    print('Sorting -----------------------------')
    sorted_array = sorted(stdnt_array)
    for s in sorted_array:
        print(s)



# Prints out the students name, and a dictionary value attached to that student
def dict_test(stdnt_dict):

    print('Dictionary test ---------------------')
    for key in stdnt_dict.keys():
        print(key, stdnt_dict[key])



# Creates and uses three lambda sorting equations to sort students
def make_function():

    gpa_comp = lambda x: x.gpa
    name_comp = lambda x: x.name
    age_comp = lambda x: x.age

    def sort_students(students):
        first_sort = sorted(students, key=age_comp)
        second_sort = sorted(first_sort, key=name_comp)
        sorted_list = sorted(second_sort, key=gpa_comp)
        return sorted_list

    return sort_students




student_array = [Student('Ashley', 26, 3.9),
                 Student('Charlie', 15, 2.0),
                 Student('Matt', 7, 3.9),
                 Student('Trevor', 28, 4.0),
                 Student('Matt', 20, 3.9)
                 ]

student_dict = {Student('Trevor', 28, 4.0): 'Trevor string',
                Student('Ashley', 26, 3.9): 'The string for ashley',
                Student('Charlie', 26, 3.9): 365,
                Student('Ashley', 20, 3.9): Student('Piper', 1, 1.0)
                }

if __name__ == '__main__':
    sort_test(student_array)
    dict_test(student_dict)
    sorting = make_function()
    sorted_students = sorting(student_array)
    for s in sorted_students:
        print(s.gpa, s.name, s.age)