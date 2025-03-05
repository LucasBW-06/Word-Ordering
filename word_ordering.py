def merge_sort(array): # função principal
    # caso o array tiver apenas 1 elemento, significa que ele já está ordenado
    if len(array) == 1:
        return array
    
    # divide o array em duas partes
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    return merge(left, right) # retorna a mescla das duas partes

def merge(left, right): # função que mescla duas arrays ordenadas
    result = []
    l = r = 0

    # enquanto houver elementos em ambas as arrays, compare as strings das arrays uma a uma
    while l < len(left) and r < len(right):
        if compare(left[l], right[r]): # verifica qual string é menor e qual é maior lexicograficamente de acordo com o alfabeto permutado
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1

    return result + left[l:] + right[r:] # retorna a array ordenada

def compare(word_1, word_2): # função que compara duas strings, de acordo com o alfabeto permutado
    l_1 = len(word_1)
    l_2 = len(word_2)
    # compara o índice de cada letra das strings na lista do alfabeto permutado
    for i in range(l_1 if l_1 <= l_2 else l_2):
        if alpha.index(word_1[i]) > alpha.index(word_2[i]):
            return False
        elif alpha.index(word_1[i]) < alpha.index(word_2[i]):
            return True
        
    if l_1 > l_2:
        return False
    
    return True

alpha = list(input()) # recebe a string do alfabeto, convertendo-o para uma lista
alpha = alpha + [i.upper() for i in alpha] # adiciona os letras maiusculas ao final da lista, na ordem recebida
num = int(input()) # recebe um número N
words = [input() for i in range(num)] # recebe N strings
print()

# ordena as strings e as exibe ordenadamente
result = merge_sort(words)

for i in result:
    print(i)