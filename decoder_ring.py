import datetime
import random
from tkinter import *
import tkinter as tk


screen_height = '600'
screen_width = '800'

profit_centers = {
    'A': 'Administration',
    'B': 'Accounting / Bookkeeping',
    'C': 'Conversion / Deconversion',
    'D': 'Disaster Recovery / Business Continuity',
    'E': 'EFT / Money Movement',
    'F': 'Forms Development',
    'G': 'Graphics Design',
    'K': 'Knowledge Development (Internal)',
    'L': 'Lending / Collections',
    'M': 'Marketing',
    'N': 'Network Services / IT',
    'O': 'CU*BASE Operations',
    'P': 'Custom Program Development',
    'Q': 'Call Center (In / Out)',
    'S': 'Sales',
    'T': 'Teller / MSR',
    'V': 'Video Production',
    'W': 'Website Development',
    'X': 'Bugs / AnswerBook Incidents',
    'Y': 'Client Education',
    'Z': 'Compliance / DORbusters'
    }

cuid = {
    'G3':'General Projects',
    'S4':'Site4'
}


def random_number():
    return random.randrange(1000, 9999)


def year_code():
    now = datetime.datetime.now()
    c_year = str(now.year)
    c_year_split = list(c_year)
    return c_year_split[3]


pc_list = profit_centers


def decoder_ring(current_code):
    decode_dict = {}
    code_list = list(current_code)

    list_profit_center = code_list[2]
    full_profit_center = profit_centers[list_profit_center]
    list_cuid = "".join(code_list[0:2])
    full_cuid = cuid[list_cuid]
    list_year = "201" + (code_list[3])
    list_uid = "".join(code_list[4:])

    dash = '\n' + '----------------------------------' + '\n'

    print(dash)
    print('Current Code   : {}'.format(current_code))
    print('CUID of client : {}'.format(full_cuid))
    print('Profit Center  : {}'.format(full_profit_center))
    print('Project Year   : {}'.format(list_year))
    print('Project Number : {}'.format(list_uid))
    print(dash)

    decode_dict['cuid'] = full_cuid
    decode_dict['fullpc'] = full_profit_center
    decode_dict['yr'] = list_year
    decode_dict['pn'] = list_uid

    print(decode_dict)
    return decode_dict


ran_num = random_number()
y_code = year_code()


# GUI Setups

def main_app():
    root = Tk()

    ccode = decoder_ring(current_code='G3O88675')
    clientid = 'Client ID      : ' + ccode['cuid']
    pcenter = 'Profit Center  : ' + ccode['fullpc']
    year = 'Project Year   : ' + ccode['yr']
    pnum = 'Project Number : ' + ccode['pn']

    time_button = tk.Button(root, text="Decode", command=ccode)
    canvas = Canvas(root, width=screen_width, height=screen_height)
    label1 = Label(root, text=clientid)
    label2 = Label(root, text=pcenter)
    label3 = Label(root, text=year)
    label4 = Label(root, text=pnum)

    time_button.pack()
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    canvas.pack()

    root.mainloop()


# Temp Area
decoder_ring('G3O88675')
main_app()

