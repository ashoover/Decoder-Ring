import datetime
import random
from tkinter import *
import tkinter as tk
import os


screen_height = '200'
screen_width = '300'

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

    decode_dict['cuid'] = full_cuid
    decode_dict['fullpc'] = full_profit_center
    decode_dict['yr'] = list_year
    decode_dict['pn'] = list_uid

    return decode_dict


def encoder_ring():
    encode = "Encode!!"
    print(encode)


ran_num = random_number()
y_code = year_code()


# GUI

def main_app():
    root = Tk()

    # Encode
    ccode = decoder_ring(current_code='G3O88675')
    clientid = 'Client ID      : ' + ccode['cuid']
    pcenter = 'Profit Center  : ' + ccode['fullpc']
    year = 'Project Year   : ' + ccode['yr']
    pnum = 'Project Number : ' + ccode['pn']

    encode_button = tk.Button(root, text="Decode", command=ccode)
    root.wm_title("Decoder Ring!")
    canvas = Canvas(root, width=screen_width, height=screen_height)
    label1 = Label(root, text=clientid)
    label2 = Label(root, text=pcenter)
    label3 = Label(root, text=year)
    label4 = Label(root, text=pnum)

    encode_button.pack()
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    canvas.pack()

    # Decode

    decode_v = StringVar()
    decode_v.set('CU*BASE Operations')  # initialize radio buttons

    pf_options = OptionMenu(root, decode_v, 'Administration',
                                            'Accounting / Bookkeeping',
                                            'Conversion / Deconversion',
                                            'Disaster Recovery / Business Continuity',
                                            'EFT / Money Movement',
                                            'Forms Development',
                                            'Graphics Design',
                                            'Knowledge Development (Internal)',
                                            'Lending / Collections',
                                            'Marketing',
                                            'Network Services / IT',
                                            'CU*BASE Operations',
                                            'Custom Program Development',
                                            'Call Center (In / Out)',
                                            'Sales',
                                            'Teller / MSR',
                                            'Video Production',
                                            'Website Development',
                                            'Bugs / AnswerBook Incidents',
                                            'Client Education',
                                            'Compliance / DORbusters')
    pf_options.pack()

    def ok():
        print("value is", decode_v.get())
        root.quit()

    encode_button = Button(root, text="ENCODE!", command=ok())
    encode_button.pack()

    # Application Icon
    root.iconphoto(True, PhotoImage(file=os.path.join("assets", "green_lantern_icon.png")))
    root.mainloop()


# Temp Area
main_app()

