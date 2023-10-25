# Tommy D. Michailidis
# #100911141, Midterm 1


# # Function draw_draw_parallelogram4(n, m)
def draw_parallelogram4(n, m):
    # print the first row (n * "*")
    print(("*" * n))
    # Iterate though each row
    for row in range(m - 2):
        # print the spaces
        print(" " * row, end=" ")
        # print the star
        print("*", end="")
        # print the spaces
        print(" " * (n - 2), end="")
        # print the star
        print("*")
    # print the last line of stars (n * "*") & spaces
    print(" " * (m - 2), end=" ")
    print("*" * n)


# ! Testing
draw_parallelogram4(8, 5)
draw_parallelogram4(5, 3)
