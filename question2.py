
import inspect
def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    """Compare the two subjects with their students and print out the higher-graded subject for each student.

    Single-subject students shouldn't be printed.

    Parameters
    ----------
    subj1_all_students, subj2_all_students
        Data structures which contain the grades of all students in a given subject.

    Notes
    -----
    Choice for the data structure of the function's arguments is up to you.

    Returns
    -------
    A data structure with the name of the student and the corresponding subject.
    """
    #list all the students that take both classes
    student_list = list(
        set(subj1_all_students[0]).intersection(subj2_all_students[0]))
    
    #create a dictionary to contain the nested data per student
    num_of_subj = 2
    num_of_exams = 2
    grades = {}
    
    for student in student_list:
        grades[student] = {}
        for subj in range(num_of_subj):
            grades[student][f"subj{subj+1}"] = {}
            for exam in range(num_of_exams):
                current_subject = [subj1_all_students, subj2_all_students][subj]
                exam_idx = current_subject[0].index(student)
                grades[student][f"subj{subj+1}"][f"exam{exam+1}"] = current_subject[exam+1][exam_idx]
    
    print(grades)

    #find the highet grade and return the student and subject
    for student in grades:
        max_grades = []
        for subj in range(num_of_subj):
            best_grade_in_subj = max(grades[student][f"subj{subj+1}"].values())
            max_grades.append(best_grade_in_subj)
        print(f"{student}'s highest grade overall: {max(max_grades)}")
                
  

# test 
charms_all_students = [["ron", "harry", "hermione", "neville", "draco"] , [80, 90, 100,40,90] , [75, 95, 100 , 70, 95] ]
divination_all_students = [["ron", "harry", "hermione", "draco"], [60, 70, 100,60], [75, 95, 100,65]]
compare_subjects_within_student(
    charms_all_students,
    divination_all_students, 
)
