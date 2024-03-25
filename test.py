def decode(message_file):
    # Read the content of the file and sort lines based on the numbers
    with open(message_file, 'r') as file:
        lines = sorted(file.readlines(), key=lambda x: int(x.split()[0]))

    decoded_message = []
    step = 1

    # Iterate over each line of the pyramid
    for line in lines:
        # Split the line into number and word
        num, word = line.strip().split()
        num = int(num)

        if num == step:  # Only consider words at the end of the pyramid lines
            step += len(decoded_message) + 2
            decoded_message.append(word)  # Append the word to the decoded message

    # Combine the decoded words into a single string
    decoded_string = ' '.join(decoded_message)

    return decoded_string


# Example usage:
decoded_message = decode("coding.txt")
print(decoded_message)
