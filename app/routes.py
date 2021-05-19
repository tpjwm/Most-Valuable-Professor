""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, session
from app import app
from app import database as db_helper
import datetime
# from .User import User
import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
import atexit

@app.route('/signup')
def signup(): 
    try: user = session['NetID']
    except: user = None

    if(user == None): return render_template("SignUpPage.html")
    else: return redirect("/")


@app.route("/logout")
def logout():
    try: user = session['NetID']
    except: user = None

    if user != None:
        session['NetID'] = None
        session['AdminUser'] = False
    return redirect("/login")


@app.route("/aboutUs")
def aboutus():
    try: 
        user = session['NetID']
        admin = session['AdminUser']
    except: 
        user = None
        admin = False
    # if User.NetID != None: 
    return render_template("AboutUsPage.html", admin=admin, user = user)
    # else: return redirect("/login")


@app.route("/login")
def login():
    try: user = session['NetID']
    except: user = None

    if(user == None): return render_template("LoginPage.html")
    else: return redirect("/")


@app.route("/authUser/<string:NetID>/<string:Password>", methods=['POST'])
def authUser(NetID, Password):
    try: user = session['NetID']
    except: user = None

    if user == None:
        try: 
            if(db_helper.checkAdminUser(NetID, Password) == True):
                session['NetID'] = NetID
                session['AdminUser'] = True
                result = {'success': True}
            elif(db_helper.checkRegisteredUser(NetID, Password) == True): 
                session['NetID'] = NetID
                session['AdminUser'] = False
                result = {'success': True}
            else: result = {'success': False}
        except Exception as e: 
            # print(e)
            result = {'success': False}
    else: result = {'success': True}
    return jsonify(result)


@app.route("/signUp/<string:NetID>/<string:Password>", methods=['POST', 'GET'])
def signUpUser(NetID, Password):
    try: user = session['NetID']
    except: user = None

    if user == None:
        try: 
            if(db_helper.checkAdminUser(NetID, Password) == True or db_helper.checkRegisteredUser(NetID, Password) == True): result = {'success': False, 'exist': True}
            db_helper.insert_new_RegisteredUser(NetID, Password)
            session['NetID'] = NetID
            session['AdminUser'] = False
            result = {'success': True, 'exist': False}
        except: result = {'success': False, 'exist': False}
    else: result = {'success': True, 'exist': False}
    return jsonify(result)
