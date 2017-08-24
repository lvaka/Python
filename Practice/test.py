def adjacentElementsProduct(inputArray):
    adjacentProducts = []

    for x in range(len(inputArray)):
        if x == len(inputArray) - 1:
            break
        else:
            adjacentProducts.append(inputArray[x] * inputArray[x+1])
        
    adjacentProducts.sort(reverse=True)
    return adjacentProducts[0]

print (adjacentElementsProduct([1,2,4]))
