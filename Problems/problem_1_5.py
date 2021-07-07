class LinearSolution:
    def solution(in1, in2):
        if in1 == in2:
            return True

        return LinearSolution.try_del(in1, in2) or LinearSolution.try_repl(in1, in2)

    def try_del(in1, in2):
        len1, len2 = len(in1), len(in2)

        if abs(len1 - len2) != 1:
            return False

        if len1 > len2:
            target = in1
            anchor = in2
        else:
            target = in2
            anchor = in1

        offset = 0
        current_index = 0
        while current_index < len(anchor):
            if anchor[current_index] != target[current_index + offset]:
                if offset == 1:
                    return False
                else:
                    offset = 1
            else:
                current_index += 1

        return True

    def try_repl(in1, in2):
        len1, len2 = len(in1), len(in2)

        if len1 != len2:
            return False

        used_replace = False
        for index in range(len1):
            if in1[index] != in2[index]:
                if used_replace:
                    return False
                used_replace = True

        return True