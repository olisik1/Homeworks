from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Let's test the functions with different values.
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)  # Expected: 23.0
print(result2)  # Expected: 'Ошибка'
print(result3)  # Expected: 7.0
print(result4)  # Expected: inf
