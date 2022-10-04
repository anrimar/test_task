def max_lucky_seq(seq):
    if not isinstance(seq, str):
        seq = ''.join(seq)
    longest_lucky_sub_seq = ''
    sub_seq = ''
    for s in seq:
        if s=='5' or s=='6':
            sub_seq+=s
        elif '5' in sub_seq and '6' in sub_seq and len(sub_seq)>len(longest_lucky_sub_seq):
                longest_lucky_sub_seq = sub_seq
                
    else:
        if '5' in sub_seq and '6' in sub_seq and len(sub_seq)>len(longest_lucky_sub_seq):
                longest_lucky_sub_seq = sub_seq
    return longest_lucky_sub_seq
        
        
if __name__ == "__main__":
    print(max_lucky_seq('4556432455665334'))