# # def assign_codes(n, p, M, connections):
# #     codes = ['A', 'B', 'C']
    
# #     # Inicjalizacja kodów identyfikacyjnych
# #     satellite_codes = {i: '' for i in range(1, 2 * n + 1)}
    
# #     # Przydzielanie kodów dla par satelitów
# #     for i in range(1, n + 1):
# #         satellite_codes[i] = codes[0]
# #         satellite_codes[i + n] = codes[1]
# #         codes = codes[1:] + [codes[0]]
    
# #     # Ustawianie komunikacji między satelitami tej samej firmy
# #     for i in range(1, n + 1):
# #         for j in range(i + 1, n + 1):
# #             satellite_codes[i], satellite_codes[j] = satellite_codes[j], satellite_codes[i]
# #             satellite_codes[i + n], satellite_codes[j + n] = satellite_codes[j + n], satellite_codes[i + n]
    
# #     # Ustawianie komunikacji między satelitami różnych firm
# #     for connection in connections:
# #         a, b = connection
# #         satellite_codes[a], satellite_codes[b] = satellite_codes[b], satellite_codes[a]
    
# #     # Wypisanie wyniku
# #     print(M)
# #     for i in range(1, 2 * n + 1):
# #         print(satellite_codes[i])

# # # Przykład użycia
# # n, p, M = map(int, input().split())
# # connections = [list(map(int, input().split())) for _ in range(p)]

# # assign_codes(n, p, M, connections)


# import itertools

# def generate_codes(n, p, M, connections):
#     # Generate all possible codes of length M
#     possible_codes = list(itertools.product('ABC', repeat=M))

#     # Assign the first 2n codes to the satellites
#     codes = possible_codes[:2*n]

#     # Check each required connection
#     for a, b in connections:
#         # Decrease the satellite numbers by 1 to use them as indices
#         a -= 1
#         b -= 1

#         # Check if the codes of the two satellites have a common character
#         common_char = any(c1 == c2 for c1, c2 in zip(codes[a], codes[b]))

#         # If not, modify the code of the second satellite
#         if not common_char:
#             for i in range(M):
#                 if codes[a][i] != codes[b][i]:
#                     codes[b] = codes[b][:i] + codes[a][i] + codes[b][i+1:]
#                     break

#     # Convert the codes from tuples to strings
#     codes = [''.join(code) for code in codes]

#     return M, codes

# # Test the function
# n, p, M = map(int, input().split())
# connections = [list(map(int, input().split())) for _ in range(p)]
# print(generate_codes(n, p, M, connections))

def assign_codes():
    n, p, M = map(int, input().split())
    connections = [list(map(int, input().split())) for _ in range(p)]

    # Assign the same code to all satellites from the same company
    codes = ['A' * i for i in range(1, n+1)] * 2

    # For each required connection between satellites from different companies,
    # add a common character to their codes
    for a, b in connections:
        common_char = 'C'
        codes[a-1] += common_char
        codes[b-1] += common_char

    # The length of the longest code is the length of the codes
    m = max(len(code) for code in codes)

    # Make all codes the same length by padding with 'B'
    codes = [code.ljust(m, 'B') for code in codes]

    return m, codes

# Test the function
print(assign_codes())