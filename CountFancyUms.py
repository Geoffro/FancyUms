import re

def count_um_in_file(file_name: str):
    with open(file_name, 'r') as file:
        content = file.read()

    # \b matches the boundary between a word char and a non-word char
    um_count = len(re.findall(r'\bum\b', content))
    other_um_count = len(re.findall(r'\bumm?\b', content)) - um_count

    print(f'Isolated "um" count: {um_count}')
    print(f'Other variations like "umm": {other_um_count}')

if __name__ == "__main__":

    count_um_in_file('Transcript.txt')