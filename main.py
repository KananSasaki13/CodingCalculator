import tkinter as tk
import setanswers as sa
import calcanswers as ca


def getAnswers():
    return sa.setAnswers('Answers.xls')


def getScore(root, entries):
    xentries = []
    for row in entries:
        rowentries = []
        for col in row:
            newelement = None
            if col.get().isdigit():
                newelement = int(col.get())
            rowentries.append(newelement)
        xentries.append(rowentries)

    highscores = ca.SolveEquation(xentries, getAnswers())
    scoreslabels = []
    total = 0
    for s in highscores:
        scoreslabels.append("Score " + str(s[0] + 1) + ":   " + str(s[1]))
        total = total + s[1]
    scoreslabels.append("Total:     " + str(total))

    newWindow = tk.Toplevel(root)
    newWindow.title("Scores")
    newWindow.geometry("220x285")
    tk.Label(newWindow, text=scoreslabels[0], font=(
        'Aerial 14 bold')).grid(row=0, column=0)
    tk.Label(newWindow, text=scoreslabels[1], font=(
        'Aerial 14 bold')).grid(row=1, column=0)
    tk.Label(newWindow, text=scoreslabels[2], font=(
        'Aerial 14 bold')).grid(row=2, column=0)
    tk.Label(newWindow, text=scoreslabels[3], font=(
        'Aerial 14 bold')).grid(row=3, column=0)
    tk.Label(newWindow, text=scoreslabels[4], font=(
        'Aerial 14 bold')).grid(row=4, column=0)
    tk.Label(newWindow, text=scoreslabels[5], font=(
        'Aerial 14 bold')).grid(row=5, column=0)
    tk.Label(newWindow, text=scoreslabels[6], font=(
        'Aerial 14 bold')).grid(row=6, column=0)
    tk.Label(newWindow, text=scoreslabels[7], font=(
        'Aerial 14 bold')).grid(row=7, column=0)
    tk.Label(newWindow, text=scoreslabels[8], font=(
        'Aerial 14 bold')).grid(row=8, column=0)


def main():
    root = tk.Tk()
    root.title("Scoring Calculator")
    root.geometry('850x285')

    # Create the lable objects and pack them into the grid
    tk.Label(root, text="Attempt 1", font=(
        'Aerial 14 bold')).grid(row=0, column=0)
    tk.Label(root, text="Attempt 2", font=(
        'Aerial 14 bold')).grid(row=1, column=0)
    tk.Label(root, text="Attempt 3", font=(
        'Aerial 14 bold')).grid(row=2, column=0)
    tk.Label(root, text="Attempt 4", font=(
        'Aerial 14 bold')).grid(row=3, column=0)
    tk.Label(root, text="Attempt 5", font=(
        'Aerial 14 bold')).grid(row=4, column=0)
    tk.Label(root, text="Attempt 6", font=(
        'Aerial 14 bold')).grid(row=5, column=0)
    tk.Label(root, text="Attempt 7", font=(
        'Aerial 14 bold')).grid(row=6, column=0)
    tk.Label(root, text="Attempt 8", font=(
        'Aerial 14 bold')).grid(row=7, column=0)

    # Create the entry objects using root
    entries = []
    for x in range(8):
        entrylist = []
        for y in range(6):
            entrylist.append(tk.Entry(root))
        entries.append(entrylist)

    # Pack them using grid
    rowcount = 0
    colcount = 1
    for el in entries:
        for e in el:
            e.grid(row=rowcount, column=colcount,
                   sticky='n,e,s,w')
            if (colcount == 6):
                rowcount = rowcount + 1
                colcount = 1
            else:
                colcount = colcount + 1

    # Create Button to get scores
    tk.Label(root, text="").grid(columnspan=6, row=9, column=0)
    button1 = tk.Button(root, text='Get Your Scores', command=lambda: getScore(root, entries),
                        bg='brown', fg='white', font=('helvetica', 12, 'bold'))
    button1.grid(columnspan=7, row=10, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
