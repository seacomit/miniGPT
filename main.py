import torch

text = ""
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#print(len(text))
#print(text[:500])

chars = sorted(list(set(text)))
#print(''.join(chars))
#print(len(chars))

# create maps from character to integer and back
# the integer is just the index of the character in the list of chars
stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

# make functions for converting lists of strings to the index based integers and back
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

#print(encode("toast"))

data = torch.tensor(encode(text), dtype=torch.long)
#print(data.shape, data.dtype)
#print(data[:1000])

# split the data into a training set and a validation set
# used to check for overfitting
n = int(0.9 * len(data))
training_data = data[:n]
validation_data = data[n:]

# define the chunk size for randomly sampling the training data
block_size = 8
#print(training_data[:block_size + 1])

x = training_data[:block_size]
y = training_data[1:block_size+1]
#print(x)
#print(y)
#for t in range(block_size):
#    context = x[:t+1]
#    target = y[t]
#    print(f"when input is {context}, the target is: {target}")

torch.manual_seed(41127)
batch_size = 4 # the number of blocks to process in parallel

def get_batch(split):
    # generate small batches of data with context of x and targets of y
    data = training_data if split == 'train' else validation_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    print(ix) # print the generated offsets
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+1+block_size] for i in ix])
    return x, y

xb, yb = get_batch('train')
print('inputs:')
print(xb.shape)
print(xb)
print('targets:')
print(yb.shape)
print(yb)
print('----')

for b in range(batch_size): # batch dimension
    for t in range(block_size): # time dimension
        context = xb[b, :t+1]
        target = yb[b,t]
        print(f"when input is {context.tolist()} the target is: {target}")
