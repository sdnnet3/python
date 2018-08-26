#UTF-8?
# Code by Clayton Hutton

seq  = ["one", "two", "three"]
for i, element in enumerate (seq):
    seq[i] = '%d : %s' % (i, seq[i])

print(seq)


def _treatment(pos, element):
    return '%d: %s' % (pos, element)

[_treatment(i, el) for i, el in enumerate(seq)]
print(seq)
