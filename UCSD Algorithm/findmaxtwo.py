def findmaxtwo(numbers):
    max_value = 0
    n = len(numbers)
    for first in range(n):
        for second in range(first+1,n):
            max_value = max(max_value,numbers[first] * numbers[second])
    return max_value

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int,input().split()))
    print(findmaxtwo(input_numbers))