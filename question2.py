import inspect


def compare_subjects_within_student(subj1_all_students: dict,
                                    subj2_all_students: dict) -> list:
  """Compare the two subjects with their students and print out the higher-graded
        subject for each student.

    Parameters
    ----------
    subj1_all_students, subj2_all_students
        2 dictionaries, each contains the grades of all students in a given subject.
        Key - students' names
        Value - a tuple containing the grades of the first and second exam
        

    Returns
    -------
    A list of tuples, each tuple contains the name of the student and the corresponding subject.
    """
  # name of the subjects
  subject1 = "Charms"
  subject2 = "Divination"

  # list all the students that take both classes
  student_list = list(
      set(subj1_all_students.keys()).intersection(subj2_all_students.keys()))
  
  students_best_subj = []
  for student in student_list:
    max_subj1 = max(subj1_all_students[student])
    max_subj2 = max(subj2_all_students[student])
    
    if max_subj1 > max_subj2:
      students_best_subj.append((student, subject1))
    else:
      students_best_subj.append((student, subject2))
  
  return students_best_subj


