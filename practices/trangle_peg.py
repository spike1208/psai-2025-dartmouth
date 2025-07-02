

def triangular(a):
    return a * (a + 1) // 2

def print_state_15(a):
    
    # Calculate the maximum width (last row has 5 numbers + 4 spaces)
    max_width = len(" ".join(str(x) for x in a[triangular(4):triangular(5)]))
    
    for i in range(1, 6):
        start = triangular(i - 1)
        end = triangular(i)
        row = a[start:end]
        row_str = " ".join('#' if x == 1 else '0' for x in row)
        print(row_str.center(max_width))

def rotate_triangle_120(initial):
    # Hardcoded correct 120° rotation mapping
    # i.e., new_list[new_index] = initial[old_index]
    mapping = {
        0: 14,
        1: 9,   2: 13,
        3: 5,   4: 8,   5: 12,
        6: 2,   7: 4,   8: 7,   9: 11,
        10: 0, 11: 1,  12: 3, 13: 6, 14: 10
    }

    rotated = [0] * 15
    for old_idx, new_idx in mapping.items():
        rotated[new_idx] = initial[old_idx]
    return rotated

def jumpable(initial):
    found = False
    n = len(initial)
    for i in range(2, 6):  # Rows 3 to 5
        start = triangular(i)
        end = triangular(i + 1)

        # Right jump: 1 1 0 → 0 0 1
        for j in range(start, min(end - 2, n - 2)):
            if initial[j] == 1 and initial[j + 1] == 1 and initial[j + 2] == 0:
                new_state = initial.copy()
                new_state[j] = 0
                new_state[j + 1] = 0
                new_state[j + 2] = 1
                print("→ Right jump:")
                print_state_15(new_state)
                found = True

        # Left jump: 0 1 1 → 1 0 0
        # Make sure the loop never starts with j < 2 (to prevent j-2 < 0)
        for j in range(max(start + 2, 2), min(end, n)):
            # Debug print:
            # print(f"Checking left jump at indices {j-2}, {j-1}, {j}")
            if (j - 2) < 0 or (j >= n) or (j - 1) < 0:
                # Skip invalid indices just in case
                continue
            if initial[j - 2] == 0 and initial[j - 1] == 1 and initial[j] == 1:
                new_state = initial.copy()
                new_state[j - 2] = 1
                new_state[j - 1] = 0
                new_state[j] = 0
                print("← Left jump:")
                print_state_15(new_state)
                found = True

    if not found:
        print("No jumpable pattern found.")

def main_argparse():
    pass

def main_input():
    initial = [0 for _ in range(15)]
    a = input("pass in all indicies that are pegged (space delimited)").strip()
    a = [int(item.strip()) for item in a.split()]
    for i in a:
        initial[i-1] = 1
    print_state_15(initial)
    jumpable(initial)
    rotated = rotate_triangle_120(initial)
    print_state_15(rotated)
    jumpable(rotated)
    rotated = rotate_triangle_120(rotated)
    print_state_15(rotated)
    jumpable(rotated)


if __name__ == "__main__":
    #main_argparse
    main_input()