commands = [[2,5,3],[4,4,1],[1,7,3]]
array = [1, 5, 2, 6, 3, 7, 4]
newlist = []
answer = []
for i in range(len(commands)):
        newlist.append(array[commands[i][0]-1:commands[i][1]])
        newlist[i].sort()

for i in range(len(commands)):
  answer.append(newlist[i][commands[i][2]-1])

print(answer)

#더 간단한 방법
# for command in commands:
#    i,j,k = command
#    answer.append(list(sorted(array[i-1:j]))[k-1])
#