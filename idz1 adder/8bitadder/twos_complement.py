def twos_complement_to_decimal(bin_str):
    is_negative = bin_str[0] == '1'
    
    if is_negative:
        bin_str = ''.join('1' if bit == '0' else '0' for bit in bin_str)
        bin_str = bin(int(bin_str, 2) + 1)[2:]
    
    decimal = int(bin_str, 2)
    
    if is_negative:
        decimal = -decimal
    
    return decimal

def to_decimal(bin_str):
    return int(bin_str, 2)
