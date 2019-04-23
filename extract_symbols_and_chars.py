
# coding: utf-8

# In[24]:


import os
import numpy as np
import sys


# In[7]:


dictname = sys.argv[1]
all_symbols = []
with open(dictname,'r') as fi_dict:
    for line in fi_dict:
        line = line.rstrip('\n')
        symbols = line.split(' ')[1:]
        all_symbols.append(symbols)
    
    
all_symbols = [x for item in all_symbols for x in item]
unique_symbols = np.unique(all_symbols)

all_characters = [c for s in unique_symbols for c in s]
unique_chars = np.unique(all_characters)


op_fname = dictname.split('.')[0]
op_symb_name = op_fname + '_uniq_symb.txt'
op_symb_name = os.path.join('symbol_unique',op_symb_name)
op_char_name = op_fname + '_uniq_chars.txt'
op_char_name = os.path.join('chars_unique',op_char_name)
with open(op_symb_name,'w') as f:
    for i in unique_symbols:
        f.write(i)
        f.write('\r\n')

with open(op_char_name,'w') as f:
    for i in unique_chars:
        f.write(i)