########################################################################################################################################################################################
@app.route("/admin/delete/A/<string:in_data>", methods=['POST'])
def deleteRegisteredUser(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.remove_RegisteredUser_by_NetID(str(in_data[7:-2]))
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/H/<string:in_data>", methods=['POST'])
def deleteProfessorImages(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.remove_ProfessorImages_by_Professor(str(in_data[7:-2]))
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/G/<string:in_data>", methods=['POST'])
def deleteAdminUser(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.remove_AdminUser_by_NetID(str(in_data[7:-2]))
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/B/<string:in_data>", methods=['POST'])
def deleteSearchHistory(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = (in_data[1:-1]).split("'B',")
        try:
            db_helper.remove_SearchHistory_entry(str(arr[1][2:-3]), int(arr[2][1:-2]), str(arr[3][2:-1]))
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/C/<string:in_data>", methods=['POST'])
def deleteCourseStats(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = (in_data[1:-1]).split("'C',")
        try:
            db_helper.remove_CourseStats_entry(arr[1][1:-2], arr[2][2:-3], arr[3][2:-3], arr[4][2:-1])
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/D/<string:in_data>", methods=['POST'])
def deleteCourseProperties(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = (in_data[1:-1]).split("'D',")
        try:
            db_helper.remove_CourseProperties_entry(int(arr[1][1:]))
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/E/<string:in_data>", methods=['POST'])
def deleteFeedback(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = (in_data[1:-1]).split("'E',")
        try:
            db_helper.remove_Feedback_entry(arr[1][2:-3], int(arr[3][1:-2]), arr[2][2:-3])
            result = {'success': True, 'response': 'Removed task'}
        except:
            result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/delete/F/<string:in_data>", methods=['POST'])
def deleteSchedule(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = (in_data[1:-1]).split("'F',")
        try:
            db_helper.remove_Schedule_entry(arr[1][2:-3], arr[2][2:-3], int(arr[3][1:-2]), int(arr[4][1:-2]), arr[5][2:-1])
            result = {'success': True, 'response': 'Removed task'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})
#################################################################################################################################################################


#################################################################################################################################################################
@app.route("/admin/edit/A/<string:in_data>/<string:Password>", methods=['POST'])
def updateRegisteredUser(in_data, Password):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.update_RegisteredUser(in_data[12:], Password)
            result = {'success': True, 'response': 'success Updated'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/G/<string:in_data>/<string:Password>", methods=['POST'])
def updateAdminUser(in_data, Password):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.update_AdminUser(in_data[12:], Password)
            result = {'success': True, 'response': 'success Updated'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/H/<string:in_data>/<string:URL>", methods=['POST'])
def updateProfessorImages(in_data, URL):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.update_ProfessorImages(in_data[12:], URL)
            result = {'success': True, 'response': 'success Updated'}
        except: result = {'success': False, 'response': 'Something went wrong'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/B/<string:in_data>/<int:CourseID>/<string:Professor>", methods=['POST'])
def updateSearchHistory(in_data, CourseID, Professor):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.update_SearchHistory(in_data[12:], int(CourseID), Professor)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/C/<string:in_data_0>/<string:in_data>", methods=['POST'])
def updateCourseStats(in_data_0, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = in_data.split('\'C\',')
        arr0 = (in_data_0[12:]).split(',')
        try:
            if(len(arr0) == 5): db_helper.update_CourseStats(int(arr0[0]), arr0[1], arr0[2], arr0[3]+','+arr0[4], int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]), int(arr[6]), int(arr[7]), int(arr[8]), int(arr[9]), int(arr[10]), int(arr[11]), int(arr[12]), int(arr[13]))
            elif(len(arr0) == 4): db_helper.update_CourseStats(int(arr0[0]), arr0[1], arr0[2], arr0[3], int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]), int(arr[6]), int(arr[7]), int(arr[8]), int(arr[9]), int(arr[10]), int(arr[11]), int(arr[12]), int(arr[13]))
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/D/<string:in_data_0>/<string:in_data>", methods=['POST'])
def updateCourseProperties(in_data_0, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = in_data.split('\'D\',')
        CourseID = ((in_data_0[12:]).split(' '))[0]
        try: 
            db_helper.update_CourseProperties(int(CourseID), arr[0], arr[1], arr[2], arr[3], arr[4], int(arr[5]), arr[6], arr[7])
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/E/<string:in_data_0>/<int:Rating>/<string:in_data>", methods=['POST'])
def updateFeedback(in_data_0, Rating, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = in_data.split('\'E\',')
        arr0 = (in_data_0[12:]).split(',')
        TimeStamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        try:
            if(len(arr0) == 3): db_helper.update_Feedback(arr0[0], int(arr0[1]), arr0[2], int(Rating), arr[0], arr[1], TimeStamp)
            elif(len(arr0) == 4): db_helper.update_Feedback(arr0[0], int(arr0[1]), arr0[2]+','+arr0[3], int(Rating), arr[0], arr[1], TimeStamp)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/edit/F/<string:in_data>/<string:SchoolYear>", methods=['POST'])
def updateSchedule(in_data, SchoolYear):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = (in_data[12:]).split(',')
        try:
            if(len(arr) == 5): db_helper.update_Schedule(arr[0], arr[2], int(arr[1]), arr[3], arr[4], SchoolYear)
            elif(len(arr) == 6): db_helper.update_Schedule(arr[0], arr[2]+','+arr[3], int(arr[1]), arr[4], arr[5], SchoolYear)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})
#################################################################################################################################################################


#################################################################################################################################################################
@app.route("/admin/create/A/<string:NetID>/<string:Password>", methods=['POST'])
def createRegisteredUser(NetID, Password):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.insert_new_RegisteredUser(NetID, Password)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/G/<string:NetID>/<string:Password>", methods=['POST'])
def createAdminUser(NetID, Password):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.insert_new_AdminUser(NetID, Password)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/H/<string:Professor>/<string:URL>", methods=['POST'])
def createProfessorImages(Professor, URL):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.insert_new_ProfessorImages(Professor, URL)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/B/<string:NetID>/<int:CourseID>/<string:Professor>", methods=['POST'])
def createSearchHistory(NetID, CourseID, Professor):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.insert_new_SearchHistory(NetID, int(CourseID), Professor)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/C/<int:CourseID>/<string:Year>/<string:Term>/<string:Professor>/<string:in_data>", methods=['POST'])
def createCourseStats(CourseID, Year, Term, Professor, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = in_data.split('\'C\',')
        try: 
            db_helper.insert_new_CourseStats(int(CourseID), Year, Term, Professor, int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]), int(arr[6]), int(arr[7]), int(arr[8]), int(arr[9]), int(arr[10]), int(arr[11]), int(arr[12]), int(arr[13]))
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/D/<int:CourseID>/<string:CourseTitle>/<int:CourseNumber>/<string:Subject>/<string:in_data>", methods=['POST'])
def createCourseProperties(CourseID, CourseTitle, CourseNumber, Subject, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = in_data.split('\'D\',')
        try: 
            db_helper.insert_new_CourseProperties(int(CourseID), CourseTitle, arr[0], arr[1], arr[2], arr[3], int(CourseNumber), arr[4], Subject)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/E/<string:NetID>/<int:CourseID>/<string:Professor>/<int:Rating>/<string:in_data>", methods=['POST'])
def createFeedback(NetID, CourseID, Professor, Rating, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        arr = in_data.split('\'E\',')
        TimeStamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        try:
            db_helper.insert_new_Feedback(NetID, int(CourseID), Professor, int(Rating), arr[0], arr[1], TimeStamp)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})


@app.route("/admin/create/F/<string:NetID>/<string:Professor>/<int:CourseID>/<string:Year>/<string:Term>/<string:SchoolYear>", methods=['POST'])
def createSchedule(NetID, Professor, CourseID, Year, Term, SchoolYear):
    try: user = session['NetID']
    except: user = None

    if user != None and session['AdminUser'] == True:
        try:
            db_helper.insert_new_Schedule(NetID, Professor, int(CourseID), Year, Term, SchoolYear)
            result = {'success': True, 'response': 'Done'}
        except: result = {'fail': False, 'response': 'Done'}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong'})
###############################################################################################################################################################################################################


###############################################################################################################################################################################################################
@app.route("/admin/Schedule/<string:in_data>")
def Schedulepage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_Schedule(int(in_data))
            except: items = db_helper.fetch_Schedule(-1)
            return render_template("Schedule.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/RegisteredUser/<string:in_data>")
def RegisteredUserpage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_RegisteredUser(int(in_data))
            except: items = db_helper.fetch_RegisteredUser(-1)
            return render_template("RegisteredUser.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/AdminUser/<string:in_data>")
def AdminUserpage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_AdminUser(int(in_data))
            except: items = db_helper.fetch_AdminUser(-1)
            return render_template("AdminUser.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/ProfessorImages/<string:in_data>")
def ProfessorImagespage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_ProfessorImages(int(in_data))
            except: items = db_helper.fetch_ProfessorImages(-1)
            return render_template("ProfessorImages.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/Feedback/<string:in_data>")
def Feedbackpage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_Feedback(int(in_data))
            except: items = db_helper.fetch_Feedback(-1)
            return render_template("Feedback.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/CourseStats/<string:in_data>")
def CourseStatspage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_CourseStats(int(in_data))
            except: items = db_helper.fetch_CourseStats(-1)
            return render_template("CourseStats.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/CourseProperties/<string:in_data>")
def CoursePropertiespage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_CourseProperties(int(in_data))
            except: items = db_helper.fetch_CourseProperties(-1)
            return render_template("CourseProperties.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


@app.route("/admin/SearchHistory/<string:in_data>")
def SearchHistorypage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try: items = db_helper.fetch_SearchHistory(int(in_data))
            except: items = db_helper.fetch_SearchHistory(-1)
            return render_template("SearchHistory.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")
########################################################################################################################################################################################


########################################################################################################################################################################################
@app.route("/admin", methods=['GET'])
def adminpage(): 
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True: return render_template("Admin.html", user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/")
def indexpage():
    try: 
        user = session['NetID']
        admin = session['AdminUser']
    except: 
        user = None
        admin = False
    # time.sleep(0.6)
    # if User.NetID != None: 
    return render_template("Index.html", admin=admin, user=user)
    # else: return redirect("/login")

@app.route("/genedselectorpage")
def genedselectorpage():
    try: 
        user = session['NetID']
        admin = session['AdminUser']
    except: 
        user = None
        admin = False
    # if User.NetID != None: 
    return render_template("GenEdSelector.html", admin=admin, user=user)
    # else: return redirect("/login")
#######################################################################################################


################################################################
#                     MAIN SEARCHES                           #
################################################################
@app.route("/search/<string:in_data>/<string:limit>")
def UserSearch(in_data, limit):
    # if User.NetID != None:
    in_data = in_data.upper()

    try: limit = int(limit)
    except: limit = 10

    if(in_data != 'IDK'):
        try:
            arr = in_data.split(' ')
            subjects = db_helper.get_subjects_from_CourseProperties()

            professor = ''
            subject  = None
            courseNumber = None

            for word in arr:
                if(word != ''):
                    word = word.replace(" ", "")
                    if(word in subjects): subject = word
                    else:
                        try: 
                            courseNumber = int(word)
                        except: 
                            if(professor == ''): professor += word
                            else: professor += ' ' + word

            if(professor != '' and subject != None and courseNumber != None): items = db_helper.rank_by_professor_subject_courseNumber(professor, subject, courseNumber, limit)
            elif(professor != '' and subject != None): items = db_helper.rank_by_professor_subject(professor, subject, limit)
            elif(professor != '' and courseNumber != None): items = db_helper.rank_by_professor_courseNumber(professor, courseNumber, limit)
            elif(subject != None and courseNumber != None): items = db_helper.rank_by_subject_courseNumber(subject, courseNumber, limit)
            elif(professor != ''): items = db_helper.rank_by_professor(professor, limit)
            elif(subject != None): items = db_helper.rank_by_subject(subject, limit)
            else: items = db_helper.rank_by_courseNumber(courseNumber, limit)

        except: items = []

    else: 
        try: items = db_helper.rank_by_nothing(limit)
        except: items = []
    
    try:
        user = session['NetID']
        admin = session['AdminUser']
    except:
        user = None
        admin = False
    return render_template("SearchPage.html", items=items, admin=admin, user=user)
    # else: return redirect("/login")


@app.route("/search/professorPage/<string:Professor>/<string:Subject>/<int:CourseNumber>")
def ProfessorSearch(Professor, Subject, CourseNumber):
    # if User.NetID != None:
    try: item = (db_helper.rank_by_professor_subject_courseNumber(Professor, Subject, CourseNumber, 1))[0]
    except: item = {"AP":0, "A":0, "AM":0, "BP":0, "B":0, "BM":0, "CP":0,"C":0,"CM":0,"DP":0,"D":0,"DM":0,"F":0,"W":0, "GPA":0}

    try: CourseProperties = (db_helper.search_CourseProperties_by_course(Subject, CourseNumber))[0]
    except: CourseProperties = {'CourseID':0, 'CourseDescription':'N/A', 'CourseTitle':'N/A'}

    try: src = (db_helper.search_ProfessorImages_by_Professor(Professor))[0]['URL']
    except: src = None

    if src == None:
        # flag = False
        # User.driver.get("https://www.google.com/search?q=uiuc+"+Professor+"&tbm=isch")
        # for v in User.driver.find_elements_by_tag_name('img'):
        #     if(v.get_attribute('class') == 'rg_i Q4LuWd'):
        #         src = v.get_attribute("src")
        #         try: db_helper.insert_new_ProfessorImages(Professor, src)
        #         except: pass
        #         break
        if src == None: src = "https://spracklinchiro.com/wp-content/uploads/2020/03/shutterstock_149293433.jpg"
    
    try:
        user = session['NetID']
        admin = session['AdminUser']
    except:
        user = None
        admin = False

    try: db_helper.insert_new_SearchHistory(str(user), int(CourseProperties['CourseID']), str(Professor))
    except: pass

    try: 
        Feedbacks=db_helper.search_Feedback_by_professor_and_course(Professor, int(CourseProperties['CourseID']))
        for feedback in Feedbacks:
            try: feedback['TimeConsumption'] = int(feedback['TimeConsumption'])
            except: feedback['TimeConsumption'] = None
    except: Feedbacks= [{"NetID":"N/A", "Rating":0, "TimeConsumption":0, "Comment":"N/A"}]

    avgRatings= 0
    avgTimeConsumption = 0
    count = 0

    for feedback in Feedbacks:
        try:
            avgRatings += int(feedback['Rating'])
            avgTimeConsumption += int(feedback['TimeConsumption'])
            count += 1
        except: continue
    
    if(count != 0):
        avgRatings /= count
        avgRatings=round(avgRatings,2)
        avgTimeConsumption /= count
        avgTimeConsumption=round(avgTimeConsumption,2)
    else:
        avgRatings = None
        avgTimeConsumption = None
 
    try:
        PercentOfAs = (item['AP'] + item['A'] + item['AM'])*100/(item['AP'] + item['A'] + item['AM'] + item['BP'] + item['B'] + item['BM'] + item['CP'] + item['C'] + item['CM'] + item['DP'] + item['D'] + item['DM'] + item['F'])
        MaxGradeLetterCount = max(item['AP'], item['A'], item['AM'], item['BP'], item['B'], item['BM'], item['CP'], item['C'], item['CM'], item['DP'], item['D'], item['DM'], item['F'])
    except:
        PercentOfAs = None
        MaxGradeLetterCount = None
    return render_template("ProfessorPage.html", PercentOfAs = round(PercentOfAs, 2), MaxGradeLetterCount=MaxGradeLetterCount, item=item, user=user, admin=admin, Professor=Professor, Subject=Subject, CourseNumber=str(CourseNumber), CourseDescription=CourseProperties['CourseDescription'], CourseTitle=CourseProperties['CourseTitle'], Image=src, Feedbacks=Feedbacks, avgTimeConsumption=avgTimeConsumption, avgRatings=avgRatings, feedbackCount=count)
    # else: return redirect("/login")

@app.route("/genEdResults/<string:in_data>")
def genEdSearch(in_data):
    try:
        user = session['NetID']
        admin = session['AdminUser']
    except:
        user = None
        admin = False
    
    # print(in_data)

    try:
        arr = in_data.split(';')
        
        # print(arr)
        tags = arr[0]
        tags = tags.replace("(Western-Comparative)", "(Western/Comparative)")
        yearFlag = int(arr[1])
        covidFlag = int(arr[2])
        gpaFlag = int(arr[3])
        ratingFlag = int(arr[4])
        workFlag = int(arr[5])
        gpaThreshold = float(arr[6])
        yearThreshold = int(arr[7])
        ratingThreshold = float(arr[8])
        workThreshold = int(arr[9])

        items = db_helper.fetch_storedProcedure(tags, yearFlag, covidFlag, gpaFlag, ratingFlag, workFlag, gpaThreshold, yearThreshold, ratingThreshold, workThreshold)
        # print("ran query")
    except Exception as e: 
        # print(e)
        items = []

    return render_template("GenEdResults.html", items=items, admin=admin, user=user)
#######################################################################################################


################################################################
#                     TABLE SEARCHES                           #
################################################################
@app.route("/admin/CourseProperties/search/<string:in_data>")
def SearchCoursePropertiespage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try:
                arr = in_data.split(' ')
                items = db_helper.search_CourseProperties_by_course(arr[0], int(arr[1]))
            except: items = []
            return render_template("CourseProperties.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/SearchHistory/search/<string:in_data>")
def SearchSearchHistorypage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try:
                arr = in_data.split(' ')
                if(len(arr) == 2): items = db_helper.search_SearchHistory_by_professor_and_course(arr[0], int(arr[1]))
                elif(len(arr) == 3): items = db_helper.search_SearchHistory_by_professor_and_course(arr[0] + " " + arr[1], int(arr[2]))
                elif(len(arr) == 4): items = db_helper.search_SearchHistory_by_professor_and_course(arr[0] + " " + arr[1] + " " + arr[2], int(arr[3]))
                else: items = []
            except:
                items = []
            return render_template("SearchHistory.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/RegisteredUser/search/<string:NetID>")
def SearchRegisteredUserpage(NetID):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.search_RegisteredUser_by_netid(NetID)
            return render_template("RegisteredUser.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/AdminUser/search/<string:NetID>")
def SearchAdminUserpage(NetID):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.search_AdminUser_by_netid(NetID)
            return render_template("AdminUser.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/ProfessorImages/search/<string:Professor>")
def SearchProfessorImagespage(Professor):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.search_ProfessorImages_by_Professor(Professor)
            return render_template("ProfessorImages.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/CourseStats/search/<string:in_data>")
def SearchCourseStatspage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            try:
                arr = in_data.split(' ')
                items = db_helper.search_CourseStats_by_course_and_year(int(arr[0]), arr[1])
            except: items = []
            return render_template("CourseStats.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/Feedback/search/<string:in_data>")
def SearchFeedbackpage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.search_Feedback_by_professor(in_data)
            return render_template("Feedback.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/Schedule/search/<string:in_data>")
def SearchSchedulepage(in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.search_Schedule_by_netid(in_data)
            return render_template("Schedule.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")


################################################################
#                   ADVANCED QUERIES                           #
################################################################
@app.route("/admin/runPratikQuery")
def pratikQueryPage():
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.advance_pratik_query()
            return render_template("PratikOutput.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/runDimitarQuery")
def dimitarQueryPage():
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.advance_dimitar_query()
            return render_template("DimitarOutput.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/runMichaelQuery")
def michaelQueryPage():
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.advance_michael_query()
            return render_template("MichaelOutput.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

@app.route("/admin/runOmarQuery")
def omarQueryPage():
    try: user = session['NetID']
    except: user = None

    if user != None:
        if session['AdminUser'] == True:
            items = db_helper.advance_omar_query()
            return render_template("OmarOutput.html", items=items, user=user)
        else: return redirect("/")
    else: return redirect("/login")

##############################################################
#                   RATE PAGE                                #
##############################################################
@app.route("/rate")
def rateFormPage():
    try:
        user = session['NetID']
        admin = session['AdminUser']
    except:
        user = None
        admin = False

    if user != None: 
        try: Professors = db_helper.getProfessors()
        except: Professors = []
        return render_template("RatePage.html", admin=admin, Professors=Professors, Professor="", Subject="", CourseNumber="", user=user)
    else: return redirect("/login")


@app.route("/rate/<string:Professor>/<string:in_data>")
def rateFormPageFilled(Professor, in_data):
    try: user = session['NetID']
    except: user = None

    if user != None:
        arr = in_data.split(" ")
        try: CourseNumber = int(arr[1])
        except: CourseNumber = None
        try: Professors = db_helper.getProfessors()
        except: Professors = []
        return render_template("RatePage.html", admin=session['AdminUser'], Professors=Professors, Professor=Professor, Subject=arr[0], CourseNumber=CourseNumber, user=user)
    else: return redirect("/login")


@app.route("/rate/<string:Professor>/<string:Subject>/<int:CourseNumber>/<int:Rating>/<int:TimeConsumption>/<string:Comment>", methods=['POST'])
def userFeedback(Professor, Subject, CourseNumber, Rating, TimeConsumption, Comment):
    try: user = session['NetID']
    except: user = None

    if user != None and 0 <= Rating and Rating <= 10 and 0 <= TimeConsumption and TimeConsumption <= 40 and len(Comment) <= 500:
        try:
            CourseID = int((db_helper.search_CourseProperties_by_course(Subject, CourseNumber))[0]['CourseID'])
            if(db_helper.assertProfessor(Professor, CourseID)):
                TimeStamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                try:
                    db_helper.insert_new_Feedback(user, CourseID, Professor, int(Rating), str(TimeConsumption), Comment, TimeStamp)
                    result = {'success': True, 'response': 'Done', 'update': False}
                except:
                    db_helper.update_Feedback(user, CourseID, Professor, int(Rating), str(TimeConsumption), Comment, TimeStamp)
                    result = {'success': True, 'response': 'Done', 'update': True}
            else: result = {'success': False, 'response': 'Something went wrong', 'update': False}
        except: result = {'success': False, 'response': 'Something went wrong', 'update': False}
        return jsonify(result)
    else: return jsonify({'success': False, 'response': 'Something went wrong', 'update': False})


def cleanup():
    # print("Cleaning Up Please Wait!")
    # try: User.driver.quit()
    # except: print("Failed to quit the selenium webdriver!")
    print("Done Cleaning Up!")
atexit.register(cleanup)
