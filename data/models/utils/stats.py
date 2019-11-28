def mean(numbers):
    length = len(numbers)

    if length > 0:
        return float(sum(numbers)) / length
    else:
        return 0

def median(numbers):
    length = len(numbers)

    if length > 0:
        numbers_sorted = sorted(numbers)
        half = length // 2
        if length % 2:
            return numbers_sorted[half]
        else:
            return float(numbers_sorted[half - 1] + numbers_sorted[half]) / 2
    else:
        return 0
