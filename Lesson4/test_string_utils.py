import pytest
from string_utils import StringUtils
@pytest.mark.parametrize("input_string, except_output", [
    ("google", "Google"),
    ("Мир", "Мир"),
    ("красота", "Красота")])

def test_capitilize_pozitiv(input_string, except_output):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == except_output


@pytest.mark.parametrize("input_string, except_output", [
    ("", ""),
    (" ", " ")])

def test_capitilize_negativ(input_string, except_output):
    string_utils = StringUtils()
    res = string_utils.capitilize(input_string)
    assert res == except_output

    
@pytest.mark.parametrize("input_string, except_output", [
    (" Google", "Google"),
    ("Мир", "Мир"),
    ("  123красота", "123красота")
    ])

def test_trim_pozitiv(input_string, except_output):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == except_output

@pytest.mark.parametrize("input_string, except_output", [
    ("", ""),
    ("   ", "")
    ])

def test_trim_negativ(input_string, except_output):
    string_utils = StringUtils()
    res = string_utils.trim(input_string)
    assert res == except_output


@pytest.mark.parametrize("input_string, except_output", [
    ("google,yandex,opera,samsung", ["google","yandex","opera","samsung"]),
    (" ,  ,   ", [" ","  ","   "])
    ])

def test_to_list_pozitiv(input_string, except_output):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string)
    assert res == except_output

@pytest.mark.parametrize("input_string, except_output", [
    ("", [])
    ])

def test_to_list_negativ(input_string, except_output):
    string_utils = StringUtils()
    res = string_utils.to_list(input_string)
    assert res == except_output

@pytest.mark.parametrize("input_string, letter, result", [
    ("googl", "g", True)                        
])                        

def test_containst_pozitiv(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, letter)
    assert res == result

@pytest.mark.parametrize("input_string, letter, result", [
    ("googl", "f", False)                        
])                        

def test_containst_negativ(input_string, letter, result):
    string_utils = StringUtils()
    res = string_utils.contains(input_string, letter)
    assert res == result


@pytest.mark.parametrize("input_string, symbol, result", [
    ("googl", "l", "goog"),
    ("Елена", "е", "Елна"),
    ("2024", "4", "202"),
    ("пирамиды Боснии", " ", "пирамидыБоснии")                       
])                        

def test_delete_symbol_pozitiv(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == result

@pytest.mark.parametrize("input_string, symbol, result", [
    ("googl", "f", "googl"),
    ("", "", ""),
    ("", "4", ""),
    ("пирамида", "", "пирамида"),
    ("высота", " ", "высота")                       
])  

def test_delete_symbol_negativ(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input_string, symbol)
    assert res == result

@pytest.mark.parametrize("input_string, symbol, result", [
    ("Googl", "G", True),
    ("Елена", "Е", True),
    ("2024", "2", True),
    ("  ", "  ", True),
    ("Anna-Mariya", "A", True),
    ("", "", True)                       
])                      

def test_starts_with_pozitiv(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, symbol)
    assert res == result

@pytest.mark.parametrize("input_string, symbol, result", [
    ("googl", "G", False),
    ("Елена", "e", False),
    ("2024", "0", False),
    ("", "@", False),
    ("Anna", "S", False),
])                      

def test_starts_with_negativ(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(input_string, symbol)
    assert res == result


@pytest.mark.parametrize("input_string, symbol, result", [
    ("Googl", "l", True),
    ("Елена", "а", True),
    ("2024", "4", True),
    ("  ", "  ", True),
    ("Anna-Mariya", "a", True),
    ("", "", True)                       
])                      

def test_end_with_pozitiv(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, symbol)
    assert res == result


@pytest.mark.parametrize("input_string, symbol, result", [
    ("googl", "r", False),
    ("Елена", "q", False),
    ("2024", "7", False),
    ("", "#", False),
    ("Anna", "S", False),
])                      

def test_end_withh_negativ(input_string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(input_string, symbol)
    assert res == result


@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("  ", True)                      
])                      

def test_is_empty_pozitiv(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize("string, result", [
    ("не пусто", False),
    (" не пусто с пробелом ", False),
    ("123", False)                      
])                      

def test_is_empty_negativ(string, result):
    string_utils = StringUtils() 
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [
    (["м", "и", "р"], ".", "м.и.р"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Первый", "Третий"], "Второй", "ПервыйВторойТретий"),
    (["ц", "у", "м"], "", "цум")
])

def test_list_to_string_pozitiv(lst, joiner, result):
    string_utils = StringUtils()
    if joiner == None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [
    ([], None, ""),
    ([], ",", ""),
    ([], "крот", ""),
])

def test_list_to_string_negativ(lst, joiner, result):
    string_utils = StringUtils()
    if joiner == None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)
    assert res == result
