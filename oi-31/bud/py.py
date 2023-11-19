arr = [
    [
        [2,3],[3,3],[4,3]
    ],
    [
        [4,2],[4,3],[4,4]
    ],
    [
        [4,2],[4,1],[4,0]
    ]
]

def check_no_common_points(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            common_points = any(point1 in arr[j] for point1 in arr[i])
            if not common_points:
                return True
    return False

arr = [
    [
        [2,3],[3,3],[4,3]
    ],
    [
        [4,2],[4,3],[4,4]
    ],
    [
        [4,1],[4,2],[0,0]
    ]
]

print(check_no_common_points(arr))