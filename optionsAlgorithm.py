from collections import Counter

# This function takes in a 2D array, the first dimension
# representing a list of people's choices (the indices represent
# the people), and the second dimension represent each person's
# choices ordered by index (index 0 is their first choice)
# out of a number of options greater then or equal to the number of
# people. The function then returns a list of tuples ordered by index
# zero of each tuple, which represents a person,
# and where the second item of the tuples represents the option
# that has been assigned to that person. Each option is assigned to no
# more than one person. The purpose of the function is to optimize the
# assignation so that every choice goes to one the peole who most wanted it,
# and where there is a tie the first person in the original array is
# assigned the option.

def assignOptions(data):
    # 'taken': store the options already assigned to a student
    taken = []
    # 'studentsDone': track the students that have been assigned an option
    studentsDone = []
    # the result will eventually be stored in 'after',
    # but we will be comparing this a 'before' dictionary
    # to decide when to stop optimizing the selection.
    before = {}
    after = {}
    # 'optimizing': decide when optimization is complete
    optimizing = True
    while (optimizing):
    # 'popular': a list to store the options that more than one
    # student choose as their 1st option, 2nd option etc.
        popular = []
        before = after
        for i in range(len(data[0])):
            tempList = []
            for j in range(len(data)):
                tempList.append(data[j][i])
            tempDict = {}
            tempDict = Counter(tempList)
            for key, value in tempDict.items():
                if key not in popular and key not in taken:
                    if value > 1:
                        popular.append(key)
                    elif value == 1:
                        for j in range(len(data)):
                            if data[j][i] == key:
                                after.update({j:key})
                                taken.append(key)
                                studentsDone.append(j)
                                for k in range(len(data[0])):
                                    data[j][k] = "x"
                                popular.append("x")

        if before == after:
            optimizing = False

    # assign the remaining options on a first come first served basis
    while len(after) < len(data):
        for i in range(len(data[0])):
            for j in range(len(data)):
                if (data[j][i] not in taken) and (j not in studentsDone) and (data[j][i] != "x"):
                    after.update({j:data[j][i]})
                    studentsDone.append(j)
                    taken.append(data[j][i])
    return after




## test example
def main():
    data = [[1,2,3,6, 7],[1,3,2,6,7],[6, 3,2,1,7],[6,2,3,1,7], [6,7,3,2,1]]
    results = assignOptions(data)
    results = sorted(results.items(), key=lambda x: x[0])
    print(results)

if __name__ == "__main__":
    main()
