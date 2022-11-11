from random import randint

def wall(entrance):
    offset = abs(3 - entrance)
    baskets = [1, 2000, 10, 1000]
    # baskets.reverse()
    temp = []
    for i in range(4):
        if randint(0, 1) == 0:
            print('l')
            # temp.append(-0.5)
            temp.append(-1)
        else:
            print('r')
            temp.append(1)
            # temp.append(0.5)
    print(temp)
    dist = abs(sum(temp)-offset)
    # print(baskets)
    # if dist == 0:
    #     return 5000
    
    print("Dstance " + str(abs(dist)))
    return baskets[abs(dist)]


def z2():
    pass


if __name__ == "__main__":
    print(wall(2))

        

