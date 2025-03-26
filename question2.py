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
  num_of_subj = 2 #inspect.signature(compare_subjects_within_student).parameters
  num_of_exams = 2
  grades = {}
  for student in student_list:
      for subj in range(num_of_subj):
        grades[student] = {f"subj{subj+1}" : {
          for exam in range(num_of_exams):
            {f"exam{exam+1}" : subj1_all_students[subj][exam]}
        }
            

    # best_in_subj1 = max(grades[student]['subj1']['exam1'], grades[student]['subj1']['exam2'])
    # best_in_subj2 = max(grades[student]['subj2']['exam1'], grades[student]['subj2']['exam2'])

#I WANT TO RETURN THE NAME OF THE COURSE BUT I DONT HAVE IT
# subj1_max_grade = max(grades.values())
#   subj2_max_grade = max(subj2.values())
#   return(key(max(subj1_max_grade, subj2_max_grade)))
  print(grades)

# test 
charms_all_students = [["ron", "harry", "hermione", "neville", "draco"] , [80, 90, 100,40,90] , [75, 95, 100 , 70, 95] ]

divination_all_students = [["ron", "harry", "hermione", "draco"], [60, 70, 100,60], [75, 95, 100,65]]
compare_subjects_within_student(
  charms_all_students,
  divination_all_students, 
)