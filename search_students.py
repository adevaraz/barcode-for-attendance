import constants
import pandas as pd

'''
Function to search class ID based on Student ID
    Parameter : Student ID
    Return : Class ID
'''

def search_student(student_id) :
    # Read data from student data excel and get its sheets name
    data_frame = pd.read_excel(constants.DATA_MHS_LOC , sheet_name=None)
    
    # Generate class ID from student ID
    # Ex :181511023 is in class 181501 or 181502
    angkatan = student_id[0:2]
    prodi = student_id[4:6]
    class_id = angkatan+prodi

    # Loop over sheets name and search the student
    for sheet_name in data_frame.keys() :
         # check if class id that generated from student id is substring from sheet name (class id)
         if class_id in sheet_name :
             # make list of student id from some class
             studentID_array = map(str, list(set(data_frame[sheet_name]["NIM"])))

             if  student_id in studentID_array:
                 # student_id is exist in this sheet (class_id)
                 # return class id
                 return sheet_name
    
    return "000000"

# print(search_student('181524007'))