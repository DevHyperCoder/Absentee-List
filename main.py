from os import write
import pandas as pd
import sys
import xlsxwriter

def get_class():
    try:
       return sys.argv[1]
    except IndexError:
        return input("Class Name:")

def convert_excel_to_list(filename,column):
    excel_file = pd.read_excel(filename)
    return  excel_file[column].tolist()

def main():
    print("Enter class name or 'help'")
    
    CLASS = get_class()

    if CLASS == 'help':
        print_help()
        return

    print(f'Reading {CLASS}_Master.xlsx')
    master_list = convert_excel_to_list(f'{CLASS}_Master.xlsx','a')
    master_list = format_list(master_list)
    print(f'Master List: {master_list}')

    print(f'Reading {CLASS}.xlsx')
    todays_list = convert_excel_to_list(f'{CLASS}.xlsx','a')
    todays_list = format_list(todays_list)
    print(f"Today's list : {todays_list}")

    absent_list = []

    print(f'Calculating absentees of {CLASS}')

    for s in master_list:
        if s not in todays_list:
            absent_list.append(s)

    print(f'Absent List: {absent_list}')
    print(f'Writing to {CLASS}_ABSENT.xlsx')
    write_excel_file(CLASS,absent_list)

def write_excel_file(class_name,list):
    with xlsxwriter.Workbook(f'{class_name}_ABSENT.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        for row_num,data in enumerate(list):
            worksheet.write_row(row_num, 0,data)

def print_help():
    helpString = """
    Master List of students should be named like this => <CLASS-NAME>_Master.xlsx
    The current present list should be named like this => <CLASS-NAME>.xlsx
    Once you run it, a new file named <CLASS-NAME>_ABSENT.xlsx would be made!

    Any errors?? Contact me!
    """
    print(helpString)

def format_list(list):
    for i in range(0,len(list)):
        e = list[i]
        e =e.upper()
        e=e.strip()
        list[i] =e
    return list

if __name__ == "__main__":
    main()