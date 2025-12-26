import sys

def check_product_parity(num_a, num_b):
    product = num_a * num_b

    if product % 2 == 0:
        return 'Even'
    return 'Odd'

def main():
    try:
        input_line = sys.stdin.readline()
        if not input_line:
            return
        num_a, num_b = map(int, input_line.split())

        result = check_product_parity(num_a, num_b)
        print(result)

    except ValueError:
        pass


if __name__ == '__main__':
    main()