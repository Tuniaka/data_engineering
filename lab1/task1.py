import re
freq = {}

if __name__ == '__main__':
    with open('lab1/data/text_1_var_75', 'r') as f:
        text = f.read()
    words = re.findall(r'\w+', text.lower())
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_freq = sorted(freq.items(), reverse = True, key=lambda x: x[1])

    with open('lab1/result/task1/result.txt', 'w') as f:
        for word, count in sorted_freq:
            f.write(f"{word}:{count}\n")