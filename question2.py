import inspect


def compare_subjects_within_student(subj1_all_students: list,
                                    subj2_all_students: list) -> list:
  """Compare the two subjects with their students and print out the higher-graded subject for each student.

    Single-subject students shouldn't be printed.

    Parameters
    ----------
    subj1_all_students, subj2_all_students
        2D lists which contain the grades of all students in a given subject.
        First column - students' names
        Second column - grades in the first exam
        Third column - grades in the second exam

    Notes
    -----
    Choice for the data structure of the function's arguments is up to you.

    Returns
    -------
    A list of tuples, each tuple contains the name of the student and the corresponding subject.
    """
  #list all the students that take both classes
  student_list = list(
      set(subj1_all_students[0]).intersection(subj2_all_students[0]))

  #create a dictionary to contain the nested data per student (student -> subject -> exam : grade)
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
        grades[student][f"subj{subj+1}"][f"exam{exam+1}"] = current_subject[
            exam + 1][exam_idx]

  #print(grades)

  #find the highet grade and return the student and subject
  students_best_subj = []
  for student in grades:
    max_grades = []
    subjects = []
    #go over all the subjects and find the highest grade
    for subj in range(num_of_subj):
      best_grade_in_subj = max(grades[student][f"subj{subj+1}"].values())
      max_grades.append(best_grade_in_subj)
      subjects.append(f"Subject {subj+1}")

    max_grade = max(max_grades)
    best_subject = subjects[max_grades.index(max_grade)]
    students_best_subj.append((student, best_subject))

  return students_best_subj





