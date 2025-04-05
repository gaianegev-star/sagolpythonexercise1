from question1 import trifeca
from question2 import compare_subjects_within_student
from question3 import check_palindrome

##############
# Question 1 #
##############

inputs = [
  'aabbcc',
  'abccddee0123',
  'llkkbmm',
  'aaaazz',
  'bbcCdd',
  '0012',
  '001122'
]

for inp in inputs:
  print(trifeca(inp))


##############
# Question 2 #
##############

# test
charms_all_students = {
    "Ron": (80, 75),
    "Harry": (90, 95),
    "Hermione": (100, 100),
    "Neville": (40, 70),
    "Draco": (80, 85)
}

divination_all_students = {
    "Ron": (60, 95),
    "Harry": (70, 95),
    "Hermione": (100, 100),
    "Draco": (60, 65)
}


print(
  compare_subjects_within_student(
      charms_all_students,
      divination_all_students,
  ))

##############
# Question 3 #
##############

check_palindrome()