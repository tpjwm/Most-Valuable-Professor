# Import 
import mysql.connector as connector
import pandas as pd
import urllib.request
import io
import requests
from tqdm import tqdm
import random
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def DropAllTables(mycursor):
    print("Dropping All Tables...")
    DropFeedbackTable(mycursor)
    DropSearchHistoryTable(mycursor)
    DropScheduleTable(mycursor)
    DropCourseStatsTable(mycursor)
    DropCoursePropertiesTable(mycursor)
    DropRegisteredUserTable(mycursor)


def DropRegisteredUserTable(mycursor):
    try: mycursor.execute("DROP TABLE RegisteredUser")
    except: pass


def DropCourseStatsTable(mycursor):
    try: mycursor.execute("DROP TABLE CourseStats")
    except: pass


def DropFeedbackTable(mycursor):
    try: mycursor.execute("DROP TABLE Feedback")
    except: pass


def DropScheduleTable(mycursor):
    try: mycursor.execute("DROP TABLE Schedule")
    except: pass


def DropSearchHistoryTable(mycursor):
    try: mycursor.execute("DROP TABLE SearchHistory")
    except: pass


def DropCoursePropertiesTable(mycursor):
    try: mycursor.execute("DROP TABLE CourseProperties")
    except: pass


def CreateAllTables(mycursor):
    print("Creating All Tables...")
    CreateRegisteredUserTable(mycursor)
    CreateCoursePropertiesTable(mycursor)
    CreateCourseStatsTable(mycursor)
    CreateFeedbackTable(mycursor)
    CreateScheduleTable(mycursor)
    CreateSearchHistoryTable(mycursor)

def CreateRegisteredUserTable(mycursor):
    try: mycursor.execute("CREATE TABLE RegisteredUser (NetID VARCHAR(20) NOT NULL, Password VARCHAR(100) NOT NULL, PRIMARY KEY(NetID))")
    except: pass


def CreateCourseStatsTable(mycursor):
    try: mycursor.execute('CREATE TABLE CourseStats (CourseID INT NOT NULL, Year VARCHAR(10) NOT NULL, Term VARCHAR(10) NOT NULL, Professor VARCHAR(100) NOT NULL, AP INT, A INT, AM INT, BP INT, B INT, BM INT, CP INT, C INT, CM INT, DP INT, D INT, DM INT, F INT, W INT, FOREIGN KEY (CourseID) REFERENCES CourseProperties(CourseID))')
    except: pass


def CreateFeedbackTable(mycursor):
    try: mycursor.execute("CREATE TABLE Feedback (NetID VARCHAR(20) NOT NULL, CourseID INT NOT NULL, Professor VARCHAR(100) NOT NULL, Rating INT NOT NULL, TimeConsumption VARCHAR(20), Comment VARCHAR(500), TimeStamp VARCHAR(100) NOT NULL, PRIMARY KEY(NetID, CourseID, Professor), FOREIGN KEY (NetID) REFERENCES RegisteredUser (NetID), FOREIGN KEY(CourseID) REFERENCES CourseProperties(CourseID))")
    except: pass


def CreateScheduleTable(mycursor):
    try: mycursor.execute("CREATE TABLE Schedule (NetID VARCHAR(20) NOT NULL, Professor VARCHAR(100) NOT NULL, CourseID INT NOT NULL, Year VARCHAR(10) NOT NULL, Term VARCHAR(10) NOT NULL, SchoolYear VARCHAR(10) NOT NULL, PRIMARY KEY(NetID, CourseID, Year, Term), FOREIGN KEY (CourseID) REFERENCES CourseProperties (CourseID), FOREIGN KEY (NetID) REFERENCES RegisteredUser (NetID))")
    except: pass


def CreateSearchHistoryTable(mycursor):
    try: mycursor.execute("CREATE TABLE SearchHistory (NetID VARCHAR(20) NOT NULL, CourseID INT NOT NULL, Professor VARCHAR(100) NOT NULL, PRIMARY KEY(NetID, CourseID, Professor), FOREIGN KEY(NetID) REFERENCES RegisteredUser(NetID), FOREIGN KEY(CourseID) REFERENCES CourseProperties(CourseID))")
    except: pass


