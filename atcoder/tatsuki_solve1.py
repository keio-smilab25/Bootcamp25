import sys

def solve():
    input_str = sys.stdin.readline()
    if not input_str:
        return
    n, a, b = map(int, input_str.split())

    total_sum = 0

    for i in range(1, n + 1):
        digit_sum = sum(map(int, str(i)))
        # 各桁の和が A 以上 B 以下であるか確認
        if a <= digit_sum <= b:
            total_sum += i

    # 結果を出力
    print(total_sum)

if __name__ == "__main__":
    solve()