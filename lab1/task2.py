import re
s = 0
avgs = []

if __name__ == '__main__':
    with open('lab1/data/text_2_var_75', 'r') as f:
        lines = f.readlines()

        for line in lines:
            nums = re.findall(r'\d+', line)
            for num in nums:
                s += int(num)
            avg = s / len(nums)
            avgs.append(avg)

    with open('lab1/result/task2/result.txt', 'w') as f:
        for avg in avgs:
            f.write(f"{avg}\n")