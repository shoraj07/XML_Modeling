from xml.etree import ElementTree
import csv

# PARSE XML
xml = ElementTree.parse(r'D:\BI- Mark\XML Data Modeling\response.xml')

# CREATE CSV FILE
csvfile = open("data.csv", 'w', encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD THE HEADER TO CSV FILE
l1 = list()

csvfile_writer.writerow(["Id", "EpCustomQuestionId", "Question"])

# FOR EACH EMPLOYEE
for employee in xml.findall("employee"):

    if (employee):
        # EXTRACT EMPLOYEE DETAILS
        Id = employee.find(r"b:CustomQuestions\b:Id")
        EpCustomQuestionId = employee.find("b:EpCustomQuestionId")
        Question = employee.find("b:Question")
        csv_line = [Question.text, EpCustomQuestionId.text, Question.text]

        # ADD A NEW ROW TO CSV FILE
        csvfile_writer.writerow(csv_line)
csvfile.close()