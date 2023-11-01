message = 'q dkfj783df r tdkfj9'
i=0
#integers = []
cifri = ''

#print (message)
#print (len(message))

while i<=len(message):
    #print (f'!итерация внешенего цикла: {i}')
    while i<len(message) and '0'<= message[i]<= '9':
        cifri +=message[i]
        #print (f'!!Внутренний цикл шаг: {i} \nнайдена цифра: {cifri}')
        i +=1
        #print (f'*Добавили шаг когда нашли цифрц {i}')
    else:
        cifri += ' '
        #print (f'Добавили пробел разделитель {cifri}чисел')
        i += 1

print (cifri)
number = cifri.split()
if number != 0 and len(number) == 1:
    print (number[0])
else:
    print (f'В тексте больше цифр, введите снова!\n {number}')
