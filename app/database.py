"""Defines all the functions related to the database"""
from app import db

MAX_NETID_LEN = 20
MAX_PASSWORD_LEN = 100
MAX_PROFESSOR_LEN = 100
MAX_YEAR_LEN = 10
MAX_TERM_LEN = 10
MAX_SUBJECT_LEN = 10
MAX_COURSETAG_LEN = 100
MAX_COURSEWEBSITELINK_LEN = 200
MAX_LINKEDSECTION_LEN = 50
MAX_PREREQUISITES_LEN = 250
MAX_COURSEDESCRIPTION_LEN = 1000
MAX_COURSETITLE_LEN = 100
MAX_TIMECONSUMPTION_LEN = 20
MAX_COMMENT_LEN = 500
MAX_TIMESTAMP_LEN = 20
MAX_SCHOOLYEAR_LEN = 10

def assertProfessor(Professor: str, CourseID: int) -> bool:
    conn = db.connect()
    query_results = conn.execute("Select * from CourseStats where Professor = '{}' and CourseID = {};".format(Professor, CourseID)).fetchall()
    conn.close()
    return len(query_results) > 0

def getProfessors():
    conn = db.connect()
    query_results = conn.execute("Select distinct Professor from CourseStats;").fetchall()
    conn.close()
    final_list = []
    for result in query_results: final_list.append(result[0])
    return final_list

def checkRegisteredUser(NetID: str, Password: str) -> bool:
    conn = db.connect()
    query_results = conn.execute("Select * from RegisteredUser where NetID = '{}' and Password = '{}';".format(NetID, Password)).fetchall()
    conn.close()
    return len(query_results) == 1


def checkAdminUser(NetID: str, Password: str) -> bool:
    conn = db.connect()
    query_results = conn.execute("Select * from AdminUser where NetID = '{}' and Password = '{}';".format(NetID, Password)).fetchall()
    conn.close()
    return len(query_results) == 1


def fetch_RegisteredUser(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from RegisteredUser order by NetID limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from RegisteredUser order by NetID;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "Password": result[1]
        }
        final_list.append(item)

    return final_list


def fetch_ProfessorImages(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from ProfessorImages order by Professor limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from ProfessorImages order by Professor;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "Professor": result[0],
            "URL": result[1]
        }
        final_list.append(item)

    return final_list


def fetch_AdminUser(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from AdminUser order by NetID limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from AdminUser order by NetID;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "Password": result[1]
        }
        final_list.append(item)

    return final_list


def fetch_SearchHistory(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from SearchHistory order by NetID limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from SearchHistory order by NetID;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "CourseID": result[1],
            "Professor": result[2]
        }
        final_list.append(item)

    return final_list


def fetch_CourseProperties(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from CourseProperties order by CourseID limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from CourseProperties order by CourseID;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "CourseTitle": result[1],
            "CourseDescription": result[2],
            "Prerequisites": result[3],
            "LinkedSections": result[4],
            "CourseWebsiteLink": result[5],
            "CourseNumber": result[6],
            "CourseTag": result[7],
            "Subject": result[8]
        }
        final_list.append(item)

    return final_list


def fetch_CourseStats(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from CourseStats order by CourseID, Year, Term limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from CourseStats order by CourseID, Year, Term;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Year": result[1],
            "Term": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17]
        }
        final_list.append(item)

    return final_list


def fetch_Feedback(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from Feedback order by NetID, CourseID limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from Feedback order by NetID, CourseID;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "CourseID": result[1],
            "Professor": result[2],
            "Rating": result[3],
            "TimeConsumption": result[4],
            "Comment": result[5],
            "TimeStamp": result[6]
        }
        final_list.append(item)

    return final_list


def fetch_Schedule(lim: int) -> dict:
    conn = db.connect()
    if(lim > 0): query_results = conn.execute("Select * from Schedule order by NetID, Year, Term limit {};".format(lim)).fetchall()
    else: query_results = conn.execute("Select * from Schedule order by NetID, Year, Term;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "Professor": result[1],
            "CourseID": result[2],
            "Year": result[3],
            "Term": result[4],   
            "SchoolYear": result[5]
        }
        final_list.append(item)

    return final_list
