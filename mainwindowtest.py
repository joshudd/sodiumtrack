
import tkinter.ttk
import tkinter.messagebox
# from tkinter.ttk import *
import sqlite3
from tkinter import *


class TestGUI:
    # main window
    def __init__(self):
        # create main window and other windows
        self.root = tkinter.Tk()

        # set window size
        self.root.geometry('520x380+100+100')

        # display title
        self.root.title('Main Test Window')

        # lines
        tkinter.ttk.Separator(self.root, orient='vertical').grid(column=2, row=0, rowspan=10, sticky='nsw', padx=0)
        tkinter.ttk.Separator(self.root, orient='horizontal').grid(column=0, row=6, columnspan=2, sticky='ews', padx=0)
        tkinter.ttk.Separator(self.root, orient='horizontal').grid(column=2, row=3, columnspan=1, sticky='ew', padx=0)

        # labels

        # food log section
        fl_title_label = tkinter.Label(self.root, text='Add Food Log: ')
        fl_title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        fl_fname_label = tkinter.Label(self.root, text='Enter First Name: ')
        fl_fname_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        fl_lname_label = tkinter.Label(self.root, text='Enter Last Name: ')
        fl_lname_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        fl_food_label = tkinter.Label(self.root, text='Enter Food Name: ')
        fl_food_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        fl_servingnum_label = tkinter.Label(self.root, text='Enter # of Servings: ')
        fl_servingnum_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        fl_date_label = tkinter.Label(self.root, text='Enter Date (mm,dd,yyyy): ')
        fl_date_label.grid(column=0, row=5, sticky=tkinter.W, padx=10, pady=5)

        # search food log section
        sl_title_label = tkinter.Label(self.root, text='Search Food Log:')
        sl_title_label.grid(column=0, row=7, sticky=tkinter.W, padx=5, pady=10)

        sl_date_label = tkinter.Label(self.root, text='Enter Date (mm,dd,yyyy): ')
        sl_date_label.grid(column=0, row=8, sticky=tkinter.W, padx=10, pady=5)

        # entries
        self.fl_fname_entry = tkinter.Entry(self.root)
        self.fl_fname_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        self.fl_lname_entry = tkinter.Entry(self.root)
        self.fl_lname_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        self.fl_food_entry = tkinter.Entry(self.root)
        self.fl_food_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        self.fl_servingnum_entry = tkinter.Entry(self.root)
        self.fl_servingnum_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        self.fl_date_entry = tkinter.Entry(self.root)
        self.fl_date_entry.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=0)

        self.sl_date_entry = tkinter.Entry(self.root)
        self.sl_date_entry.grid(column=1, row=8, sticky=tkinter.W, padx=10, pady=0)

        # create buttons
        add_log_button = tkinter.Button(text='Add Food Log', command=self.add_log)
        add_log_button.grid(column=1, row=6, sticky=tkinter.E, padx=10, pady=10)

        search_button = tkinter.Button(text='Search', command=self.search_log)
        search_button.grid(column=1, row=9, sticky=tkinter.E, padx=10, pady=10)

        quit_button = tkinter.Button(text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=9, padx=20, pady=10)

        # window opening buttons
        w_create_food_button = tkinter.Button(text='Create Food', command=self.create_food)
        w_create_food_button.grid(column=2, row=0, sticky=tkinter.E, padx=20, pady=0)

        w_create_user_button = tkinter.Button(text='Create User', command=self.create_user)
        w_create_user_button.grid(column=2, row=1, sticky=tkinter.E, padx=20, pady=0)

        w_find_food_button = tkinter.Button(text='Find Food', command=self.find_food)
        w_find_food_button.grid(column=2, row=2, sticky=tkinter.E, padx=20, pady=0)

        # enter main loop
        tkinter.mainloop()

    # adds log to History table in sodium database based on entries in main window
    def add_log(self):
        try:
            conn = None
            # connect to the database
            conn = sqlite3.connect('sodium.db')

            # get a database cursor
            cur = conn.cursor()

            cur.execute('SELECT food_id FROM Food WHERE food_name = (?)', (self.fl_food_entry.get(),))
            food_num = cur.fetchall()
            for row in food_num:
                food_num = row

            # print(food_num)

            # gets user id based on inputted
            cur.execute('SELECT user_id FROM User WHERE first_name = (?)', (self.fl_fname_entry.get(),))
            name_num = cur.fetchall()
            for row in name_num:
                name_num = row

            # tests if name_num and food_num lists have a value meaning the first name entries inputted had
            # corresponding id's
            # if they do, enters them into History table and tells the user
            if len(food_num) == 0:
                tkinter.messagebox.showinfo('ERROR', 'The food name entered did not match an existing Food. '
                                                     'Please enter an existing food or create a new one.')
            elif len(name_num) == 0:
                tkinter.messagebox.showinfo('ERROR', 'The first name entered did not match an existing User. '
                                                     'Please enter an existing user or create a new one.')
            else:
                # convert name_num and food_num to ints
                food_num_int = food_num[0]
                print(food_num_int)
                name_num_int = name_num[0]

                # creates new entry
                cur.execute('''INSERT INTO History (food_id, day, quantity, user_id) VALUES (?, ?, ?, ?)''',
                            (food_num_int, self.fl_date_entry.get(),
                             self.fl_servingnum_entry.get(), name_num_int))
                tkinter.messagebox.showinfo('Success!', 'The food item has been added.')

            # commit changes
            conn.commit()

        # error with database
        except sqlite3.OperationalError:
            tkinter.messagebox.showinfo('ERROR', 'Error. Please try again.')

        # general exception
        except:
            tkinter.messagebox.showinfo('ERROR', 'An Error Occurred.')

    # adds log to History table in sodium database based on entries in main window
    def search_log(self):
        # try:
        conn = None
        # connect to the database
        conn = sqlite3.connect('sodium.db')

        # get a database cursor
        cur = conn.cursor()
        cur_food = conn.cursor()
        cur_name = conn.cursor()
        print(self.sl_date_entry.get())
        cur.execute('SELECT user_id, food_id, quantity, day FROM History WHERE day = (?)', (self.sl_date_entry.get(),))
        day_log = cur.fetchall()

        # create new list to transfer data into and display
        day_log_list = []

        # create new list with names instead of id's
        for row in day_log:
            # make tuple a list
            row_list = list(row)

            # get food name based on id
            cur_food.execute('SELECT food_name FROM Food WHERE food_id = (?)', (row[1],))
            cur_name.execute('SELECT first_name, last_name FROM User WHERE user_id = (?)', (row[0],))

            food_names = cur_food.fetchall()
            name_names = cur_name.fetchall()

            row_list[0] = name_names[0][0] + ' ' + name_names[0][1]
            row_list[1] = food_names[0][0]
            row_list[2] = 'Servings: ' + str(row_list[2])
            day_log_list.append(row_list)

        x_len = len(day_log_list)
        y_len = len(day_log_list[0])
        table_window = tkinter.Toplevel(self.root)

        for x in range(x_len):
            for y in range(y_len):
                w = Text(table_window, width=20, height=3)
                w.grid(row=x, column=y)
                w.insert(END, day_log_list[x][y])

        # table_window.state("zoomed")
        table_window.mainloop()

        # commit changes
        conn.commit()

        # error with database
        # except sqlite3.OperationalError:
        #     tkinter.messagebox.showinfo('ERROR', 'Error. Please try again.')

        # general exception
        # except:
        #     tkinter.messagebox.showinfo('ERROR', 'An Error Occurred.')

    # create food window
    def create_food(self):
        # new window toplevel object
        self.food_window = tkinter.Toplevel(self.root)

        # title of window
        self.food_window.title("Create Food")

        # geometry of new window
        self.food_window.geometry("500x290+150+150")

        # lines
        tkinter.ttk.Separator(self.food_window, orient='vertical').grid(column=2, row=0, rowspan=10, sticky='nsw', padx=0)

        # labels
        title_label = tkinter.Label(self.food_window, text='Enter the following information: ')
        title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        food_name_label = tkinter.Label(self.food_window, text='Enter Food Name: ')
        food_name_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        sodium_label = tkinter.Label(self.food_window, text='Enter Sodium Amount (mg): ')
        sodium_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        carb_label = tkinter.Label(self.food_window, text='Enter Total Carb Amount (g): ')
        carb_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        fat_label = tkinter.Label(self.food_window, text='Enter Total Fat Amount (g): ')
        fat_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        protein_label = tkinter.Label(self.food_window, text='Enter Protein Amount (g): ')
        protein_label.grid(column=0, row=5, sticky=tkinter.W, padx=10, pady=5)

        calorie_label = tkinter.Label(self.food_window, text='Enter Caloric Amount: ')
        calorie_label.grid(column=0, row=6, sticky=tkinter.W, padx=10, pady=5)

        # entries
        self.food_name_entry = tkinter.Entry(self.food_window)
        self.food_name_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        self.sodium_entry = tkinter.Entry(self.food_window)
        self.sodium_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        self.carb_entry = tkinter.Entry(self.food_window)
        self.carb_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        self.fat_entry = tkinter.Entry(self.food_window)
        self.fat_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        self.protein_entry = tkinter.Entry(self.food_window)
        self.protein_entry.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=0)

        self.calorie_entry = tkinter.Entry(self.food_window)
        self.calorie_entry.grid(column=1, row=6, sticky=tkinter.W, padx=10, pady=0)

        # buttons
        create_button = tkinter.Button(self.food_window, text='Create Food', command=self.add_food)
        create_button.grid(column=1, row=7, sticky=tkinter.W, padx=10, pady=10)

        cancel_button = tkinter.Button(self.food_window, text='Cancel', command=self.food_window.destroy)
        cancel_button.grid(column=0, row=7, sticky=tkinter.E, padx=10, pady=10)

        quit_button = tkinter.Button(self.food_window, text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=7, padx=20, pady=10)

    # adds food to Food table in sodium database based on entries in create food window
    def add_food(self):
        try:
            conn = None
            # connect to the database
            conn = sqlite3.connect('sodium.db')

            # get a database cursor
            cur = conn.cursor()

            # creates new entry
            cur.execute('''INSERT INTO Food (food_name, sodium_amt, carb_amt, fat_amt, calorie_amt, protein_amt)
                                VALUES (?, ?, ?, ?, ?, ?)''', (self.food_name_entry.get(), self.sodium_entry.get(),
                                                               self.carb_entry.get(), self.fat_entry.get(),
                                                               self.calorie_entry.get(), self.protein_entry.get()))
            # commit changes
            conn.commit()
            tkinter.messagebox.showinfo('Success!', 'The food item has been added.')

        except sqlite3.IntegrityError:
            tkinter.messagebox.showinfo('ERROR', 'Error. That food name has been used, please use a unique one.')

        except sqlite3.OperationalError:
            tkinter.messagebox.showinfo('ERROR', 'Error. Please try again.')

        # general exception
        except:
            tkinter.messagebox.showinfo('ERROR', 'An Error Occurred.')

        # closes user window if no exceptions occur and user is added
        else:
            self.food_window.destroy()

    # create user window
    def create_user(self):
        # new window toplevel object
        self.user_window = tkinter.Toplevel(self.root)

        # set window title
        self.user_window.title("Create User")

        # set window sizing geometry
        self.user_window.geometry("500x220+150+150")

        # line
        tkinter.ttk.Separator(self.user_window, orient='vertical').grid(column=2, row=0, rowspan=10, sticky='nsw', padx=0)

        # labels
        title_label = tkinter.Label(self.user_window, text='Enter the following information: ')
        title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        first_name_label = tkinter.Label(self.user_window, text='Enter First Name: ')
        first_name_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        last_name_label = tkinter.Label(self.user_window, text='Enter Last Name: ')
        last_name_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        age_label = tkinter.Label(self.user_window, text='Enter Age (yrs): ')
        age_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        weight_label = tkinter.Label(self.user_window, text='Enter Weight (lbs): ')
        weight_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        # entries
        self.first_name_entry = tkinter.Entry(self.user_window)
        self.first_name_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        self.last_name_entry = tkinter.Entry(self.user_window)
        self.last_name_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        self.age_entry = tkinter.Entry(self.user_window)
        self.age_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        self.weight_entry = tkinter.Entry(self.user_window)
        self.weight_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        # create buttons
        create_user_button = tkinter.Button(self.user_window, text='Create', command=self.add_user)
        create_user_button.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=10)

        cancel_button = tkinter.Button(self.user_window, text='Cancel', command=self.user_window.destroy)
        cancel_button.grid(column=0, row=5, sticky=tkinter.E, padx=10, pady=10)

        quit_button = tkinter.Button(self.user_window, text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=5, padx=20, pady=10)

    # adds user to User table in sodium.db based on entries in create user window
    def add_user(self):
        try:
            conn = None
            # connect to the database
            conn = sqlite3.connect('sodium.db')

            # get a database cursor
            cur = conn.cursor()

            # creates new entry
            cur.execute('''INSERT INTO User (first_name, last_name, age, weight)
                                VALUES (?, ?, ?, ?)''', (self.first_name_entry.get(), self.last_name_entry.get(),
                                                         self.age_entry.get(), self.weight_entry.get()))
            # commit changes
            conn.commit()
            tkinter.messagebox.showinfo('Success!', 'The user has been added.')

        # error handle for used name
        except sqlite3.IntegrityError:
            tkinter.messagebox.showinfo('ERROR', 'Error. That first name has been used, please use a unique one.')

        # error handle for locked database
        except sqlite3.OperationalError:
            tkinter.messagebox.showinfo('ERROR', 'Error. Please try again.')

        # general exception
        except:
            tkinter.messagebox.showinfo('ERROR', 'An Error Occurred.')

        # closes user window if no exceptions occur and user is added
        else:
            self.user_window.destroy()

    # food search window
    def find_food(self):
        # new window toplevel object
        search_window = tkinter.Toplevel(self.root)

        # title of window
        search_window.title("Food Search")

        # set window sizing
        search_window.geometry("510x420+150+150")

        # line
        tkinter.ttk.Separator(search_window, orient='vertical').grid(column=2, row=0, rowspan=12, sticky='nsw', padx=0)

        # labels
        title_label = tkinter.Label(search_window, text='Enter the following parameters: ')
        title_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

        min_sod_label = tkinter.Label(search_window, text='Enter Minimum Sodium (mg): ')
        min_sod_label.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady=5)

        max_sod_label = tkinter.Label(search_window, text='Enter Maximum Sodium(mg): ')
        max_sod_label.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=5)

        min_carb_label = tkinter.Label(search_window, text='Enter Minimum Total Carbs (g): ')
        min_carb_label.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady=5)

        max_carb_label = tkinter.Label(search_window, text='Enter Maximum Total Carbs (g): ')
        max_carb_label.grid(column=0, row=4, sticky=tkinter.W, padx=10, pady=5)

        min_fat_label = tkinter.Label(search_window, text='Enter Minimum Total Fat (g): ')
        min_fat_label.grid(column=0, row=5, sticky=tkinter.W, padx=10, pady=5)

        max_fat_label = tkinter.Label(search_window, text='Enter Maximum Total Fat (g): ')
        max_fat_label.grid(column=0, row=6, sticky=tkinter.W, padx=10, pady=5)

        min_protein_label = tkinter.Label(search_window, text='Enter Minimum Protein (g): ')
        min_protein_label.grid(column=0, row=7, sticky=tkinter.W, padx=10, pady=5)

        max_protein_label = tkinter.Label(search_window, text='Enter Maximum Protein (g): ')
        max_protein_label.grid(column=0, row=8, sticky=tkinter.W, padx=10, pady=5)

        min_cal_label = tkinter.Label(search_window, text='Enter Minimum Calories: ')
        min_cal_label.grid(column=0, row=9, sticky=tkinter.W, padx=10, pady=5)

        max_cal_label = tkinter.Label(search_window, text='Enter Maximum Calories: ')
        max_cal_label.grid(column=0, row=10, sticky=tkinter.W, padx=10, pady=5)

        # entries
        min_sod_entry = tkinter.Entry(search_window)
        min_sod_entry.grid(column=1, row=1, sticky=tkinter.W, padx=10, pady=0)

        max_sod_entry = tkinter.Entry(search_window)
        max_sod_entry.grid(column=1, row=2, sticky=tkinter.W, padx=10, pady=0)

        min_carb_entry = tkinter.Entry(search_window)
        min_carb_entry.grid(column=1, row=3, sticky=tkinter.W, padx=10, pady=0)

        max_carb_entry = tkinter.Entry(search_window)
        max_carb_entry.grid(column=1, row=4, sticky=tkinter.W, padx=10, pady=0)

        min_sod_entry = tkinter.Entry(search_window)
        min_sod_entry.grid(column=1, row=5, sticky=tkinter.W, padx=10, pady=0)

        max_sod_entry = tkinter.Entry(search_window)
        max_sod_entry.grid(column=1, row=6, sticky=tkinter.W, padx=10, pady=0)

        min_carb_entry = tkinter.Entry(search_window)
        min_carb_entry.grid(column=1, row=7, sticky=tkinter.W, padx=10, pady=0)

        max_carb_entry = tkinter.Entry(search_window)
        max_carb_entry.grid(column=1, row=8, sticky=tkinter.W, padx=10, pady=0)

        min_carb_entry = tkinter.Entry(search_window)
        min_carb_entry.grid(column=1, row=9, sticky=tkinter.W, padx=10, pady=0)

        max_carb_entry = tkinter.Entry(search_window)
        max_carb_entry.grid(column=1, row=10, sticky=tkinter.W, padx=10, pady=0)

        # create buttons
        search_button = tkinter.Button(search_window, text='Search')
        search_button.grid(column=1, row=11, sticky=tkinter.W, padx=10, pady=10)

        cancel_button = tkinter.Button(search_window, text='Cancel', command=search_window.destroy)
        cancel_button.grid(column=0, row=11, sticky=tkinter.E, padx=10, pady=10)

        quit_button = tkinter.Button(search_window, text='Quit', command=self.root.destroy)
        quit_button.grid(column=2, row=11, padx=20, pady=10)


if __name__ == '__main__':
    test = TestGUI()
