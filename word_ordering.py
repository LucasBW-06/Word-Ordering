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
    # compara o índice de cada letra das strings na lista do alfabeto permutado
    for i in range(min(len(word_1), len(word_2))):
        if alpha_index[word_1[i]] > alpha_index[word_2[i]]:
            return False
        elif alpha_index[word_1[i]] < alpha_index[word_2[i]]:
            return True
    
    return len(word_1) <= len(word_2) # retorna se as palavras são de mesmo tamanho ou se a primeira palavra é menor que a segunda

alpha = list(input()) # recebe a string do alfabeto, convertendo-o para uma lista
alpha = alpha + [i.upper() for i in alpha] # adiciona os letras maiusculas ao final da lista, na ordem recebida
alpha_index = {letter: idx for idx, letter in enumerate(alpha)}
num = int(input()) # recebe um número N
words = [input() for i in range(num)] # recebe N strings
print()

# ordena as strings e as exibe ordenadamente
result = merge_sort(words)

for i in result:
    print(i)