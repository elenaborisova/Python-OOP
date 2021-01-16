def fibonacci():
    prev_num = 0
    curr_num = 1
    while True:
        yield prev_num
        prev_num, curr_num = curr_num, prev_num + curr_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
