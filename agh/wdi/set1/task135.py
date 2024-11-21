T = [[0, 0, 0, 0, 0, 0, 0, 9],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 2]]

def znajdz_trase(T, w, k, suma):
    # print("w:", w,"k:",k, "suma:", suma)
    if w == 7:
        return suma
    koszt = float("inf")
    for i in [-1,0,1]:
        if k + i > 0 and k + i < 8:
            koszt = min(koszt, znajdz_trase(T, w + 1, k + i, suma + T[w+1][k]))
            # print("\t", koszt)

    return koszt


def start(T, k):
    koszt = T[0][k]
    return znajdz_trase(T, 0, k, koszt)

print(start(T, 5))