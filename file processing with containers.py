from collections import Counter

def process_numbers(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    
    frequencies = Counter(numbers)
    print(f"Numbers: {numbers}")
    print(f"Frequencies: {dict(frequencies)}")

process_numbers("num.txt")

