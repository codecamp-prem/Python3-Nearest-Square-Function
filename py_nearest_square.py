#TODO: Implement the nearest_square function
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

test1 = nearest_square(16)
print("expected result: 9, actual result: {}".format(test1))

test1 = nearest_square(4)
print("expected result: 1, actual result: {}".format(test1))
