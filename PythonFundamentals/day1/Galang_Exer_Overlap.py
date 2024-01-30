r1_tl = []  # rectangle 1 top left point
r1_br = []  # rectangle 1 bottom right point
r2_tl = []  # rectangle 2 top left point
r2_br = []  # rectangle 2 bottom right point


def overlapping_check(r1_tl, r1_br, r2_tl, r2_br):
    horizontal_overlap = True
    vertical_overlap = True
    if int(r1_tl[0]) > int(r2_br[0]) or int(r2_tl[0]) > int(r1_br[0]):
        print("rectangle are side by side")
        horizontal_overlap = False

    if int(r1_tl[1]) < int(r2_br[1]) or int(r2_tl[1]) < int(r1_br[1]):
        print("rectangles are stacked ")
        vertical_overlap = False

    return horizontal_overlap and vertical_overlap


temp = input("Input rectangle 1 top left point (x,y): ")
r1_tl = temp.split(",")

temp = input("Input rectangle 1 bottom right point (x,y): ")
r1_br = temp.split(",")

temp = input("Input rectangle 2 top left point (x,y): ")
r2_tl = temp.split(",")

temp = input("Input rectangle 2 bottom right point (x,y): ")
r2_br = temp.split(",")

is_overlapping = overlapping_check(r1_tl, r1_br, r2_tl, r2_br)

print(f"Rectangles are overlapping? {is_overlapping}")
