import random

def create_post(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding
        lines = file.readlines()
    
    if not lines:
        return None  # Return None if the file is empty

    # Pick a random line
    random_line = random.choice(lines)
    
    # Remove the picked line from the list of lines
    lines.remove(random_line)

    # Rewrite the file without the removed line
    with open(file_path, 'w', encoding='utf-8') as file:  # Specify encoding
        file.writelines(lines)
    
    return random_line.strip()  # Return the random line without newline characters
