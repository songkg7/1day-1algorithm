result = 1
i = 1

def multifly(result):
    global i
    if i == 10:
        return result
    
    i += 1
    result *= i
    return multifly(result)

print(multifly(result))
