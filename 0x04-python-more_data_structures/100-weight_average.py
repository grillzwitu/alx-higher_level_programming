#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    sumWeightedScores = 0
    sumTotalWeights = 0
    for i in my_list:
        sumWeightedScores += i[0] * i[1]
        sumTotalWeights += i[1]
    return  sumWeightedScores/sumTotalWeights
