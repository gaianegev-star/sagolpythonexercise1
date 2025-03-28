from question1 import trifeca
from question2 import compare_subjects_within_student
from question3 import complicated_palindrome

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

# for inp in inputs:
#   print(trifeca(inp))


##############
# Question 2 #
##############

# test
charms_all_students = [["Ron", "Harry", "Hermione", "Neville", "Draco"],
                       [80, 90, 100, 40, 80], [75, 95, 100, 70, 85]]
divination_all_students = [["Ron", "Harry", "Hermione", "Draco"],
                           [60, 70, 100, 60], [95, 95, 100, 65]]

print("\nQuestion 2 results:")
print(
  compare_subjects_within_student(
      charms_all_students,
      divination_all_students,
  ))

##############
# Question 3 #
##############

print("\nQuestion 3 results:")
complicated_palindrome()
