def arithmetic_arranger(problems, solve = False):

    top = []
    bottom = []
    dashes = []
    solutions = []

    if len(problems) > 5:
         return "Error: Too many problems."

    for problem in problems:
        problem_list = problem.split()
        operand1 = problem_list[0]
        operator = problem_list[1]
        operand2 = problem_list[2]

        if operand1.isdigit() and operand2.isdigit():
            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Numbers must only contain digits."

        if operator == "+":
            answer = int(operand1) + int(operand2)
        elif operator == "-":
            answer = int(operand1) - int(operand2)
        else:
            return "Error: Operator must be '+' or '-'."

        width = max(len(operand1), len(operand2)) + 2

        tophalf = str(operand1).rjust(width)
        bottomhalf = operator + str(operand2).rjust(width -1)
        separator = ""
        for dash in range(width):
            separator += "-"
        solution = str(answer).rjust(width)

        top.append(tophalf)
        bottom.append(bottomhalf)
        dashes.append(separator)
        solutions.append(solution)

    s = '    '
    ftop = s.join(top)
    fbot = s.join(bottom)
    fdash = s.join(dashes)
    fsolve = s.join(solutions)


    if solve == True:
        arranged_problems = f'{ftop}\n{fbot}\n{fdash}\n{fsolve}'
    else:
        arranged_problems = f'{ftop}\n{fbot}\n{fdash}'

    return arranged_problems