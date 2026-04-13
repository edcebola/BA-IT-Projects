from exercise4 import Queue


def get_pairs(numbers):
    evenNums = Queue()
    oddNums = Queue()

    pairs = []

    for num in numbers:
        if num % 2 == 0:
            if len(oddNums) != 0:
                odd_num = oddNums.dequeue()
                pairs.append((num, odd_num))
            else:
                evenNums.enqueue(num)
        elif num % 2 != 0:
            if len(evenNums) != 0:
                even_num = evenNums.dequeue()
                pairs.append((even_num, num))
            else:
                oddNums.enqueue(num)
    return pairs
