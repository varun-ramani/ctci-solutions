from collections import defaultdict

class DictSolution:
    def solution(input_str: str):
        rep = defaultdict(bool)

        for char in input_str:
            rep[char] = not rep[char]

        found_odd = False
        for is_odd in rep.values():
            if is_odd:
                if found_odd:
                    return False

                found_odd = True

        return True

class BitVectorSolution:
    def toggle_bit(bit_vector, bit_index):
        return bit_vector ^ (1 << bit_index)

    def solution(input_str: str):
        bit_vector = 0
        for chr in input_str:
            bit_vector = BitVectorSolution.toggle_bit(bit_vector, ord(chr) - ord('a'))

        return (bit_vector & (bit_vector - 1)) == 0

print(BitVectorSolution.solution("ajajka"))