def convert_to_binary(num: int) -> str:
    result = ""
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result[::-1]  # reverse


def count_consecutive_ones(x: str) -> int:
    max_count = 0
    current = 0

    for ch in x:
        if ch == '1':
            current += 1
            max_count = max(max_count, current)
        else:
            current = 0

    return max_count


if __name__ == '__main__':
    n = int(input().strip())
    print(count_consecutive_ones(convert_to_binary(n)))
