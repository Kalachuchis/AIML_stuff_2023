import math
import re


def get_distance(given_point, point_2):

    # print(given_point, point_2)
    distance = math.sqrt(
        (given_point[0] - point_2[0]) ** 2 + (given_point[1] - point_2[1]) ** 2
    )
    # print(f"distance: {distance}")
    return distance


def get_points(string):
    # gets all the numbers in the string
    # number_list = [int(i) for i in string if i.isnumeric()]
    pattern = "(\d+|\d\.\d)"
    number_list = [int(i) for i in re.findall(pattern, string)]

    if len(number_list) % 2 == 1:
        raise ValueError("Incorrect points")

    # separates the number list into x and y
    x_points = number_list[:-1:2]
    y_points = number_list[1::2]

    # zips x_values and y_values to get the list of points
    return [i for i in zip(x_points, y_points)]


distance_from_given_point = {}
try:
    set_of_points = get_points(input("list of points: "))
    # has 0 since it should only have one point
    given_point = get_points(input("given point: "))[0]
    n = int(input("k: "))

    # print(set_of_points, given_point)

    for i in set_of_points:
        i_distance = get_distance(given_point, i)
        distance_from_given_point.update({i: i_distance})
    sorted_by_distance = sorted(
        distance_from_given_point.items(), key=lambda x: x[1], reverse=False
    )[:n]

    # gets points from sorted_by_distance
    list_to_print = [i[0] for i in sorted_by_distance]
    print(f"Nearest {n} points: {list_to_print}")
    # sorts dictionary by value
    for i in sorted_by_distance:
        print(f"{i[0]} distance: {i[1]}")

except ValueError as e:
    print(e)
