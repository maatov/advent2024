from itertools import product

contents = open("input.txt").readlines()


def calculate_calibration(include_concatenation = False) -> int:
    results = []

    calibration_result = 0

    for line in contents:
        target, numbers = (int(line.split(":")[0]), [int(num) for num in line.split(":")[1].split()])
        op_list = ["+", "*", "||"] if include_concatenation else ["+", "*"]
        p = product(op_list, repeat=len(numbers) - 1)

        for operators in p:
            res = 0
            for op, num in zip([""] + list(operators), numbers):
                if not op:
                    res = num
                if op and op == "+":
                    res += num
                if op and op == "*":
                    res *= num
                if include_concatenation and op and op == "||":
                    # work with `numbers` copy and update it with concatenations
                    pass

            #print(res)
            if res == target:
                results.append(res)

        calibration_result += target if any([res == target for res in results]) else 0
    return calibration_result


# Part 1
print(calculate_calibration())

# Part 2
#print(calculate_calibration(True))