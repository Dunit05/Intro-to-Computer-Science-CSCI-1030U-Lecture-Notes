import json

# Write some code to output the following data values to a file (grade_output.csv) in comma-separated value format:

# Part 1

sids = [
    "100000000",
    "100000001",
    "100000002",
    "100000003",
    "100000004",
    "100000005",
    "100000006",
    "100000007",
    "100000008",
    "100000009",
]
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]
with open("data/grade_output.csv", "w") as file:
    file.write("SID, Midterm Mark\n")
    for i in range(len(sids)):
        file.write(f"{sids[i]}, {midterm_marks[i]}\n")

# Write some code to input the same data file (grade_output.csv) that was output in the previous exercise, and put those values into a list of dictionaries:

# 100000000, 52.0
# 100000001, 48.5
# 100000002, 54.25
# 100000003, 61.5
# 100000004, 64.0
# 100000005, 77.75

# Part 2

with open("data/grade_output.csv", "r") as file:
    lines = file.readlines()
    data = []
    for line in lines[1:]:
        sid, midterm_mark = line.strip().split(",")
        data.append({"SID": sid, "Midterm Mark": float(midterm_mark)})
    print(data)
