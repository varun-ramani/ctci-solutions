class LinearSolution:
    def solution(input_str):
        curr_char = input_str[0]
        count = 0
        char_counts = []

        for index, char in enumerate(input_str):
            if char != curr_char:
                char_counts += curr_char, str(count)
                curr_char = char
                count = 1
            else:
                count += 1

            if index == len(input_str) - 1:
                char_counts += curr_char, str(count)

        new_str = "".join(char_counts)
        if len(new_str) >= len(input_str):
            return input_str
        return new_str

print(LinearSolution.solution("abcdddddddddddddddd"))