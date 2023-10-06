def     linearSearchProduct(productList,targetProduct):
  indices = []

  for index,product in enumerate(productList):
   if product==targetProduct:
    indices.append(index)

  return indices


#example usage:
product =["shoes","boot","loafer","shoes","s andal","shoes"]
target ="shoes"
target2 ='apple'
result       =linearSearchProduct(product,       target)
print(result)
