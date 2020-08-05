alphabet_string = string.ascii_uppercase
nmb = [[[eachNum for eachNum in range(10)] for _ in range(10)] for _ in range(10)]
for x in nmb:
    for var in x:
        for each in var:
            if each == 0:
                var[var.index(each)] = 'A'
print(nmb)
print(alphabet_string)