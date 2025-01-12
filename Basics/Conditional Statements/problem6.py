#A student will not be allowed to sit in exam if his/her attendance is less than 75%.
classes_held= int(input('enter the number of classes held- '))
class_attended= int(input('Enter the number of classses attended- '))
percentage= class_attended/classes_held * 100
print('The percentage of the class attended is- ' , percentage, "%")
if percentage>=75:
    print('The student can write the exam')
else:
    print('You are not eligible to write the exam')