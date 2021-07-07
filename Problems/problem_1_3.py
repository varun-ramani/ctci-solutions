def replace(input_str, length):
    input_str = list(input_str)

    for index in range(length, -1, -1):
        if input_str[index] == " ":
            for iter_index in range(length, index, -1):
                input_str[iter_index + 2] = input_str[iter_index]

            input_str[index:(index+ 3)] = "%20"

            length += 2

    return "".join(input_str)

print(replace("hello world..", 10))
print(replace(" helloworld..", 10))
