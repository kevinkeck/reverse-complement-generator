# Take an input sequence and give reverse complement

bp_list = []
rev_comp_list = []

# get user to input sequence and loop until a line is empty 
user_input = 'blank value'
user_input_unjoined = []
instructions = "Input your DNA sequence 5' to 3'\nHit enter when done: "
print(instructions)
while user_input:
    user_input = input("")
    user_input_unjoined.append(user_input)
# Join all lines of user input
user_input_concat = ''.join(user_input_unjoined)

# remove spaces 
no_whitespace = user_input_concat.replace(' ', '')
# capitalize all characters for normalization and nice output later on
no_white_uppercase = no_whitespace.upper()

#get length and print length
dna_seq_len = len(no_white_uppercase)
print('Input sequence: {}'.format(user_input_concat))
print('You input a {} basepair sequence.'.format(str(dna_seq_len)))

# convert string to list: dna sequence to list of basepairs
bp_list = list(no_white_uppercase)

# pop a bp from end of bp_list, get the complement, and add it to rev_comp list
# this reverses and comp's the sequence in one loop
while bp_list:
    bp = bp_list.pop()
    if bp == 'A':
        complement_bp = 'T'
    elif bp == 'T':
        complement_bp = 'A'
    elif bp == 'C':
        complement_bp = 'G'
    elif bp == 'G':
        complement_bp = 'C'
        # alert user for N
    elif bp == 'N':
        print("Your input sequence contains an 'N' character.")
        complement_bp = 'N'
    else:
        print("Your input sequence contains non- ATCG characters.")
        break
    rev_comp_list.append(complement_bp)

# take the rev_comp list and concatenate it together
rev_comp_seq = ''.join(rev_comp_list)
print('Reverse complement: {}'.format(rev_comp_seq))
