immutable_var=tuple([15,'forest',True])
print(immutable_var)
#immutable_var[15]=25
#print(immutable_var) я специально вывела в коммент, иначе код не срабатывает
#Кортежи являются неизменяемыми последовательностями. Это означает, что после того как кортеж создан, его невозможно изменить.
mutable_list=['blue', 12, False, 4.6]
print(mutable_list)
mutable_list[0]='green'
print(mutable_list)