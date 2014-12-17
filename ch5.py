# -- List comprehensions
mins = [1, 2, 3, 4, 5, 6]
# Convert mins to secs for each list item
secs = [m * 60 for m in mins]
print(secs)


# create set
distances = {10.6, 11, 8, 10.6, "two", 7}
print(distances)
# or
distances = set([10.6, 11, 8, 10.6, "two", 7])
print(distances)

# Dictionary
dictionary = {'name' : 'Dido', 'age': 31, 'sex': 'male'}
print(dictionary)