def comp(seq):
    comp_dict={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    seq_comp= ""
    for char in seq:
        seq_comp += comp_dict[char]
    return seq_comp

def rev(src):
    seq_rev = "".join(reversed(src))
    return seq_rev

def comp_rev(src):
    tmp = comp(src)
    return rev(tmp)

src = input("DNA sequence:")
cnvt = int(input("1(Comp), 2(Rev), 3(Comp_Rev) :"))
if cnvt >=1 and cnvt <= 3:
    if cnvt == 1:
        rst = comp(src)
    elif cnvt == 2:
        rst = rev(src)
    else:
        rst = comp_rev(src)
    print(src, '->', rst)
else:
    print("1:comp 2:rev 3:comp_rev!!!!!!!!!!!")
