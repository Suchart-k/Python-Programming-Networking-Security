# Default value in Lambda function    
mz = (lambda a = 'A', b = 'B', c = 'C':"["+ a + b + c + "]")
#calling lambda function
print(mz('A'))
print(mz('A', ' B'))
print(mz('A', ' B', ' C'))
print(mz('A', ' X', ' Y'))
print(mz('X', ' Y', ' Z'))



