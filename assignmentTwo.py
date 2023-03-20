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
data = []   # Overall Data

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

            # TODO ask - assign another variable and replacing the space and then check
            tmp_name = tmp_record_list[0].replace(" ", "")
            if tmp_name.isalpha() != True:
                print("The student name must be a string. Record rejected.")
                tmp_type_check.append(False)
                break

            if len(tmp_record_list[1]) != 6:
                print("ID must have 6 digits. Record rejected. ")
                tmp_type_check.append(False)
                break

            for id in IDs:
                if int(id) == int(tmp_record_list[1]):
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

            if not all(tmp_type_check):
                break

            if all(tmp_test_scores_booleans) and all(tmp_lab_scores_booleans) and all(tmp_type_check):
                print("Record Accepted.")

                tmp_overall_grade = (((int(tmp_record_list[-1])/20*0.2) + (
                    tmp_lab_scores_total/30*.30) + (tmp_test_scores_total/50*0.5))*100)

                if int(tmp_overall_grade) >= 87:
                    tmp_letter_grade = "A"

                elif 75 <= int(tmp_overall_grade) <= 86:
                    tmp_letter_grade = "B"

                elif 65 <= int(tmp_overall_grade) <= 74:
                    tmp_letter_grade = "C"

                else:
                    tmp_letter_grade = "F"

                tmp_data = [tmp_record_list[0], int(tmp_record_list[1]), tmp_record_list[2], str(tmp_test_list), str(tmp_lab_list), int(
                    tmp_record_list[-1]), int(tmp_overall_grade), tmp_letter_grade]
                data.append(tmp_data)
                Names.append(tmp_record_list[0])
                IDs.append(int(tmp_record_list[1]))
                Prog.append(tmp_record_list[2])
                Tests.append(tmp_test_list)
                Labs.append(tmp_lab_list)
                Proj.append(int(tmp_record_list[-1]))
                Grds.append(int(tmp_overall_grade))
                LGrds.append(tmp_letter_grade)
                break

    elif selection == "2":
        data.sort()
        x = "{:12s} {:6d} {:3s} {:8s} {:12s} {:3d} {:3d} {:1s}"
        for i in data:
            print(x.format(i[0], i[1], i[2], i[3],
                  i[4], i[5], i[6], i[7]))

    elif selection == "3":
        tmp_total_Grds = 0
        print("Number of students entered: " + str(len(Names)))

        for i in Grds:
            tmp_total_Grds += i
        print("Class average based on total grade: " +
              str((tmp_total_Grds)/len(Names)))

        # TODO Mode
        A = LGrds.count("A")
        B = LGrds.count("B")
        C = LGrds.count("C")
        F = LGrds.count("F")

        print("Class Mode(s) based on letter grade: " + str())

        T1 = []
        T2 = []
        T1_total = 0
        T2_total = 0
        L1_total = 0
        L2_total = 0
        L3_total = 0
        Proj_total = 0
        for i in Tests:
            T1_total += i[0]
            T1.append(i[0])
            T2_total += i[1]
            T2.append(i[1])

        for i in Labs:
            L1_total += i[0]
            L2_total += i[1]
            L3_total += i[2]

        for i in Proj:
            Proj_total += i

        print("Evaluation Averages: T1: " + str(float((T1_total/len(Names))*100/25)) + " T2: " + str(float((T2_total/len(Names))*100/25)) + " L1: " + str(float((L1_total/len(Names))*100/10)
                                                                                                                                                          ) + " L2: " + str(float((L2_total/len(Names))*100/10)) + " L3: " + str(float((L3_total/len(Names))*100/10)) + " Proj: " + str(float((Proj_total/len(Names))*100/20)))

        print("Letter Grade distribution: A: " + str(A) +
              " B: " + str(B) + " C: " + str(C) + " F: " + str(F))

        print("Highest Grade for T1: " + str(max(T1)*100/25) + " Lowest Grade for T1: " + str(min(T1)*100/25) +
              " Highest Grade for T2: " + str(max(T2)*100/25) + " Lowest Grade for T2: " + str(min(T2)*100/25))

    elif selection == "4":
        id_input = input("Enter the student's ID: ")
        for record in data:
            if record[1] == int(id_input):
                print("Name: " + str(record[0]) + "    ID: " + str(record[1]))
                print("Test Grades: " + str(record[3]).strip(" []") + " Lab Grades: " + str(
                    record[4]).strip(" []") + " Project Grade: " + str(record[5]))
                print("Total Grade: " +
                      str(record[6]) + "     Letter Grade: " + str(record[7]))

    elif selection == "5":
        break

    elif selection == "6":
        id_input = input("Enter the student's ID: ")
        grade_input = input("Which grade to update: ")
        for record in data:
            if record[1] == int(id_input):
                for i in record[3]:
                    test_list_stripped = str(i).strip(" []")
                    test_list = test_list_stripped.split(",")
                    T1_grade = test_list[0]
                    T2_grade = test_list[1]
                for i in record[4]:
                    lab_list_stripped = str(i).strip(" []")
                    lab_list = lab_list_stripped.split(",")
                    L1_grade = i[0]
                    L2_grade = i[1]
                    L3_grade = i[2]
                proj_grade = record[5]
                if grade_input == "T1":
                    print("The current T1 grade is " + str(T1_grade))
                    update = input("Enter the new T1 grade: ")
                    str(record[3]).replace(T1_grade, update)

                elif grade_input == "T2":
                    print("The current T2 grade is " + str(T2_grade))
                    update = input("Enter the new T2 grade: ")
                    str(record[3]).replace(T2_grade, update)

                elif grade_input == "L1":
                    print("The current L1 grade is " + str(L1_grade))
                    update = input("Enter the new L1 grade: ")
                    str(record[3]).replace(L1_grade, update)

                elif grade_input == "L2":
                    print("The current L2 grade is " + str(L2_grade))
                    update = input("Enter the new L2 grade: ")
                    str(record[3]).replace(L2_grade, update)

                elif grade_input == "L3":
                    print("The current L3 grade is " + str(L3_grade))
                    update = input("Enter the new L3 grade: ")
                    str(record[3]).replace(L3_grade, update)

                else:
                    print("The current PR grade is " + str(proj_grade))
                    update = input("Enter the new PR grade: ")
                    str(record[3]).replace(proj_grade, update)

    elif selection == "7":
        break

    else:
        print("Please enter a valid option. Please select a number between 1 and 7")
