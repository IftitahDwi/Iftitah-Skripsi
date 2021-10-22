import re
import string

def case_folding(titles=[]):
    title_cases=[]
    for title in titles:
        title_cases.append(re.sub(r'[^\w\s]', '', re.sub(r"\d+", "", title.lower()).strip()))
    return title_cases