def find(str1, str2):
    try:
        char = [
            "-",
            "?",
            "(",
            ")",
            ">",
            "<",
            ".",
            ",",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "=",
            "+",
            "_",
            "]",
            "[",
            "{",
            "}",
            "|",
            "'",
            "/",
        ]
        for i in char:
            str1 = str1.replace(i," ")
        findall1 = str1.split()
    except:
        "i wana 2 string"
    else:
        if str2 in findall1:
            return True
        else:
            return(False)