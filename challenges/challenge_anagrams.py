# sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla () com a primeira string ordenada, a segunda string ordenada e um booleano, True ou False representando se são anagramas.
# O algoritmo deve considerar letras maiúsculas e minúsculas como iguais durante a comparação das entradas, ou seja, ser case insensitive.
# Utilize qualquer algoritmo que quiser (Selection sort, Insertion sort, Bubble sort, Merge sort, Quick sort ou TimSort), desde que atinja a complexidade O(n log n).
# Você deverá implementar sua própria função de ordenação, ou seja, o uso de funções prontas não é permitido.
#   Exemplos de funções não permitidas: sort, sorted e Counter;
# A função retorna True caso uma string seja um anagrama da outra independente se as letras são maiúsculas ou minúsculas;
# A função retorna False caso uma string não seja um anagrama da outra;


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    sort_first_string = merge_sort(first_string)
    sort_second_string = merge_sort(second_string)
    if len(first_string) != len(second_string):
        return ("".join(sort_first_string), "".join(sort_second_string), False)

    for i in range(len(sort_first_string)):
        if sort_first_string[i] != sort_second_string[i]:
            return (
                "".join(sort_first_string),
                "".join(sort_second_string),
                False,
            )

    return ("".join(sort_first_string), "".join(sort_second_string), True)


teste = is_anagram("aaadepr", "aaadepra")
print(teste)