def CreateCoursePropertiesTable(mycursor):
    try: mycursor.execute("CREATE TABLE CourseProperties (CourseID INT NOT NULL, CourseTitle VARCHAR(100) NOT NULL, CourseDescription VARCHAR(1000), Prerequisites VARCHAR(250), LinkedSections VARCHAR(50), CourseWebsiteLink VARCHAR(200), CourseNumber INT NOT NULL, CourseTag VARCHAR(100), Subject VARCHAR(10) NOT NULL, PRIMARY KEY (CourseID))")
    except: pass


def InitializeAllTables(mycursor, mydb):
    print("Initializing All Tables...")
    InitializeRegisteredUserTable(mycursor, mydb)
    InitializeCoursePropertiesTable(mycursor, mydb)
    InitializeCourseStatsTable(mycursor, mydb)
    InitializeScheduleTable(mycursor, mydb)
    InitializeSearchHistoryTable(mycursor, mydb)
    InitializeFeedbackTable(mycursor, mydb)


def GetAllCSVFilesOnGitHub():
    webUrl = urllib.request.urlopen("https://github.com/wadefagen/datasets/tree/master/gpa/raw")
    csvFiles = []
    for word in str(webUrl.read()).split(): 
        if("title=" in word and ".csv" in word): csvFiles.append(word[7:-1])
    webUrl.close()
    return csvFiles


def InitializeRegisteredUserTable(mycursor, mydb):
    namesFile = open("Names.txt", "r")
    for count, name in tqdm(iterable=enumerate(namesFile), desc ="Registered User Table Progress"):
        if(" " in name): name.replace(" ", "")
        name = name[:-1]
        if(name == ""): continue
        sql = "INSERT INTO RegisteredUser VALUES (%s, %s)"
        val = (name, "".join(sorted(name)) + str(count))
        try: mycursor.execute(sql, val)
        except: continue
    mydb.commit()


def InitializeSearchHistoryTable(mycursor, mydb):
    mycursor.execute("SELECT NetID FROM RegisteredUser LIMIT 1000")
    RegisteredUserTable = mycursor.fetchall()

    mycursor.execute("SELECT DISTINCT CourseID, Professor FROM CourseStats LIMIT 1000")
    CourseStatsTables = mycursor.fetchall()

    for i in tqdm(range(1000), desc ="Search History Table Progress"):
        sql = "INSERT INTO SearchHistory VALUES (%s, %s, %s)"
        randInd = random.randint(0, 999)
        val = (RegisteredUserTable[random.randint(0, 999)][0], CourseStatsTables[randInd][0], CourseStatsTables[randInd][1])
        try: mycursor.execute(sql, val)
        except: continue

    mydb.commit()


