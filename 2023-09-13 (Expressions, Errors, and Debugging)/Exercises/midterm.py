# Write a program that asks the user for a midterm mark, a lab mark, and a final exam mark and outputs the student's final mark (out of 100)

midterm_mark = int(input("Enter midterm mark: "))
lab_mark = int(input("Enter lab mark: "))
final_exam_mark = int(input("Enter final exam mark: "))

mark = (midterm_mark / 80 * 30) + lab_mark + (final_exam_mark / 180 * 40)

print("The final mark is", mark)
