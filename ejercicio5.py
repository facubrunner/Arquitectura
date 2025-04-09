def calcu(op, num1, num2):
    if op == "sum":
        print(num1 + num2)
    if op == "res":
        print(num1 - num2)
    if op == "multi":
        print(num1 * num2)
    if op == "div":
        print(num1 / num2)
calcu("sum", 10, 5)