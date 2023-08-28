import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char, self.freq, self.left, self.right = char, freq, None, None

    def __lt__(self, other):
        return self.freq < other.freq if isinstance(other, HuffmanNode) else NotImplemented

def build_huffman_tree(chars, freqs):
    heap = [HuffmanNode(c, f) for c, f in zip(chars, freqs)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        combined = HuffmanNode(None, heap[0].freq + heap[1].freq)
        combined.left, combined.right = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, combined)
    
    return heapq.heappop(heap)

def build_huffman_codes(root, code='', codes={}):
    if root:
        if root.char:
            codes[root.char] = code
        build_huffman_codes(root.left, code + '0', codes)
        build_huffman_codes(root.right, code + '1', codes)

def encode_decode_string(encoded, root):
    decoded, current = '', root
    for bit in encoded:
        current = current.left if bit == '0' else current.right
        if current.char:
            decoded += current.char
            current = root
    return decoded

def get_input(count, data_type):
    return [data_type(input(f"Enter {'character' if data_type == str else 'probability'} {i+1}: ")) for i in range(count)]

n = int(input("Enter number of characters: "))
characters = get_input(n, str)
frequencies = get_input(n, float)

huffman_tree = build_huffman_tree(characters, frequencies)
huffman_codes = {}
build_huffman_codes(huffman_tree, '', huffman_codes)

string = input("Enter a string to encode: ")
encoded_string = ''.join(huffman_codes[char] for char in string)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(char, ":", code)

if input("Decode encoded string? (Y/N): ").lower() == 'y':
    binary_number = encoded_string if input("Do you have binary? (Y/N): ").lower() == 'y' else input("Enter binary: ")
    decoded_string = encode_decode_string(binary_number, huffman_tree)
    print("Decoded encoded string:", decoded_string)
else:
    print("Decoding skipped.")
