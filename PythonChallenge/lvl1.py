"""
Author: Moritz van Eimern
Date: 8/7/25
"""
import string

if __name__ == "__main__":
    pass

raw = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

shift = 2
alphabet = string.ascii_lowercase

table = str.maketrans(alphabet,
                      alphabet[shift:] + alphabet[:shift])

def shift2(text: str) -> str:
    return text.translate(table)

print(shift2(raw))

print(shift2("map"))

sol = "ocr"
