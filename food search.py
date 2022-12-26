
import tkinter.ttk
import tkinter.messagebox
from tkinter.ttk import *
import sqlite3
from tkinter import *

class FindFoodGUI:
    def __init__(self):
        # create main window
        self.root = tkinter.Tk()

        # set window size
        self.root.geometry('510x420+100+100')

        # display title
        self.root.title('Food Search')

        # lines
        tkinter.ttk.Separator(self.root, orient='vertical').grid(column=2, row=0, rowspan=12, sticky='nsw', padx=0)

        # labels

        # food log section
        title_label = tkinter.Label(self.root, text='Enter the following parameters: ')
        title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        min_sod_label = tkinter.Label(self.root, text='Enter Minimum Sodium (mg): ')
        min_sod_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        max_sod_label = tkinter.Label(self.root, text='Enter Maximum Sodium (mg): ')
        max_sod_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        min_carb_label = tkinter.Label(self.root, text='Enter Minimum Total Carbs (g): ')
        min_carb_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        max_carb_label = tkinter.Label(self.root, text='Enter Maximum Total Carbs (g): ')
        max_carb_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        min_fat_label = tkinter.Label(self.root, text='Enter Minimum Total Fat (g): ')
        min_fat_label.grid(column=0, row=5, sticky=tkinter.W, padx=10, pady=5)

        max_fat_label = tkinter.Label(self.root, text='Enter Maximum Total Fat (g): ')
        max_fat_label.grid(column=0, row=6, sticky=tkinter.W, padx=10, pady=5)

        min_protein_label = tkinter.Label(self.root, text='Enter Minimum Protein (g): ')
        min_protein_label.grid(column=0, row=7, sticky=tkinter.W, padx=10, pady=5)

        max_protein_label = tkinter.Label(self.root, text='Enter Maximum Protein (g): ')
        max_protein_label.grid(column=0, row=8, sticky=tkinter.W, padx=10, pady=5)

        min_cal_label = tkinter.Label(self.root, text='Enter Minimum Calories: ')
        min_cal_label.grid(column=0, row=9, sticky=tkinter.W, padx=10, pady=5)

        max_cal_label = tkinter.Label(self.root, text='Enter Maximum Calories: ')
        max_cal_label.grid(column=0, row=10, sticky=tkinter.W, padx=10, pady=5)

        # entries
        self.min_sod_entry = tkinter.Entry(self.root)
        self.min_sod_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        self.max_sod_entry = tkinter.Entry(self.root)
        self.max_sod_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        self.min_carb_entry = tkinter.Entry(self.root)
        self.min_carb_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        self.max_carb_entry = tkinter.Entry(self.root)
        self.max_carb_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        self.min_fat_entry = tkinter.Entry(self.root)
        self.min_fat_entry.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=0)

        self.max_fat_entry = tkinter.Entry(self.root)
        self.max_fat_entry.grid(column=1, row=6, sticky=tkinter.W, padx=10, pady=0)

        self.min_protein_entry = tkinter.Entry(self.root)
        self.min_protein_entry.grid(column=1, row=7, sticky=tkinter.W, padx=10, pady=0)

        self.max_protein_entry = tkinter.Entry(self.root)
        self.max_protein_entry.grid(column=1, row=8, sticky=tkinter.W, padx=10, pady=0)

        self.min_cal_entry = tkinter.Entry(self.root)
        self.min_cal_entry.grid(column=1, row=9, sticky=tkinter.W, padx=10, pady=0)

        self.max_cal_entry = tkinter.Entry(self.root)
        self.max_cal_entry.grid(column=1, row=10, sticky=tkinter.W, padx=10, pady=0)

        # create buttons
        search_button = tkinter.Button(text='Search', command=self.search_food)
        search_button.grid(column=1, row=11, sticky=tkinter.W, padx=10, pady=10)

        cancel_button = tkinter.Button(text='Cancel', command=self.root.destroy)
        cancel_button.grid(column=0, row=11, sticky=tkinter.E, padx=10, pady=10)

        quit_button = tkinter.Button(text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=11, padx=20, pady=10)

        # enter main loop
        tkinter.mainloop()

    def search_food(self):
        conn = None
        # connect to the database
        conn = sqlite3.connect('sodium.db')

        # get a database cursor
        cur = conn.cursor()

        # print(len(self.min_sod_entry.get()))

        # set placeholder values if entries are empty
        if len(self.min_sod_entry.get()) == 0:
            min_sod = -1
        else:
            min_sod = self.min_sod_entry.get()
        if len(self.max_sod_entry.get()) == 0:
            max_sod = 9999999
        else:
            max_sod = self.max_sod_entry.get()

        if len(self.min_carb_entry.get()) == 0:
            min_carb = -1
        else:
            min_carb = self.min_carb_entry.get()
        if len(self.max_carb_entry.get()) == 0:
            max_carb = 9999999
        else:
            max_carb = self.max_carb_entry.get()

        if len(self.min_fat_entry.get()) == 0:
            min_fat = -1
        else:
            min_fat = self.min_fat_entry.get()
        if len(self.max_fat_entry.get()) == 0:
            max_fat = 9999999
        else:
            max_fat = self.max_fat_entry.get()

        if len(self.min_cal_entry.get()) == 0:
            min_cal = -1
        else:
            min_cal = self.min_cal_entry.get()
        if len(self.max_cal_entry.get()) == 0:
            max_cal = 9999999
        else:
            max_cal = self.max_cal_entry.get()

        if len(self.min_protein_entry.get()) == 0:
            min_protein = -1
        else:
            min_protein = self.min_protein_entry.get()
        if len(self.max_protein_entry.get()) == 0:
            max_protein = 9999999
        else:
            max_protein = self.max_protein_entry.get()

        print(min_sod, max_sod, min_carb, max_carb, min_fat, max_fat, min_cal, max_cal, min_protein,
              max_protein)

        # get food items that fit parameters
        cur.execute("SELECT food_name, sodium_amt, carb_amt, fat_amt, calorie_amt, protein_amt FROM Food WHERE "
                    "((sodium_amt BETWEEN (?) and (?2)) OR (sodium_amt IS NULL OR sodium_amt = '')) AND "
                    "((carb_amt BETWEEN (?3) and (?4)) OR (carb_amt IS NULL OR carb_amt = '')) AND "
                    "((fat_amt BETWEEN (?5) and (?6)) OR (fat_amt IS NULL OR fat_amt = '')) AND "
                    "((calorie_amt BETWEEN (?7) and (?8)) OR (calorie_amt IS NULL OR calorie_amt = '')) AND "
                    "((protein_amt BETWEEN (?9) and (?10)) OR (protein_amt IS NULL OR protein_amt = ''))",
                    (min_sod, max_sod, min_carb, max_carb, min_fat, max_fat,
                     min_cal, max_cal, min_protein, max_protein))

        # store selection
        results = cur.fetchall()
        print(results)

        # create new list to transfer data into and display
        results_list = []

        # create new list with names instead of id's
        for row in results:
            # make tuple a list
            row_list = list(row)

            # alter string appearance to be understandable to user
            row_list[1] = 'Sodium: ' + str(row[1]) + ' mg'
            row_list[2] = 'Total Carbs: ' + str(row[2]) + ' g'
            row_list[3] = 'Total Fat: ' + str(row[3]) + ' g'
            row_list[4] = 'Calories: ' + str(row[4])
            row_list[5] = 'Protein: ' + str(row[5]) + ' g'

            # adds adjusted list to previously empty list that will be displayed
            results_list.append(row_list)

        # create window that will show data
        results_window = tkinter.Toplevel(self.root)
        results_window.title("Food Search Results")

        # nested for loop that grids data from day_log_list list
        for x in range(len(results_list)):
            for y in range(len(results_list[0])):
                w = Text(results_window, width=20, height=3)
                w.grid(row=x, column=y)
                w.insert(END, results_list[x][y])

        # commit changes
        conn.commit()


if __name__ == '__main__':
    test = FindFoodGUI()
