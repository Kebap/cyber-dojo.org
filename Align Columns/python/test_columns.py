from columns import *

def test_read_file():
    assert read_file() == """Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space."""

def test_read_lines():
    input_text = """Line1
Line2"""
    output = ["Line1", "Line2"]
    assert read_lines(input_text) == output

def test_split_text():
    input_text = "Words$To$Split"
    output = ["Words", "To", "Split"]
    assert split_text(input_text) == output

def test_append_spaces():
    input_text = "Test"
    output = "Test     "
    assert append_spaces(input_text, 5) == output

def test_calc_length():
    input_data = ["We", "are", "the", "world"]
    output_data = 5
    assert calc_length(input_data) == output_data
    
def test_join_line():
    input_data = ["We", "are", "the", "world"]
    output_data = "We are the world"
    assert join_line(input_data) == output_data

def test_calc_column_lengths_1():
    input_data = [["We", "are"]]
    output_data = (2, 3)
    assert calc_column_lengths(input_data) == output_data

def test_calc_column_lengths_2():
    input_data = [["We", "are"], ["the", "world"]]
    output_data = (3, 5)
    assert calc_column_lengths(input_data) == output_data
    
def test_append_row():
    input_data = [["We", "are"], (3, 5)]
    output_data = ["We ", "are  "]
    assert append_row(*input_data) == output_data

def test_append_columns():
    input_data = [["We", "are"], ["the", "world"]]
    output_data = [["We ", "are  "], ["the", "world"]]
    assert append_columns(input_data) == output_data

def test_split_rows():
    input_data = ["Words$To$Split", "Words$To$Split"]
    output_data = [["Words", "To", "Split"], ["Words", "To", "Split"]]
    assert split_rows(input_data) == output_data
    
def test_end_to_end():
    input_data = ""
    output_data = ""
    assert end_to_end() == output_data
    
#
#
# 

def _test_template():
    input_data = ["We", "are", "the", "world"]
    output_data = 5
    assert calc_length(input_data) == output_data
    
#
#
#
