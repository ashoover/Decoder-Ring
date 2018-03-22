import datetime
import random

print("Welcome to the Decoder Ring")

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


def decoder_ring(current_code):
    code_list = list(current_code)
    dc_profit_center = str(code_list[0:2])

    list_cuid = str(code_list[0,1])

    print('CUID of client CD: {}'.format{})
    print('Profit Center : {}'.format(dc_profit_center))
    print(''.format{})


ran_num = random_number()
y_code = year_code()
