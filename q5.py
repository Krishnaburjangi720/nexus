def calculate(expression: str) -> float:
    expr = expression.replace(" ", "")
    nums = []
    ops = []
    i = 0

    while i < len(expr):
        if expr[i] in "+-*/":
            ops.append(expr[i])
            i += 1
        else:
            num = ""
            if i == 0 and expr[i] == '-':
                num += expr[i]
                i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            nums.append(float(num))

    i = 0
    while i < len(ops):
        if ops[i] == "*":
            nums[i] *= nums[i + 1]
        elif ops[i] == "/":
            nums[i] /= nums[i + 1]
        else:
            i += 1
            continue
        nums.pop(i + 1)
        ops.pop(i)

    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            result += nums[i + 1]
        else:
            result -= nums[i + 1]

    return round(result, 2)
