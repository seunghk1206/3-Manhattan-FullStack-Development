import string
alphabet_string = string.ascii_uppercase
##
nmb = [[[eachNum for eachNum in range(26)] for _ in range(26)] for _ in range(26)]
for x in nmb:
    for var in x:
        for each in var:
            var[var.index(each)] = alphabet_string[var.index(each)]
print(nmb)
print(alphabet_string)
## is the same as
nmb_Alpha = [[[eachNum for eachNum in alphabet_string] for _ in range(26)] for _ in range(26)]
print(nmb_Alpha)
print(len(alphabet_string))