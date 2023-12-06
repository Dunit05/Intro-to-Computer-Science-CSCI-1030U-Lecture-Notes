# Write a class (Point3D) that stores three floating point instance variables (x, y, and z).  The class should have a constructor to initialize the three variables, as well as a function (get_distance_to) that takes another Point3D and returns the linear distance, according to the following formula (where (x1,y1,z1) is the first point, and (x2,y2,z2) is the second point):


# distance = sqrt((x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2)


# Sample usage:

# if __name__ == '__main__':

#     p1 = Point3D(2.0, 2.0, 4.0)

#     p2 = Point3D(3.0, 1.0, 2.0)


#     print(f'distance between p1 and p2: {p1.get_distance_to(p2)}')

#     # output:  distance between p1 and p2: 2.449489742783178

from math import sqrt


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_distance_to(self, other):
        return sqrt(
            sum(
                [
                    (self.x - other.x) ** 2,
                    (self.y - other.y) ** 2,
                    (self.z - other.z) ** 2,
                ]
            )
        )


if __name__ == "__main__":
    p1 = Point3D(2.0, 2.0, 4.0)
    p2 = Point3D(3.0, 1.0, 2.0)
    print(f"distance between p1 and p2: {p1.get_distance_to(p2)}")
    # output:  distance between p1 and p2: 2.449489742783178
