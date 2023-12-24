result = []
const = 50 + 75

if __name__ == '__main__':
    with open('lab1/data/text_3_var_75') as file:
        lines = file.readlines()
 
    for line in lines:
        item = line.split(',')
        for i in range(len(item)):
            if item[i] == 'NA':
                item[i] = (int(item[i-1]) + int(item[i+1])) / 2
        
        item = list(filter(lambda x: x ** 0.5 >= (const), list(map(int, item))))
        if len(item) > 0:
            result.append(item)

    with open('lab1/result/task3/result', 'w') as output:
        for line in result:
            output.write(",".join(str(num) for num in line) + '\n')