###################################################################################################################################################################


###################################################################################################################################################################
def update_RegisteredUser(NetID: str, Password: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update RegisteredUser set Password = "{}" where NetID = "{}";'.format(Password, NetID)
    conn.execute(query)
    conn.close()


def update_AdminUser(NetID: str, Password: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update AdminUser set Password = "{}" where NetID = "{}";'.format(Password, NetID)
    conn.execute(query)
    conn.close()


def update_ProfessorImages(Professor: str, URL: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update ProfessorImages set URL = "{}" where Professor = "{}";'.format(URL, Professor)
    conn.execute(query)
    conn.close()


def update_SearchHistory(NetID: str, CourseID: int, Professor: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update SearchHistory set Professor = "{}", CourseID = {} where NetID = "{}" ;'.format(Professor, CourseID, NetID)
    conn.execute(query)
    conn.close()


def update_CourseStats(CourseID: int, Year: str, Term: str, Professor: str, AP: int, A: int, AM: int, BP: int, B: int, BM: int, CP: int, C: int, CM: int, DP: int, D: int, DM: int, F: int, W: int) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update CourseStats set AP = {}, A = {}, AM = {}, BP = {}, B = {}, BM = {}, CP = {}, C = {}, CM = {}, DP = {}, D = {}, DM = {}, F = {}, W = {} where CourseID = {} and Year = "{}" and Term = "{}" and Professor = "{}";'.format(AP, A, AM, BP, B, BM, CP, C, CM, DP, D, DM, F, W, CourseID, Year, Term, Professor)
    conn.execute(query)
    conn.close()


def update_CourseProperties(CourseID : int, CourseTitle : str, CourseDescription : str, Prerequisites : str, LinkedSections : str, CourseWebsiteLink : str, CourseNumber : int, CourseTag : str, Subject : str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update CourseProperties set CourseTitle = "{}", CourseDescription = "{}", Prerequisites = "{}", LinkedSections = "{}", CourseWebsiteLink = "{}", CourseNumber = {},  CourseTag = "{}", Subject = "{}" where CourseID = {};'.format(CourseTitle, CourseDescription, Prerequisites, LinkedSections, CourseWebsiteLink, CourseNumber, CourseTag, Subject, CourseID)
    conn.execute(query)
    conn.close()


def update_Feedback(NetID: str, CourseID : int, Professor : str, Rating : int, TimeConsumption : str, Comment : str, TimeStamp : str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update Feedback set Rating = {}, TimeConsumption = "{}", Comment = "{}", TimeStamp = "{}" where NetID = "{}" and CourseID = {} and Professor = "{}";'.format(Rating, TimeConsumption, Comment, TimeStamp, NetID, CourseID, Professor)
    conn.execute(query)
    conn.close()


def update_Schedule(NetID: str, Professor : str, CourseID : int, Year : str, Term : str, SchoolYear: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'Update Schedule set SchoolYear = "{}" where NetID = "{}" and CourseID = {} and Professor = "{}" and Year = "{}" and Term = "{}";'.format(SchoolYear, NetID, CourseID, Professor, Year, Term)
    conn.execute(query)
    conn.close()
###################################################################################################################################################################


###################################################################################################################################################################
def insert_new_RegisteredUser(NetID: str, Password: str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO RegisteredUser VALUES ("{}", "{}");'.format(NetID, Password)
    conn.execute(query)
    conn.close()
    

def insert_new_AdminUser(NetID: str, Password: str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO AdminUser VALUES ("{}", "{}");'.format(NetID, Password)
    conn.execute(query)
    conn.close()

    
def insert_new_ProfessorImages(Professor: str, URL: str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Password) > MAX_PASSWORD_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO ProfessorImages VALUES ("{}", "{}");'.format(Professor, URL)
    conn.execute(query)
    conn.close()


def insert_new_SearchHistory(NetID: str, CourseID : int, Professor : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO SearchHistory VALUES ("{}", {}, "{}");'.format(NetID, CourseID, Professor)
    conn.execute(query)
    conn.close()


def insert_new_CourseStats(CourseID : int, Year : str, Term : str, Professor : str, AP : int, A : int, AM : int, BP : int, B : int, BM : int, CP : int, C : int, CM : int, DP : int, D : int, DM : int, F : int, W : int) ->  None:
    #if(len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(Professor) > MAX_PROFESSOR_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO CourseStats VALUES ({}, "{}", "{}", "{}", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});'.format(CourseID, Year, Term, Professor, AP, A, AM, BP, B, BM, CP, C, CM, DP, D, DM, F, W)
    conn.execute(query)
    conn.close()


def insert_new_CourseProperties(CourseID : int, CourseTitle : str, CourseDescription : str, Prerequisites : str, LinkedSections : str, CourseWebsiteLink : str, CourseNumber : int, CourseTag : str, Subject : str) ->  None:
    #if(len(CourseTitle) > MAX_COURSETITLE_LEN or len(CourseDescription) > MAX_COURSEDESCRIPTION_LEN or len(Prerequisites) > MAX_PREREQUISITES_LEN or len(LinkedSections) > MAX_LINKEDSECTION_LEN or len(CourseWebsiteLink) > MAX_COURSEWEBSITELINK_LEN or len(CourseTag) > MAX_COURSETAG_LEN or len(Subject) > MAX_SUBJECT_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO CourseProperties VALUES ({}, "{}", "{}", "{}", "{}", "{}", {}, "{}", "{}");'.format(CourseID, CourseTitle, CourseDescription, Prerequisites, LinkedSections, CourseWebsiteLink, CourseNumber, CourseTag, Subject)
    conn.execute(query)
    conn.close()


def insert_new_Feedback(NetID: str, CourseID : int, Professor : str, Rating : int, TimeConsumption : str, Comment : str, TimeStamp : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(TimeConsumption) > MAX_TIMECONSUMPTION_LEN or len(Comment) > MAX_COMMENT_LEN or len(TimeStamp) > MAX_TIMESTAMP_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO Feedback VALUES ("{}", {}, "{}", {}, "{}", "{}", "{}");'.format(NetID, CourseID, Professor, Rating, TimeConsumption, Comment, TimeStamp)
    conn.execute(query)
    conn.close()


def insert_new_Schedule(NetID: str, Professor : str, CourseID : int, Year : str, Term : str, SchoolYear : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO Schedule VALUES ("{}", "{}", {}, "{}", "{}", "{}");'.format(NetID, Professor, CourseID, Year, Term, SchoolYear)
    conn.execute(query)
    conn.close()


def insert_new_ProfessorImages(Professor : str, URL : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'INSERT INTO ProfessorImages VALUES ("{}", "{}");'.format(Professor, URL)
    conn.execute(query)
    conn.close()
###################################################################################################################################################################



###################################################################################################################################################################
def remove_RegisteredUser_by_NetID(NetId: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN): return False
    conn = db.connect()
    query = 'Delete From RegisteredUser where NetID="{}";'.format(NetId)
    conn.execute(query)
    conn.close()
    

def remove_AdminUser_by_NetID(NetId: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN): return False
    conn = db.connect()
    query = 'Delete From AdminUser where NetID="{}";'.format(NetId)
    conn.execute(query)
    conn.close()
    

def remove_ProfessorImages_by_Professor(Professor: str) -> None:
    #if(len(NetID) > MAX_NETID_LEN): return False
    conn = db.connect()
    query = 'Delete From ProfessorImages where Professor="{}";'.format(Professor)
    conn.execute(query)
    conn.close()


def remove_SearchHistory_entry(NetID: str, CourseID : int, Professor : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN): return False
    conn = db.connect()
    query = 'Delete From SearchHistory where NetID="{}" and CourseID={} and Professor="{}";'.format(NetID, CourseID, Professor)
    conn.execute(query)
    conn.close


def remove_Feedback_entry(NetID: str, CourseID : int, Professor : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN): return False
    conn = db.connect()
    query = 'Delete from Feedback where NetID="{}" and CourseID={} and Professor="{}";'.format(NetID, CourseID, Professor)
    conn.execute(query)
    conn.close()


def remove_Schedule_entry(NetID: str, Professor : str, CourseID : int, Year : str, Term : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'Delete from Schedule where NetID="{}" and Professor="{}" and CourseID={} and Year="{}" and Term="{}";'.format(NetID, Professor, CourseID, Year, Term)
    conn.execute(query)
    conn.close()


def remove_CourseStats_entry(CourseID : int, Year : str, Term : str, Professor : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'Delete from CourseStats where Professor="{}" and CourseID={} and Year="{}" and Term="{}";'.format(Professor, CourseID, Year, Term)
    conn.execute(query)
    conn.close()


def remove_CourseProperties_entry(CourseID : int) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'Delete from CourseProperties where CourseID={};'.format(CourseID)
    conn.execute(query)
    conn.close()


def remove_ProfessorImages(Professor : str) ->  None:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'Delete from ProfessorImages where Professor = "{}";'.format(Professor)
    conn.execute(query)
    conn.close()
###################################################################################################################################################################


###################################################################################################################################################################
def search_CourseStats_by_professor(Professor: str) -> dict:
    conn = db.connect()
    query = 'Select CourseID, Professor from CourseStats where Professor LIKE "%%{}%%";'.format(Professor)
    query_results = conn.execute(query).fetchall()
    conn.close()
    final_list = []
    for result in query_results:        
        item = {
            "CourseID": result[0],
            "Year": result[1],
            "Term": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17]
        }
        final_list.append(item)
    return final_list

def search_CourseStats_by_Subject(Subject: str) -> dict:
    conn = db.connect()
    query = 'Select * from CourseStats where Subject = "{}";'.format(Subject)
    query_results = conn.execute(query).fetchall()
    conn.close()
    final_list = []
    for result in query_results:        
        item = {
            "CourseID": result[0],
            "Year": result[1],
            "Term": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17]
        }
        final_list.append(item)
    return final_list

def search_CourseStats_by_CourseID(CourseID: int) -> dict:
    conn = db.connect()
    query = 'Select * from CourseStats where CourseID = {};'.format(CourseID)
    query_results = conn.execute(query).fetchall()
    conn.close()
    final_list = []
    for result in query_results:        
        item = {
            "CourseID": result[0],
            "Year": result[1],
            "Term": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17]
        }
        final_list.append(item)
    return final_list

def search_ProfessorImages_by_Professor(Professor : str) ->  dict:
    #if(len(NetID) > MAX_NETID_LEN or len(Professor) > MAX_PROFESSOR_LEN or len(Year) > MAX_YEAR_LEN or len(Term) > MAX_TERM_LEN or len(SchoolYear) > MAX_SCHOOLYEAR_LEN): return False
    conn = db.connect()
    query = 'Select * from ProfessorImages where Professor = "{}";'.format(Professor)
    query_results = conn.execute(query).fetchall()
    conn.close()
    final_list = []
    for result in query_results:        
        item = {
            "Professor": result[0],
            "URL": result[1]
        }
        final_list.append(item)
    return final_list
###################################################################################################################################################################


###################################################################################################################################################################
def search_CourseProperties_by_course(Subject: str, CourseNumber: int) -> dict:
    conn = db.connect()
    query = 'Select * from CourseProperties WHERE Subject = "' + Subject + '" AND CourseNumber = ' + str(CourseNumber) + ';'
    try: 
        query_results = conn.execute(query).fetchall()
    except Exception as e: 
        print(e)
        return []
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "CourseTitle": result[1],
            "CourseDescription": result[2],
            "Prerequisites": result[3],
            "LinkedSections": result[4],
            "CourseWebsiteLink": result[5],
            "CourseNumber": result[6],
            "CourseTag": result[7],
            "Subject": result[8]
        }
        final_list.append(item)

    return final_list

def search_SearchHistory_by_professor_and_course(Professor: str, CourseID: int) -> dict:
    conn = db.connect()
    query = 'Select * from SearchHistory WHERE Professor LIKE "%%{}%%" AND CourseID LIKE {};'.format(Professor, CourseID)
    try: 
        query_results = conn.execute(query).fetchall()
    except Exception as e: 
        print(e)
        return []
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "CourseID": result[1],
            "Professor": result[2]
        }
        final_list.append(item)

    return final_list


def search_RegisteredUser_by_netid(NetID: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from RegisteredUser where NetID LIKE "%%{}%%" order by NetID;'.format(NetID)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "Password": result[1]
        }
        final_list.append(item)

    return final_list


def search_AdminUser_by_netid(NetID: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from AdminUser where NetID LIKE "%%{}%%" order by NetID;'.format(NetID)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "Password": result[1]
        }
        final_list.append(item)

    return final_list


def search_ProfessorImages_by_Professor(Professor: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from ProfessorImages where Professor LIKE "%%{}%%" order by Professor;'.format(Professor)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "Professor": result[0],
            "URL": result[1]
        }
        final_list.append(item)

    return final_list


def search_CourseStats_by_course_and_year(CourseID: int, Year: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from CourseStats where CourseID = {} and Year = "{}" order by CourseID, Year, Term;'.format(CourseID, Year)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Year": result[1],
            "Term": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17]
        }
        final_list.append(item)

    return final_list


def search_Feedback_by_professor(Professor: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from Feedback where Professor LIKE "%%{}%%" order by NetID, CourseID;'.format(Professor)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "CourseID": result[1],
            "Professor": result[2],
            "Rating": result[3],
            "TimeConsumption": result[4],
            "Comment": result[5],
            "TimeStamp": result[6]
        }
        final_list.append(item)

    return final_list


def search_Feedback_by_professor_and_course(Professor: str, CourseID: int) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from Feedback where Professor = "{}" and CourseID = {} order by TimeStamp desc;'.format(Professor, CourseID)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "CourseID": result[1],
            "Professor": result[2],
            "Rating": result[3],
            "TimeConsumption": result[4],
            "Comment": result[5],
            "TimeStamp": result[6]
        }
        final_list.append(item)

    return final_list


def search_Schedule_by_netid(NetID: str) -> dict:
    conn = db.connect()
    query_results = conn.execute('Select * from Schedule where NetID like "%%{}%%" order by NetID, Year, Term;'.format(NetID)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "NetID": result[0],
            "Professor": result[1],
            "CourseID": result[2],
            "Year": result[3],
            "Term": result[4],   
            "SchoolYear": result[5]
        }
        final_list.append(item)

    return final_list


def get_subjects_from_CourseProperties() -> dict:
    conn = db.connect()
    query_results = conn.execute('Select distinct Subject from CourseProperties;').fetchall()
    conn.close()
    final_list = []
    for result in query_results: final_list.append(result[0])
    return final_list


###################################################################################################################################################################


###################################################################################################################################################################
def advance_pratik_query() -> dict:
    conn = db.connect()
    query_results = conn.execute("SELECT a.Professor, SUM(Rating), COUNT(NetID) FROM (SELECT Professor, Rating FROM Feedback) a JOIN SearchHistory b ON a.Professor = b.Professor GROUP BY a.Professor ORDER BY a.Professor;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "Professor": result[0],
            "Ratings": result[1],
            "CountofNetID": result[2]
        }
        final_list.append(item)
    return final_list

def advance_dimitar_query() -> dict:
    conn = db.connect()
    query_results = conn.execute("SELECT COUNT(CourseID) as numCourses, Professor FROM (SELECT CourseID, Professor FROM CourseProperties NATURAL JOIN CourseStats WHERE Professor LIKE '%%%%') as joined_table GROUP BY Professor ORDER BY numCourses DESC;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "numCourses": result[0],
            "Professor": result[1]
        }
        final_list.append(item)
    return final_list

def advance_michael_query() -> dict:
    conn = db.connect()
    query_results = conn.execute("SELECT CourseTitle, Avg(TimeConsumption) as avgTime FROM CourseStats JOIN Feedback USING(CourseID) JOIN CourseProperties USING (CourseId) GROUP BY CourseID ORDER BY avgTime DESC;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseTitle": result[0],
            "AvgTimeConsumption": result[1]
        }
        final_list.append(item)
    return final_list

def advance_omar_query() -> dict:
    conn = db.connect()
    query_results = conn.execute("SELECT cs.Professor, cp.CourseTitle, SUM(AP) AS num_Aplus, SUM(A) AS num_A, SUM(AM) AS num_Aminus FROM CourseStats cs NATURAL JOIN CourseProperties cp GROUP BY cs.Professor, cp.CourseTitle ORDER BY num_Aplus DESC, num_A DESC, num_Aminus DESC;").fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "Professor": result[0],
            "CourseTitle": result[1],
            "Aplus":result[2],
            "A": result[3],
            "Aminus": result[4]
        }
        final_list.append(item)
    return final_list
###################################################################################################################################################################


###################################################################################################################################################################
def rank_by_professor_subject_courseNumber(Professor:str, Subject:str, CourseNumber:int, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties where Subject = "{}" and CourseNumber = {}) as temp where Professor LIKE "%%{}%%" group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(Subject, CourseNumber, Professor, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_professor_subject(Professor:str, Subject:str, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties where Subject = "{}") as temp where Professor LIKE "%%{}%%" group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(Subject, Professor, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_professor_courseNumber(Professor:str, CourseNumber:int, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties where CourseNumber = {}) as temp where Professor LIKE "%%{}%%" group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(CourseNumber, Professor, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_subject_courseNumber(Subject:str, CourseNumber:int, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties where Subject = "{}" and CourseNumber = {}) as temp group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(Subject, CourseNumber, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_professor(Professor:str, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties) as temp where Professor LIKE "%%{}%%" group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(Professor, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_subject(Subject:str, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties where Subject = "{}") as temp group by Professor, CourseID order by GPA desc, Professor LIMIT {};'.format(Subject, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_courseNumber(CourseNumber:int, limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties where CourseNumber = {}) as temp group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(CourseNumber, limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list


def rank_by_nothing(limit:int) -> dict:
    conn = db.connect()
    query_results = conn.execute('SELECT CourseID, Subject, CourseNumber, Professor, SUM(AP), SUM(A), SUM(AM), SUM(BP), SUM(B), SUM(BM), SUM(CP), SUM(C), SUM(CM), SUM(DP), SUM(D), SUM(DM), SUM(F), SUM(W), (4.0*SUM(AP)+4.00*SUM(A)+SUM(AM)*3.67+SUM(BP)*3.33+SUM(B)*3.00+SUM(BM)*2.67+SUM(CP)*2.33+SUM(C)*2.00+SUM(CM)*1.67+SUM(DP)*1.33+SUM(D)+SUM(DM)*0.67)/(SUM(AP)+SUM(A)+SUM(AM)+SUM(BP)+SUM(B)+SUM(BM)+SUM(CP)+SUM(C)+SUM(CM)+SUM(DP)+SUM(D)+SUM(DM)+SUM(F)+SUM(W)) as GPA from CourseStats natural join (select * from CourseProperties) as temp group by Professor, CourseID order by GPA DESC, Professor LIMIT {};'.format(limit)).fetchall()
    conn.close()
    final_list = []
    for result in query_results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "AP": result[4],
            "A": result[5],
            "AM": result[6],
            "BP": result[7],
            "B": result[8],
            "BM": result[9],
            "CP": result[10],
            "C": result[11],
            "CM": result[12],
            "DP": result[13],
            "D": result[14],
            "DM": result[15],
            "F": result[16],
            "W": result[17],
            "GPA": round(result[18], 2)
        }
        final_list.append(item)
    return final_list

def fetch_storedProcedure(tags, yearFlag, covidFlag, gpaFlag, ratingFlag, workFlag, gpaThreshold, yearThreshold, ratingThreshold, workThreshold):
    conn = db.connect()

    query = "call UIUCMVP.search_geneds('{}', {}, {}, {}, {}, {}, {}, {}, {}, {});".format(tags, yearFlag, covidFlag, gpaFlag, ratingFlag, workFlag, gpaThreshold, yearThreshold, ratingThreshold, workThreshold)
    print(query)
    results = conn.execute(query)
    conn.close()
    

    final_list = []
    for result in results:
        item = {
            "CourseID": result[0],
            "Subject": result[1],
            "CourseNumber": result[2],
            "Professor": result[3],
            "GenEd_Tags": result[4],
            "Average_GPA": result[5],
            "Average_Rating": result[6],
            "Average_Work_Hours": result[7]
        }
        final_list.append(item)
    return final_list

        