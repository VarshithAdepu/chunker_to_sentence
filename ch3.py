def read_file(file_path):
    lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line.strip().split())
    i = 0
    for l in range(len(lines) - 1, 0, -1):
        if len(lines[l]) > 2 and lines[l][2] == 'CC':
            cc_index = l
            ocount = get_output(lines, i, cc_index)
            break
    return ocount

def get_output(lines, j, l):
    c = 0
    count = 0
    flag = False
    for i in range(j, len(lines)):
        if len(lines[i]) > 1 and lines[i][1] == 'VGF':
            flag = True
        if len(lines[i]) > 2 and lines[i][2] == 'CC' and flag:
            if lines[i][0] == 'कि':
                for k in range(i - 1, 0, -1):
                    if 'VM' in lines[k]:
                        lines.insert(k, ['यह'])
                        
                        break
            count += 1
            sentence = " ".join([lines[o][0] for o in range(j, i)])
            sentence = sentence.replace("((","").replace("))","").replace("  "," ")
            arr.append(sentence)
            flag = False
            get_output(lines, i, l)
            c += 1
        elif i == l:
            sentence = " ".join([lines[o][0] for o in range(l, len(lines))])
            sentence = sentence.replace("((","").replace("))","").replace("  "," ")
            arr.append(sentence)
            break
    return count

arr = []
file_path = "p_parser_output.txt"
output = read_file(file_path)
print(arr)

def add_yah_agar(arr):

    # for i in range(1, len(arr)):
    #     if arr[i].startswith('कि') and not any(word in arr[i-1] for word in ['इतना', 'इतनी', 'इतने']):
    #         # words=arr[i-1].split()
    #         # if 'यह' in arr[i-1]:
    #         #     words.remove('यह')
    #         # arr[i-1]=' '.join(words)
    #         words = arr[i-1].split()
    #         words.insert(-1, 'यह')
    #         arr[i-1] = ' '.join(words)
    if arr[0].startswith('अगर'):
        for i in range(len(arr)):
            words = arr[i].split()
            for j in range(len(words)):
                if words[j] in ['और', 'तथा', 'एवं']:
                    words.insert(j+1, 'अगर')
                    break
            arr[i] = ' '.join(words)
    return arr
    

result = add_yah_agar(arr)
# print(result)

# arr1=add_yah(arr)
fp1 = 'output4.txt'
with open(fp1, 'w') as file:
    for i in range(output + 1):
        file.write("%s\n" % arr[i].strip())
        print(arr[i])
