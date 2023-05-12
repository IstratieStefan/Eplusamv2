for i in range(28):
    file = open(f"D:\\School\\Teme\\9-12\\Info\\eplusam69\\Eplusamv2\\Eplusam\\data\\battle_{i+1}.json", 'w')
    file.write("""{
    "arena":"plains colosseum",
    "positions":[
        "-",
        "-",
        "-",
        "-",
        "-",
        "-"
    ],
    "wage":"""+str(10+5*i)+""",
    "number":"""+str(i+1)+"""
}""")