def InitializeFeedbackTable(mycursor, mydb):
    mycursor.execute("SELECT NetID FROM RegisteredUser")
    RegisteredUserTable = mycursor.fetchall()

    mycursor.execute("SELECT DISTINCT CourseID, Professor FROM CourseStats LIMIT 1000")
    CourseStatsTables = mycursor.fetchall()
    comments = ['I really love ', 'I really hate ', 'The worst class in UIUC is ', 'The best class in UIUC is ', 'The best class in UIUC is ', 'Please Don\'t take this class: ', 'Save yourself from ', 'I didn\'t learn anything from ']

    for i in tqdm(range(1000), desc ="Search History Table Progress"):
        sql = "INSERT INTO Feedback VALUES (%s, %s, %s, %s, %s, %s, %s)"
        randInd = random.randint(0, 999)

        mycursor.execute("SELECT Subject, CourseNumber FROM CourseProperties WHERE CourseID = " + str(CourseStatsTables[randInd][0]))
        CoursePropertiesRow = mycursor.fetchall()[0]

        val = (RegisteredUserTable[i][0], str(CourseStatsTables[randInd][0]), CourseStatsTables[randInd][1], str(random.randint(0, 5)), str(random.randint(0, 25)), comments[random.randint(0, len(comments) - 1)] + CoursePropertiesRow[0] + " " + str(CoursePropertiesRow[1]), datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        
        try: mycursor.execute(sql, val)
        except: continue

    mydb.commit()


def InitializeScheduleTable(mycursor, mydb):
    mycursor.execute("SELECT NetID FROM RegisteredUser LIMIT 205")
    RegisteredUserTable = mycursor.fetchall()

    schoolYears = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    semesters = ['fa', 'sp']
    years = [i for i in range(2010, 2020)]
    
    for i in tqdm(range(205), desc ="Schedule Table Progress"):
        schoolYear = schoolYears[random.randint(0, 3)]
        sem = semesters[random.randint(0, 1)]
        classes = []
        year = years[random.randint(0, len(years) - 1)]
        
        for j in range(5):
            classCourseID = 0
            CourseStatsTables = []

            while classCourseID in classes or len(CourseStatsTables) == 0: 
                classCourseID = random.randint(0, 1999)
                mycursor.execute("SELECT Professor, Year, Term FROM CourseStats WHERE CourseID = " + str(classCourseID) + " AND Term = \"" + sem + "\" AND Year = " + str(year))
                CourseStatsTables = mycursor.fetchall()

            sql = "INSERT INTO Schedule VALUES (%s, %s, %s, %s, %s, %s)"
            CourseStatsTables = CourseStatsTables[random.randint(0, len(CourseStatsTables)-1)]
            val = (RegisteredUserTable[i][0], CourseStatsTables[0], str(classCourseID), str(CourseStatsTables[1]), CourseStatsTables[2], schoolYear)

            try: mycursor.execute(sql, val)
            except: continue

    mydb.commit()


def InitializeCoursePropertiesTable(mycursor, mydb):
    csvFiles = GetAllCSVFilesOnGitHub()
    SubAndNumList = []
    titles = []
    count = 0
    courseNumberField = None
    courseSubjectField = None
    courseNumberFieldName = None
    courseSubjectFieldName = None

    for csvFile in tqdm(iterable =csvFiles, desc ="Course Properties Table CSV Files Progress"):
        pdf = pd.read_csv("https://raw.githubusercontent.com/wadefagen/datasets/master/gpa/raw/" + csvFile, encoding = "ISO-8859-1")

        if 'Course' in pdf.columns: courseNumberFieldName = 'Course'
        elif 'Course ' in pdf.columns: courseNumberFieldName = 'Course '
        else: courseNumberFieldName = 'Course Number'
        
        for colName in pdf.columns:
            if('Subject' in colName): 
                courseSubjectFieldName = colName
                break

        for index, row in pdf.iterrows():
            courseSubjectField = row[courseSubjectFieldName]
            courseNumberField = row[courseNumberFieldName]

            if(" " in courseSubjectField): courseSubjectField.replace(" ", "")
            
            if((courseSubjectField, courseNumberField) not in SubAndNumList):
                SubAndNumList.append((courseSubjectField, courseNumberField))
                sql = "INSERT INTO CourseProperties(CourseID, CourseTitle, CourseNumber, Subject) VALUES (%s, %s, %s, %s)"
                val = (int(count), row['Course Title'], int(courseNumberField), courseSubjectField)

                try:
                    mycursor.execute(sql, val)
                    count += 1
                except: continue

        mydb.commit()


def InitializeCoursePropertiesTableNullAttributes(mycursor, mydb):
    pass


def InitializeCourseStatsTable(mycursor, mydb):
    csvFiles = GetAllCSVFilesOnGitHub()
    courseNumberFieldName = None
    courseSubjectFieldName = None

    for csvFile in tqdm(iterable =csvFiles, desc ="Course Stats CSV Table Files Progress"):
        pdf = pd.read_csv("https://raw.githubusercontent.com/wadefagen/datasets/master/gpa/raw/" + csvFile, encoding = "ISO-8859-1")

        if 'Course' in pdf.columns: courseNumberFieldName = 'Course'
        elif 'Course ' in pdf.columns: courseNumberFieldName = 'Course '
        else: courseNumberFieldName = 'Course Number'
        
        for colName in pdf.columns:
            if('Subject' in colName): 
                courseSubjectFieldName = colName
                break
        
        for index, row in pdf.iterrows():
            mycursor.execute("SELECT CourseID FROM CourseProperties WHERE CourseNumber = \"" + str(row[courseNumberFieldName]) + "\" AND Subject = \"" + row[courseSubjectFieldName] + "\"")
            courseID = mycursor.fetchall()

            if(len(courseID) == 0): continue
            courseID = courseID[0][0]

            sql = "INSERT INTO CourseStats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            try: mycursor.execute(sql, (courseID, csvFile[2:-4], csvFile[:2], row['Primary Instructor'], int(row['A+']), int(row['A']), int(row['A-']), int(row['B+']), int(row['B']), int(row['B-']), int(row['C+']), int(row['C']), int(row['C-']), int(row['D+']), int(row['D']), int(row['D-']), int(row['F']), int(row['W'])))
            except: continue

        mydb.commit()
   

def createDriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
   

def InitializeProfessorImages(mycursor, mydb):
    driver = createDriver()

    mycursor.execute("SELECT distinct Professor FROM CourseStats")
    Professors = mycursor.fetchall()

    for Professor in tqdm(iterable =Professors, desc ="Professor Images Table Progress"):
        Professor = Professor[0]
        count = 0

        while True:
            driver.get("https://www.google.com/search?q=uiuc+"+Professor+"&tbm=isch")
            src = None

            try:
                for v in driver.find_elements_by_tag_name('img'):
                    if(v.get_attribute('class') == 'rg_i Q4LuWd'): 
                        src = v.get_attribute("src")
                        break
            except: src = None

            if src != None:
                sql = "INSERT INTO ProfessorImages VALUES (%s, %s)"
                val = (Professor, src)
                try: mycursor.execute(sql, val)
                except: pass
                break
            else:
                if count > 0: break
                count += 1
                mydb.commit()
                driver.close()
                driver = createDriver()
    
    driver.close()


def ShowRegisteredUserTable(mycursor):
    mycursor.execute("SELECT * FROM RegisteredUser")
    myresult = mycursor.fetchall()
    for x in myresult: print(x)


def ShowSearchHistoryTable(mycursor):
    mycursor.execute("SELECT * FROM SearchHistory")
    myresult = mycursor.fetchall()
    for x in myresult: print(x)


def ShowCourseStatsTable(mycursor):
    mycursor.execute("SELECT * FROM CourseStats")
    myresult = mycursor.fetchall()
    for x in myresult: print(x)
    

def ShowCoursePropertiesTable(mycursor):
    mycursor.execute("SELECT * FROM CourseProperties")
    myresult = mycursor.fetchall()
    for x in myresult: print(x)


def ShowFeedbackTable(mycursor):
    mycursor.execute("SELECT * FROM Feedback")
    myresult = mycursor.fetchall()
    for x in myresult: print(x)


def ShowScheduleTable(mycursor):
    mycursor.execute("SELECT * FROM Schedule")
    myresult = mycursor.fetchall()
    for x in myresult: print(x)


def ConnectDatabase():
    mydb = connector.connect(host="34.121.180.219", user="root", password="z1mpLslBvvkKOnmN", database="UIUCMVP")
    return mydb.cursor(), mydb


def CreateDatabase():
    mycursor, mydb = ConnectDatabase()
    DropAllTables(mycursor)
    CreateAllTables(mycursor)
    InitializeAllTables(mycursor, mydb)


if __name__ == "__main__":
    mycursor, mydb = ConnectDatabase()
    print("Call the function!!!!")
    mycursor.close()
    mydb.close()
