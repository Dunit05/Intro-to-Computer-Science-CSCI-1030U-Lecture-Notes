# Write a program that asks the user for a midterm mark, a lab mark, and a final exam mark and outputs the student's final mark (out of 100)

midterm_mark = float(input("Enter the midterm mark (Out of 80): "))
lab_mark = float(input("Enter the lab mark (Out of 30): "))
final_exam_mark = float(input("Enter the final exam mark (Out of 180): "))

mark = (midterm_mark / 80 * 30) + lab_mark + (final_exam_mark / 180 * 40)
mark = round(mark, 2)

print("The final mark is", mark)
