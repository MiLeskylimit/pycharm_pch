# 已知attributes,values输出如下内容

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]

# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]


# 1
L = []
for v in values:
        d = {}
        for i, e in enumerate(attributes):
            d[attributes[i]] = v[i]
        L.append(d)
print(L)

# 2
print([{attributes[i]: value[i] for i in range(len(attributes))} for value in values])

# 3
a = [dict(zip(attributes, v)) for v in values]
print(a)




# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]