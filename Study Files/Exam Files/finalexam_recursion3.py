# Tommy D. Michailidis
# 2023-12-06
# Final Exam


def reduce_rec(op, values):
    if len(values) == 1:
        return values[0]
    else:
        return op(values[0], reduce_rec(op, values[1:]))


print(f"{reduce_rec(lambda x,y: x + y, [1,2,3,4,5])}")
print(f"{reduce_rec(lambda x,y: x * y, [1,2,3,4,5])}")
