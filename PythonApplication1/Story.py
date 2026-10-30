
import subprocess

from config import PATH_TO_FILE
from classes import Part

pathes = [[1, 72, 76, 55, 92, 35, 40, 71, 90, 65, 11, 60, 16, 89, 58, 33, 13, 38, 100], [42, 77, 7, 90], [56, 3, 15, 10, 46, 88, 33]]
options = {
    35: [97, 40],
    97: [40, 71, 42],
    11: [56, 60]
}

def extract_parts(path_to_file):
    result = []

    with open(path_to_file, "r", encoding="utf-8") as story_text_file:
        lines = story_text_file.readlines()

        part_number = extract_number(lines[0])
        content = ""

        for i in range(1, len(lines)):
            line = lines[i]
            if "#" in line:
                result.append(Part(part_number, content))
                content = ""
                part_number = extract_number(line)
                continue

            content += line

        result.append(Part(part_number, content))
        return result

def assign_next_parts(pathes: list, parts: list):
    for path in pathes:
        part = find_part(path[0], parts)

        for i in range(1, len(path)):
            next_part = find_part(path[i], parts)
            part.next_part = next_part
            part = next_part

def find_part(part_number, parts):
    return next((part for part in parts if part.number == part_number))

def extract_number(line : str):
    result = ""
    for i in range(len(line) - 1):
        if line[i].isnumeric():
            result += line[i]

        if len(result) > 0 and not line[i + 1].isnumeric():
            return int(result)
    
    return int(result + line[-1])

def clear_console():
    subprocess.run("cls", shell=True)

def game(parts, options):
    current_part = parts[0]

    while True:
        clear_console()
        print(current_part)
        print(current_part.read())

        if current_part.number in options:

            choice = ""
            while choice not in options[current_part.number]:
                choice = input("Which part do you want to read next? ")
                try:
                    int(choice)
                except:
                    print("Incorrect input")
                else:
                    choice = int(choice)

            current_part = find_part(choice, parts)
            continue
        else:
            if (current_part.next_part == None):
                print("Thank you for reading")
                break
            else:
                current_part = current_part.next_part
        input()

        

def __main__():
    parts = extract_parts(PATH_TO_FILE)
    assign_next_parts(pathes, parts)
    game(parts, options)


if __name__ == "__main__":
    __main__()