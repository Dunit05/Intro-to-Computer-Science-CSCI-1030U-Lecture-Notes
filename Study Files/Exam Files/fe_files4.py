# Tommy D. Michailidis
# 2023-12-06
# Final Exam


def get_average_classic_rating(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines.pop(0)
        ratings = []
        for line in lines:
            line = line.split(",")
            if line[4] == "Classic":
                ratings.append(float(line[5]))
        return sum(ratings) / len(ratings)


print(f'{get_average_classic_rating("data/data.csv"):0.1f}')
