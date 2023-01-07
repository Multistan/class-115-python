#syntax error

# a=8
# b=30
# c= a b

#zero division error
number=[5,0,2]
for i in number:
    try:
        result=5/i
        print("the result of 5/",i,"is", result)



    except ZeroDivisionError:
        print("oops error occured")