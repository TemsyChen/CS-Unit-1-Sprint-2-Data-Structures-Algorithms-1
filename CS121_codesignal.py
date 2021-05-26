'''
You are given a non-empty array of integers.

One element appears exactly once, with every other 
element appearing at least twice, perhaps more.

Write a function that can find and return the element 
that appears exactly once.

Understand:
[1,1,2,1] --> 2
[1,2,1,2,1,2,80] --> 80

Plan:
Use a dictionary to keep track of how often an integer 
appears in the array. Return the integer that only appears once.
'''

def csFindTheSingleNumber(nums):
    dict_ = {}
    for i, num in enumerate(nums):
        if num not in dict_:
            dict_[num] = 1
        else:
            dict_[num] += 1
    for num, inst in dict_.items():
        if inst == 1:
            return num
    else:
        return 0 
'''
Given a list of different students' scores, write a function 
that returns the average of each student's top five scores. 
You should return the averages in ascending order of the 
students' id numbers.

Each entry (scores[i]) has the student's id number 
(scores[i][0]) and the student's score (scores[i][1]). 
The averages should be calculated using integer division.

Understand:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],
[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]

Plan:
For each student, store the student ID and the average of their scores. 
Sort the array by the order of the average, and return the array. 
'''
from statistics import mean

def csAverageOfTopFive(scores):
    average_scores = {}
    for i in range(len(scores)):
        if scores[i][0] not in average_scores:
            new_list = []
            new_list.append(scores[i][1])
            average_scores[scores[i][0]] = new_list
        else:
            average_scores[scores[i][0]].append(scores[i][1])     
    print(average_scores) 
    result = []
    for student, grades in average_scores.items():
        sorted_grades = sorted(grades, reverse=True)
        top_five = sorted_grades[:5]
        entry = [student, sum(top_five)//len(top_five)]
        result.append(entry)
    return result

'''
Given a string text, you need to use the characters 
of text to form as many instances of the word "lambda" as possible.

You can use each character in text at most once.

Write a function that returns the maximum number of 
instances of "lambda" that can be formed.

Understand:
"mbxcdatlas": 1
"lalaaxcmbdtsumbdav": 2
"sctlamb": 0

Plan:
While there is a letter from the text "lambda", pop it off 
the text and add it to an empty string. If the string spells 
"lambda', add 1 to the counter, and clear the string/start over. 
Return the counter. 
'''

def csMaxNumberOfLambdas(text):
    lambda_dic = {}
    char_list = [char for char in text]
    lambda_list = 'lambda'
    for char in text:
        if char in lambda_list and char not in lambda_dic:
            lambda_dic[char] = 1
        elif char in lambda_list and char in lambda_dic:
            lambda_dic[char] += 1
        else:
            continue

    min_num = min(lambda_dic.keys(), key=(lambda k: lambda_dic[k]))
    min_num = lambda_dic[min_num]
    if all(value >= min_num for value in lambda_dic.values()) and lambda_dic['a'] >= (2*min_num):
        return min_num
    else:
        return 0