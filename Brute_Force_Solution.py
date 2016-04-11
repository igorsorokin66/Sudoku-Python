__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'

import copy
test = []
test.append(['1', ' ', ' ', '5', '7', ' ', ' ', '3', '8'])
test.append(['7', ' ', ' ', ' ', ' ', '8', '4', ' ', ' '])
test.append([' ', '8', '3', ' ', '1', ' ', '5', ' ', ' '])
test.append([' ', '1', ' ', '8', ' ', '3', ' ', ' ', '2'])
test.append(['8', ' ', '7', ' ', ' ', ' ', '6', ' ', '4'])
test.append(['5', ' ', ' ', '7', ' ', '6', ' ', '8', ' '])
test.append([' ', ' ', '8', ' ', '9', ' ', '7', '2', ' '])
test.append([' ', ' ', '5', '3', ' ', ' ', ' ', ' ', '1'])
test.append(['9', '7', ' ', ' ', '8', '5', ' ', ' ', '6'])
print(test)
box = ["" for i in range(9)] # i hard coded all which cell belongs to which box, a more elegant solution exists
box[0] = [0,0],[0,1],[0,2],\
         [1,0],[1,1],[1,2],\
         [2,0],[2,1],[2,2]
box[1] = [3,0],[3,1],[3,2],\
         [4,0],[4,1],[4,2],\
         [5,0],[5,1],[5,2]
box[2] = [6,0],[6,1],[6,2],\
         [7,0],[7,1],[7,2],\
         [8,0],[8,1],[8,2]
box[3] = [0,3],[0,4],[0,5],\
         [1,3],[1,4],[1,5],\
         [2,3],[2,4],[2,5]
box[4] = [3,3],[3,4],[3,5],\
         [4,3],[4,4],[4,5],\
         [5,3],[5,4],[5,5]
box[5] = [6,3],[6,4],[6,5],\
         [7,3],[7,4],[7,5],\
         [8,3],[8,4],[8,5]
box[6] = [0,6],[0,7],[0,8],\
         [1,6],[1,7],[1,8],\
         [2,6],[2,7],[2,8]
box[7] = [3,6],[3,7],[3,8],\
         [4,6],[4,7],[4,8],\
         [5,6],[5,7],[5,8]
box[8] = [6,6],[6,7],[6,8],\
         [7,6],[7,7],[7,8],\
         [8,6],[8,7],[8,8]
def is_Legal(input):
    for col in range(9):
        for row in range(9):
            if input[row][col] != " ":
                digit = input[row][col]
                if input[row].count(digit) > 1: # check row
                    return False
                if [input[i][col] for i in range(9)].count(digit) > 1: # check col
                    return False
                saveB = 0
                for b in range(len(box)): # check box
                    for elem in box[b]:
                        if elem[0] == col and elem[1] == row:# found correct box
                            checkBox = []
                            for elem in box[b]: # save all digits from the correct box and
                                checkBox.append(input[elem[0]][elem[1]])
                            if checkBox.count(digit) > 1: # check for duplicates
                                return False
    return True

def recurse(input):
    for col in range(9):
        for row in range(9):
            if input[row][col] == " ":
                for i in range(1, 10):
                    copyInput = copy.deepcopy(input)
                    copyInput[row][col] = str(i)
                    if is_Legal(copyInput):
                        flag = recurse(copyInput)
                        if flag == "Done":
                            return
                return
    print(input)
    return "Done"
recurse(test)