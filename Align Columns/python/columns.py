from itertools import zip_longest as zippel

def read_file(file_name = "input.txt"):
    with open(file_name, "r") as file:
        return file.read().strip()

def read_lines(multiline_text):
    return multiline_text.split("\n")

def split_text(a_text):
    return a_text.split("$")

def split_rows(list_of_texts):
    return list(split_text(t) for t in list_of_texts)

def append_spaces(a_text, ammount):
    return a_text + " " * ammount

def calc_length(texts_of_a_row):
    return max(len(s) for s in texts_of_a_row)

def join_line(texts_of_a_row):
    return " ".join(texts_of_a_row)

def calc_column_lengths(text_in_2d_matrix):
    columns = zippel(*text_in_2d_matrix, fillvalue = "")
    return tuple(calc_length(c) for c in columns)

def append_row(texts_of_a_row, lengths):
    return list(append_spaces(text, length - len(text)) for text, length in zip(texts_of_a_row, lengths))
    
def append_columns(text_in_2d_matrix):
    lengths = calc_column_lengths(text_in_2d_matrix)
    return list(append_row(texts_of_a_row, lengths) for texts_of_a_row in text_in_2d_matrix)
    
def end_to_end():
    lines = read_lines(read_file())
    text_in_2d_matrix = split_rows(lines)
    appended_texts = append_columns(text_in_2d_matrix)
    joined_texts = [join_line(t) for t in appended_texts]
    print()
    for line in joined_texts: 
        print(line)
    print()        
    return ""
