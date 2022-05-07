import xlrd


def setAnswers(filelocation):
    book = xlrd.open_workbook(filelocation)
    print("The number of worksheets is {0}".format(book.nsheets))
    print("Worksheet name(s): {0}".format(book.sheet_names()))
    sh = book.sheet_by_index(0)

    answers = []

    for x in range(sh.nrows):
        answerrow = []
        for y in range(sh.ncols):
            answerrow.append(int(sh.cell_value(x, y)))
        answers.append(answerrow)

    print(answers)

    return answers
