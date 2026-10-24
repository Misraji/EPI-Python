# Pg 25: Count number of bits that are set to 1.
def count_bits(x: int) -> int:
    x_copy = x
    num_bits = 0
    while x > 0:
        num_bits += x & 1
        x >>= 1
    print("count_bits(",x_copy,") = ", num_bits) 
    return num_bits

def parity(x:int) -> int:
    x_copy = x

    result = 0
    while x > 0: 
        result ^= (x & 1)
        x >>= 1

    print("parity(",x_copy,") = ", result) 
    return result

def parity_cache(x: int) -> int:
    mask_size: int = 16
    bit_mask:int = 0xFFFF

    return (PRECOMPUTED_PARITY[(x >> (3*mask_size))] ^
            PRECOMPUTED_PARITY[(x >> (2*mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask] ^
            PRECOMPUTED_PARITY[(x & bit_mask)]
           )

# Pg 29: Swap the i-th and j-th bits in the number x.
def swap_bits(x:int, i:int, j:int) -> int:
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

if __name__ == "__main__":
    # Test count_bits.
    count_bits(0)
    count_bits(1)
    count_bits(2)
    count_bits(7)

    # Test Parity
    parity(0)
    parity(1)
    parity(2)
    parity(3)
    parity(7)
