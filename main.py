text = ""
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#print(len(text))
#print(text[:500])

chars = sorted(list(set(text)))
print(''.join(chars))
print(len(chars))

# create maps from character to integer and back
# the integer is just the index of the character in the list of chars
stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

# make functions for converting lists of strings to the index based integers and back
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

print(encode("toast"))
