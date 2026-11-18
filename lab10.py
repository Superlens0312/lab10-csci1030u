# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    '''
    I need to evaluate the expression and return the integer result.

    # Outline:

    First I create a stack using a Python list.
    I loop through the tokens from left to right.
    If the token is a number, I push it onto the stack.
    If the token is an operator, I pop the last two numbers,
    perform the operation, and push the result back onto the stack.
    After processing all the tokens, I return the remaining
    value in the stack.

    # Example:
    tokens = ["5", "2", "+", "4", "*"]

    5 and 2 are added together to get 7.
    Then 7 and 4 are multiplied together to get 28.
    I return 28.
    '''
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            first = stack.pop()
            second = stack.pop()
            if token == "+":
                # addition
               result = first + second
               stack.append(result)
            elif token == "-":
                # subtraction
                result = second - first
                stack.append(result)
            elif token == "*":
                # multiplication
                result = first * second
                stack.append(result)
            elif token == "/":
                # division
                result = int(second / first)
                stack.append(result)

    return stack.pop()


def decode_string(s):
    # Outline:
    '''
    I need to decode a string by repeating the characters inside
    brackets based on the number before the opening bracket.
    The brackets can also be nested.

    # Outline:

    First I create a stack to store the previous strings and
    their repeat counts.
    I loop through each character in the string.
    If the character is a number, I build the repeat count.
    If the character is an opening bracket, I push the current
    string and repeat count onto the stack.
    If the character is a closing bracket, I pop the previous
    string and repeat count and combine them with the current string.
    Otherwise, I add the character to the current string.
    After processing all characters, I return the decoded string.

    # Example:
    s = "3[a]2[bc]"

    3[a] becomes aaa.
    2[bc] becomes bcbc.
    I return "aaabcbc".
    '''
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_num = 0
    current_string = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)

        elif char == "[":
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0

        elif char == "]":
            previous_string, repeat = stack.pop()
            current_string = previous_string + current_string * repeat

        else:
            current_string += char

    return current_string


def daily_temperatures(temps):
    # Outline:
    '''
    I need to find how many days it takes for each temperature
    to have a warmer temperature. If there is no warmer day,
    I return 0 for that day.

    # Outline:

    First I create a result list filled with zeros and an empty stack.
    I loop through the temperatures using their indexes.
    I use the stack to keep track of days that are waiting
    for a warmer temperature.
    If the current temperature is warmer than a previous day
    stored in the stack, I pop that index.
    I calculate how many days passed and store the result
    at that previous day's index.
    I repeat this while there are previous days waiting
    for a warmer temperature.
    Then I push the current index onto the stack.
    After the loop, I return the result list.

    # Example:
    temps = [30, 40, 50, 60]

    30 waits 1 day for 40.
    40 waits 1 day for 50.
    50 waits 1 day for 60.
    60 has no warmer day, so it gets 0.

    I return [1, 1, 1, 0].
    '''
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    #  print(eval_rpn(["2", "1", "+", "3", "*"]))  
    #  print(eval_rpn(["2", "1", "+", "3", "*"]))
    #  print(eval_rpn(["4", "13", "5", "/", "+"]))
    #  # 9
    pass
    


if __name__ == "__main__":
    main()
