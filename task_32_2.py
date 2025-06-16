def heightofbuilding():
    heights = [25,35,15,16,30,45,37,39]
    height_sorted = sorted(heights,reverse=True)

    for i in range(3):
        print(height_sorted[i])

heightofbuilding()