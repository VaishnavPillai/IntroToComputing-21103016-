my_list=['Red','Green','White','Black','Pink','Yellow']
#(a) part
print('(a)')
print(my_list)
# remove 4th term that is black
my_list.remove('Black')
print(my_list)

my_list=['Red','Green','White','Black','Pink','Yellow']
#(b) part
print('(b)')
print(my_list)
#replace black and pink with purple
# to replace nth term we write {my_list[n-1]='new value'}
my_list[3:5]=['Purple']
print(my_list)
