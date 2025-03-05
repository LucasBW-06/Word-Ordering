def merge_sort(array):
    if len(array) == 1:
        return array
    
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0

    while l < len(left) and r < len(right):
        if compare(left[l], right[r]):
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1

    return result + left[l:] + right[r:]

def compare(word_1, word_2):
    l_1 = len(word_1)
    l_2 = len(word_2)
    for i in range(l_1 if l_1 <= l_2 else l_2):
        if alpha.index(word_1[i]) > alpha.index(word_2[i]):
            return False
        elif alpha.index(word_1[i]) < alpha.index(word_2[i]):
            return True
        
    if l_1 > l_2:
        return False
    
    return True

alpha = list(input())
alpha = alpha + [i.upper() for i in alpha]
num = int(input())
words = [input() for i in range(num)]
print()

result = merge_sort(words)

for i in result:
    print(i)