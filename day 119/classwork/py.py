def orive_masivshi_roa(arr1, arr2):
    result = []
    for i in arr1:
        for j in arr2:
            if i == j:
                result.append(i)
    return result
