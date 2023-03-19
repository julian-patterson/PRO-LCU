'''
Julian Patterson 2131249
420-LCU Computer Programming, Section 5
S. Hilal, instructor
Assignment 2
'''

Names = []  # names
IDs = []    # students' IDs
Prog = []   # program codes
Tests = []  # Test grades (2 grades/student)
Labs = []   # Lab grades (3 grades/student)
Proj = []   # Project grades
Grds = []   # Total grades
LGrds = []  # letter grades

'''
Guide:
- variables starting with "tmp" are only used for validation and in one option (ex. tmp_test_scores; only used validate that test scores are integers)
'''

# Program Menu:
MENU = '''\nWelcome to the Simple Class Calculator. Here's the list of available:
    1- Enter a student record (Name, ID, Program, and 6 grades seperated by commas, no spaces).
    2- Display the full class data in a table format sorted in alphabetical order based on full name.
    3- Calculate and Display the class descriptive statistics.
    4- Display the record of a given student. 
    5- Display a list of the students whose total grade is below the average.
    6- Update an evaluation grade for one student.
    7- Exit
Select an option by entering its number or 7 to exit: '''

while True:
    selection = input(MENU)
    if selection == "1":
        while True:
            record = input("Enter Student Record: ")
            tmp_record_list = record.split(",")
            tmp_type_check = []

            if len(tmp_record_list) != 9:
                print("Record Incomplete, Record rejected.")
                tmp_type_check.append(False)
                break

            if tmp_record_list[0].isalpha() != True:
                print("The student name must be a string. Record rejected.")
                tmp_type_check.append(False)
                break

            if len(tmp_record_list[1]) != 6:
                print("ID must have 6 digits. Record rejected. ")
                tmp_type_check.append(False)
                break

            # TODO for loop
            if int(tmp_record_list[1]) == any(IDs):
                print("Duplicate ID number. Record rejected")
                tmp_type_check.append(False)
                break

            if tmp_record_list[2] != "HH" and tmp_record_list[2] != "HP" and tmp_record_list[2] != "B2":
                print("Invalid program enter. Please enter HH, HP or B2")
                tmp_type_check.append(False)
                break

            tmp_test_scores_booleans = []
            tmp_lab_scores_booleans = []
            tmp_project_scores_booleans = []

            tmp_test_list = []
            tmp_lab_list = []
            tmp_project_list = []

            tmp_test_scores_total = 0
            tmp_lab_scores_total = 0

            for test_score in tmp_record_list[3:5]:
                if test_score.isdigit() != True:
                    print("Invalid test score. Test scores must be integers. ")
                    tmp_test_scores_booleans.append(False)
                    break

                if int(test_score) > 25:
                    print("Invalid test score. Test scores must be 25 or below 25. ")
                    tmp_test_scores_booleans.append(False)
                    break

                else:
                    tmp_test_scores_booleans.append(True)
                    tmp_test_list.append(int(test_score))
                    tmp_test_scores_total += int(test_score)
                    continue

            for lab_score in tmp_record_list[5:8]:
                if lab_score.isdigit() != True:
                    print("Invalid lab score. Lab scores must be integers. ")
                    tmp_lab_scores_booleans.append(False)
                    break

                if int(lab_score) > 10:
                    print("Invalid lab score. Lab scores must be 10 or below 10. ")
                    tmp_lab_scores_booleans.append(False)
                    break

                else:
                    tmp_lab_scores_booleans.append(True)
                    tmp_lab_list.append(int(lab_score))
                    tmp_lab_scores_total += int(lab_score)
                    continue

            if tmp_record_list[-1].isdigit() != True:
                print("Invalid project score. Project scores must be integers. ")
                tmp_type_check.append(False)
                break

            if int(tmp_record_list[-1]) > 20:
                print("Invalid project score. Project scores must be 20 or below 20. ")
                tmp_type_check.append(False)
                break

            if all(tmp_test_scores_booleans) != True or all(tmp_lab_scores_booleans) != True:
                break

            # TODO overall grade is messed up
            if all(tmp_test_scores_booleans) and all(tmp_lab_scores_booleans) and not any(tmp_type_check):
                print("Record Accepted.")
                print(tmp_lab_scores_total)
                print(tmp_test_scores_total)
                print(tmp_record_list[-1])
                tmp_overall_grade = ((int(tmp_record_list[-1])*(100/20)*0.2) + (
                    tmp_lab_scores_total*(100/30)*.30) + ((tmp_test_scores_total)*0.5))

                if int(tmp_overall_grade) >= 87:
                    tmp_letter_grade = "A"

                elif 75 <= int(tmp_overall_grade) <= 86:
                    tmp_letter_grade = "B"

                elif 65 <= int(tmp_overall_grade) <= 74:
                    tmp_letter_grade = "C"

                else:
                    tmp_letter_grade = "F"

                Names.append(tmp_record_list[0])
                IDs.append(int(tmp_record_list[1]))
                Prog.append(tmp_record_list[2])
                Tests.append(tmp_test_list)
                Labs.append(tmp_lab_list)
                Proj.append(int(tmp_record_list[-1]))
                Grds.append(int(tmp_overall_grade))
                LGrds.append(tmp_letter_grade)
                print(Names)
                print(IDs)
                print(Prog)
                print(Tests)
                print(Labs)
                print(Proj)
                print(Grds)
                print(LGrds)
                break

    elif selection == "2":
        break

    elif selection == "3":
        break

    elif selection == "4":
        break

    elif selection == "5":
        break

    elif selection == "6":
        break

    elif selection == "7":
        break

    else:
        print("Please enter a valid option. Please select a number between 1 and 7")
