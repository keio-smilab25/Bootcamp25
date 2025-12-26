def main():
    # 1行目の整数の入力
    a = int(input())
    
    # 2行目のスペース区切りの整数の入力
    b, c = map(int, input().split())
    
    # 3行目の文字列の入力
    s = input()
    
    # 計算と出力
    print(a + b + c, s)

if __name__ == '__main__':
    main()