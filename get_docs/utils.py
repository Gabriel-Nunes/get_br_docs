# -*- coding: utf-8 -*-
from validate_docbr import CPF, CNPJ
import re
import pandas as pd
from unicodedata import normalize


def unique_values(values: list) -> list:
    """
    Filter duplicated values in a given list.
    """
    unique_values = set(values)
    return list(unique_values)

def clean_doc_num(cpf: str) -> str:
    """
    Filter non alphanumeric charcters from a document
    number.
    """
    return "".join([num for num in cpf if num.isalnum()])


def normaliza(txt: str) -> str:
    """
    Returns a copy of a string replacing special characters
    by its ASCII equivalent.
    Also removes duplicated spaces.
    """
    result = normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")
    result.strip()
    result = re.sub("\s{2,}", " ", result)
    return result


def short_form(phrase: str, max: int) -> str:
    """
    Abbreviate a phrase to "max" number of characters.
    """
    phrase_list = phrase.split(" ")
    max_letters = 4
    new_phrase = phrase

    while len(new_phrase) > max:
        for i in range(len(phrase_list)):
            word = phrase_list[i]
            if len(word) > 1:
                phrase_list[i] = word[:max_letters]
            new_phrase = " ".join(phrase_list)
            if len(new_phrase) <= max:
                break
        max_letters -= 1
    return new_phrase


def to_capitalized(nome: str) -> str:
    """
    Capitalize words skipping portuguese prepositions.
    """
    name = nome.lower()
    p = [
        "a",
        "o",
        "e",
        "da",
        "do",
        "dos",
        "das",
        "de",
        "di",
        "em",
        "para",
        "com",
        "por",
    ]
    return " ".join(
        list(map(lambda w: w.capitalize() if w not in p else w, name.split()))
    )


def to_currency(x: str) -> str:
    """
    returns a string in European (also Brazilian)
    currency format, between double quotes ("00,00")

    :param x: string 00.00
    :return: string "00,00"
    """
    # regex para moedas no formato $ XX.XX
    regex2 = re.compile(r"\d+\.\d\b")
    regex3 = re.compile(r"\d+\.\d\d\b")

    if regex3.search(x):
        return x.replace(".", ",")
    elif regex2.search(x):
        x = x + "0"
        return x.replace(".", ",")
    else:
        return x + ",00"


def find_cep(text: str) -> list:
    """
    Returns a list of brazilian zip code (CEP)
    finded in a given string.
    """
    cep = re.findall(r"\b(\d\d\d\d\d-?\d\d\d)\b", text)
    return unique_values([clean_doc_num(c) for c in cep])


def lefted_zeros(lenght: int, num: str):
    """
    Add left zeros to a string number
    up to it get "lenght" size.
    """
    while len(num) < lenght:
        num = "0" + num
    return num


def find_cpf(text: str) -> list:
    """
    Returns a list with brazilian unique personal ID (CPF)
    finded in a string.
    """
    regexCPF = re.compile(r"\b\d{11}\b|\b\d\d\d.\d\d\d.\d\d\d-\d\d\b")
    cpfs = set(
        ["".join([num for num in x if num.isalnum()]) for x in regexCPF.findall(text)]
    )
    valid_cpfs = []
    for cpf in cpfs:
        cpf_num = CPF()
        if cpf_num.validate(cpf):
            valid_cpfs.append(cpf)
    return unique_values(valid_cpfs)

def find_vehicles(text: str) -> list:
    """
    Returns a list of brazilian vehicles plates.
    """
    plates = re.findall(r"\b([A-Za-z]{3}[\s-]?[0-9][0-9A-Za-z][0-9]{2})\b", text)
    return unique_values([clean_doc_num(p) for p in plates])

def find_cnpj(text: str) -> list:
    """
    Returns a list with brazilian unique company ID (CNPJ)
    finded in a string.
    """
    regexCNPJ = re.compile(r"\b\d{14}\b|\b\d\d.\d\d\d.\d\d\d\/\d\d\d\d-\d\d\b")
    # regexCNPJ = re.compile(r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
    cnpjs = set(
        ["".join([num for num in x if num.isalnum()]) for x in regexCNPJ.findall(text)]
    )
    valid_cnpjs = []
    for cnpj in cnpjs:
        cnpj_num = CNPJ()
        if cnpj_num.validate(cnpj):
            valid_cnpjs.append(cnpj)
    return unique_values(valid_cnpjs)


def to_table(file_path: str):
    """
    Generate a html table from a given data file separeted by '|'.
    """
    df = pd.read_csv(
        file_path, sep="|", dtype=str, names=["doc_num", "arquivo", "local", "texto"]
    )
    file_name = f"{file_path}".replace(".txt", ".html")
    page = df.to_html()
    new_page = re.sub(
        r">(.{100,})?<", lambda pattern: pattern.group(0)[:300] + "...<", page
    )
    try:
        with open(f"{file_name}", "w") as file:
            file.write(new_page)
    except UnicodeEncodeError:
        with open(f"{file_name}", "w") as file:
            normalized_page = normaliza(page)
            file.write(normalized_page)
