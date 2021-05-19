$('.remove').click(function () 
{
    const remove = $(this);
    const index = (remove.data('source'))[2];

    $.ajax
    ({
        type: 'POST',
        url: '/admin/delete/' + index + '/' + remove.data('source'),
        success: function (res)
        {
            console.log(res.response)
            location.reload();
        },
        error: function ()
        { 
            console.log('Error');
        }
    });
});

$('#submit-rating').click(function () 
{
    var Professor = document.getElementById("professor-field").value;
    var Subject = document.getElementById("course-field").value;
    var CourseNumber = document.getElementById("courseNum-field").value;
    var Rating = document.getElementById("ratingRangeRATEPAGE").value;
    var TimeConsumption = document.getElementById("hourRange").value;
    var Comment = document.getElementById("comment-field").value;
    
    // document.getElementById("liveToast").show();

    // $("#response").text("");
    if(":" + Professor + ":" != "::" && ":" + Subject + ":" != "::"  && ":" + CourseNumber + ":" != "::" && ":" + Rating + ":" != "::" && ":" + TimeConsumption + ":" != "::" && ":" + Comment + ":" != "::")
    {
        $.ajax
        ({
            type: 'POST',
            url: '/rate/' + Professor + '/' + Subject + '/' + CourseNumber + '/' + Rating + '/' + TimeConsumption + '/' + Comment,
            success: function (res)
            {
                if(res.success && res.update)
                {
                    $("#response").text("Your Response Has Been Updated!");
                    $("#response-bg").css("background-color", "blue");
                    $('.toast').toast('show');
                }
                else if(res.success)
                {
                    $("#response").text("Your Response Has Been Recorded!");
                    $("#response-bg").css("background-color", "green");
                    $('.toast').toast('show');
                }
                else
                {
                    $("#response").text("Your Response Has Failed To Process!");
                    $("#response-bg").css("background-color", "red");
                    $('.toast').toast('show');
                }
            },
            error: function ()
            {
                $("#response").text("Your Response Has Failed To Process!");
                $("#response-bg").css("background-color", "red");
                $('.toast').toast('show');
            }
        });
    }
    else
    {
        $("#response").text("Please Fill Out All Fields!");
        $("#response-bg").css("background-color", "orange");
        $('.toast').toast('show');
    }
    
    return false;
});

$('#submit-RegisteredUser').click(function () 
{
    var Password = document.getElementById("password-form-display").value;
    var title = document.getElementById("LabelX").innerHTML;

    if(title == "New Entry: ")
    {
        var NetID = document.getElementById("netid-form-display").value;
        $.ajax({
            type: 'POST',
            url: '/admin/create/A/' + NetID + '/' + Password,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/A/' + title + '/' + Password,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#rate-professor').click(function () 
{
    var Professor = document.getElementById("professor-name").innerHTML;
    var Course = document.getElementById("course-subject-number").innerHTML;

    if(":" + Professor + ":" != "::" && ":" + Course + ":" != "::")
    {
        document.location.href = "../../../../rate/" + Professor + "/" + Course;
    }
});

$('#continueBtn').click(function () 
{
    document.location.href = "/..";
});

$('#submit-AdminUser').click(function () 
{
    var Password = document.getElementById("password-form-display").value;
    var title = document.getElementById("LabelX").innerHTML;

    if(title == "New Entry: ")
    {
        var NetID = document.getElementById("netid-form-display").value;
        $.ajax({
            type: 'POST',
            url: '/admin/create/G/' + NetID + '/' + Password,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/G/' + title + '/' + Password,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#submit-ProfessorImages').click(function () 
{
    var URL = document.getElementById("password-form-display").value;
    var title = document.getElementById("LabelX").innerHTML;
    console.log(URL)

    if(title == "New Entry: ")
    {
        var Professor = document.getElementById("netid-form-display").value;
        $.ajax({
            type: 'POST',
            url: '/admin/create/H/' + Professor + '/' + URL,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/H/' + title + '/' + URL,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#submit-CourseProperties').click(function () 
{
    var title = document.getElementById("Label").innerHTML;
    var CourseTitle = document.getElementById("CourseTitle-form-display").value;
    var CourseDescription = document.getElementById("CourseDescription-form-display").value;
    var Prerequisites = document.getElementById("Prerequisites-form-display").value;
    var LinkedSections = document.getElementById("LinkedSections-form-display").value;
    var CourseWebsiteLink = document.getElementById("CourseWebsiteLink-form-display").value;
    var CourseNumber = document.getElementById("CourseNumber-form-display").value;
    var CourseTag = document.getElementById("CourseTag-form-display").value;
    var Subject = document.getElementById("Subject-form-display").value;

    if(title == "New Entry: ")
    {
        var CourseID = document.getElementById("CourseID-form-display").value;
        $.ajax({
            type: 'POST',
            url: '/admin/create/D/' + CourseID + '/' + CourseTitle + '/' + CourseNumber + '/' + Subject + '/' + CourseDescription + '\'D\',' + Prerequisites + '\'D\',' + LinkedSections + '\'D\',' + CourseWebsiteLink + '\'D\',' + CourseTag,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/D/' + title + '/' + CourseTitle + '\'D\',' + CourseDescription + '\'D\',' + Prerequisites + '\'D\',' + LinkedSections + '\'D\',' + CourseWebsiteLink + '\'D\',' + CourseNumber + '\'D\',' + CourseTag + '\'D\',' + Subject,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#submit-Schedule').click(function () 
{
    var title = document.getElementById("Label").innerHTML;
    var SchoolYear = document.getElementById("SchoolYear-form-display").value;

    if(title == "New Entry: ")
    {
        var NetID = document.getElementById("NetID-form-display").value;
        var Professor = document.getElementById("Professor-form-display").value;
        var CourseID = document.getElementById("CourseID-form-display").value;
        var Year = document.getElementById("Year-form-display").value;
        var Term = document.getElementById("Term-form-display").value;

        $.ajax({
            type: 'POST',
            url: '/admin/create/F/' + NetID + '/' + Professor + '/' + CourseID + '/' + Year + '/' + Term + '/' + SchoolYear,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/F/' + title + '/' + SchoolYear,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#submit-SearchHistory').click(function () 
{
    var title = document.getElementById("Label").innerHTML;
    var CourseID = document.getElementById("CourseID-form-display").value;
    var Professor = document.getElementById("Professor-form-display").value;

    if(title == "New Entry: ")
    {
        var NetID = document.getElementById("NetID-form-display").value;
        $.ajax({
            type: 'POST',
            url: '/admin/create/B/' + NetID + '/' + CourseID + '/' + Professor,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/B/' + title + '/' + CourseID + '/' + Professor,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#submit-Feedback').click(function () 
{
    var title = document.getElementById("Label").innerHTML;
    var Rating = document.getElementById("Rating-form-display").value;
    var TimeConsumption = document.getElementById("TimeConsumption-form-display").value;
    var Comment = document.getElementById("Comment-form-display").value;

    if(title == "New Entry: ")
    {
        var title = document.getElementById("Label").innerHTML;
        var CourseID = document.getElementById("CourseID-form-display").value;
        var NetID = document.getElementById("NetID-form-display").value;
        var Professor = document.getElementById("Professor-form-display").value;
        
        $.ajax({
            type: 'POST',
            url: '/admin/create/E/' + NetID + '/' + CourseID + '/' + Professor + '/' + Rating + '/' + TimeConsumption + '\'E\',' + Comment,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/E/' + title + '/' + Rating + '/' + TimeConsumption + '\'E\',' + Comment,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#submit-CourseStats').click(function () 
{
    var title = document.getElementById("Label").innerHTML;
    var AP = document.getElementById("AP-form-display").value;
    var A = document.getElementById("A-form-display").value;
    var AM = document.getElementById("AM-form-display").value;
    var BP = document.getElementById("BP-form-display").value;
    var B = document.getElementById("B-form-display").value;
    var BM = document.getElementById("BM-form-display").value;
    var CP = document.getElementById("CP-form-display").value;
    var C = document.getElementById("C-form-display").value;
    var CM = document.getElementById("CM-form-display").value;
    var DP = document.getElementById("DP-form-display").value;
    var D = document.getElementById("D-form-display").value;
    var DM = document.getElementById("DM-form-display").value;
    var F = document.getElementById("F-form-display").value;
    var W = document.getElementById("W-form-display").value;

    if(title == "New Entry: ")
    {
        var CourseID = document.getElementById("CourseID-form-display").value;
        var Year = document.getElementById("Year-form-display").value;
        var Term = document.getElementById("Term-form-display").value;
        var Professor = document.getElementById("Professor-form-display").value;

        $.ajax({
            type: 'POST',
            url: '/admin/create/C/' + CourseID + '/' + Year + '/' + Term + '/' + Professor + '/' + AP + '\'C\',' + A + '\'C\',' + AM + '\'C\',' + BP + '\'C\',' + B + '\'C\',' + BM + '\'C\',' + CP + '\'C\',' + C + '\'C\',' + CM + '\'C\',' + DP + '\'C\',' + D + '\'C\',' + DM + '\'C\',' + F + '\'C\',' + W,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/admin/edit/C/' + title + '/' + AP + '\'C\',' + A + '\'C\',' + AM + '\'C\',' + BP + '\'C\',' + B + '\'C\',' + BM + '\'C\',' + CP + '\'C\',' + C + '\'C\',' + CM + '\'C\',' + DP + '\'C\',' + D + '\'C\',' + DM + '\'C\',' + F + '\'C\',' + W,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#user-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    }
});

$('#limitBtn').click(function () 
{
    var limit = document.getElementById("mySearch").value;
    document.location.href = limit
});

//search
$('#CoursePropertiesSearchBtn').click(function () 
{
    //ignore this for now. This filters without a db query
    // input = input.split(' ')
    // console.log(input)
    // $('.table-row').each(function () {
    //     var isSubject = false
    //     var isNumber = false
    //     $(this).children().each(function () {
    //         console.log($(this).text())
    //         if($(this).text() === input[0]) {
    //             isSubject = true
    //         }
    //         if($(this).text() === input[1]) {
    //             isNumber = true
    //         }
    //     })

    //     if (isSubject && isNumber) {
    //         $(this).show()
    //     } else {
    //         $(this).hide()
    //     }
    // });
    //This is if a database query is preferred.
    var input = document.getElementById("customSearch").value;
    //console.log(input)
    //console.log(document.location.href)
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/CourseProperties/search/" + input;
    }
});

$('#SearchHistorySearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/SearchHistory/search/" + input;
    }
});

$('#RegisteredUserSearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/RegisteredUser/search/" + input;
    }
});

$('#AdminUserSearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/AdminUser/search/" + input;
    }
});

$('#ProfessorImagesSearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/ProfessorImages/search/" + input;
    }
});

$('#CourseStatsSearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/CourseStats/search/" + input;
    }
});

$('#FeedbackSearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/Feedback/search/" + input;
    }
});

$('#ScheduleSearchBtn').click(function () 
{
    var input = document.getElementById("customSearch").value;
    if(":" + input + ":" != "::")
    {
        document.location.href = "/admin/Schedule/search/" + input;
    }
});

//Modal stuff
$('#user-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        //var b = a.replace(/[\s\{]']|'[:\},]/g, "\"");

        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];

        keys.push(obj["NetID"])
        fields.push(obj["Password"])
        
        modal.find('.modal-title').text('Edit Entry: ' + keys.toString());
        $('.primary-key').hide()
    }

    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }
    
    
    

    // if (NetID === 'New User') {
    //     modal.find('.modal-title').text(NetID)
    //     $('#netid-form-display').removeAttr('NetID')
    // } else {
    //     modal.find('.modal-title').text('Edit User ' + NetID)
    //     $('#netid-form-display').attr('NetID', NetID)
    // }

    // if (content) {
    //     modal.find('.form-control').val(content);
    // } else {
    //     modal.find('.form-control').val('');
    // }
});

$('#professorimages-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        //var b = a.replace(/[\s\{]']|'[:\},]/g, "\"");

        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];

        keys.push(obj["Professor"])
        fields.push(obj["URL"])
        
        modal.find('.modal-title').text('Edit Entry: ' + keys.toString());
        $('.primary-key').hide()
    }

    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }
    
    
    

    // if (NetID === 'New User') {
    //     modal.find('.modal-title').text(NetID)
    //     $('#netid-form-display').removeAttr('NetID')
    // } else {
    //     modal.find('.modal-title').text('Edit User ' + NetID)
    //     $('#netid-form-display').attr('NetID', NetID)
    // }

    // if (content) {
    //     modal.find('.form-control').val(content);
    // } else {
    //     modal.find('.form-control').val('');
    // }
});

$('#CourseProperties-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];
        keys.push(obj["CourseID"])
        fields.push(obj["CourseTitle"])
        fields.push(obj["CourseDescription"])
        fields.push(obj["Prerequisites"])
        fields.push(obj["LinkedSections"])
        fields.push(obj["CourseWebsiteLink"])
        fields.push(obj["CourseNumber"])
        fields.push(obj["CourseTag"])
        fields.push(obj["Subject"])

        modal.find('.modal-title').text('Edit Entry: ' + keys.toString() + '  (' + obj["CourseTitle"] + ')');
        $('.primary-key').hide()
    }
    
    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }

        
});

$('#CourseStats-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];
        keys.push(obj["CourseID"])
        keys.push(obj["Year"])
        keys.push(obj["Term"])
        keys.push(obj["Professor"])
        fields.push(obj["AP"])
        fields.push(obj["A"])
        fields.push(obj["AM"])
        fields.push(obj["BP"])
        fields.push(obj["B"])
        fields.push(obj["BM"])
        fields.push(obj["CP"])
        fields.push(obj["C"])
        fields.push(obj["CM"])
        fields.push(obj["DP"])
        fields.push(obj["D"])
        fields.push(obj["DM"])
        fields.push(obj["F"])
        fields.push(obj["W"])

        modal.find('.modal-title').text('Edit Entry: ' + keys.toString());
        $('.primary-key').hide()
    }
    
    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }
  
});

$('#Feedback-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];
        keys.push(obj["NetID"])
        keys.push(obj["CourseID"])
        keys.push(obj["Professor"])
        fields.push(obj["Rating"])
        fields.push(obj["TimeConsumption"])
        fields.push(obj["Comment"])
        //fields.push(obj["TimeStamp"]) note that this should be auto generated

        modal.find('.modal-title').text('Edit Entry: ' + keys.toString());
        $('.primary-key').hide()
    }
    
    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }
  
});

$('#Schedule-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];
        keys.push(obj["NetID"])
        keys.push(obj["CourseID"])
        keys.push(obj["Professor"])
        keys.push(obj["Year"])
        keys.push(obj["Term"])
        fields.push(obj["SchoolYear"])

        modal.find('.modal-title').text('Edit Entry: ' + keys.toString());
        $('.primary-key').hide()
    }
    
    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }
  
});

$('#SearchHistory-modal').on('show.bs.modal', function (event) 
{
    const button = $(event.relatedTarget) // Button that triggered the modal
    const isEdit = button.attr("class").includes("edit");
    const isAdd = button.attr("class").includes("add");
    const modal = $(this)

    if(isEdit) {
        const table = button.data('source') // Extract table name
        var content = button.data('content').replace(/\{'/g, '\{\"').replace(/None/g, '""') // Extract column values from row
        content = content.replace(/\s'/g, ' \"')
        content = content.replace(/':/g, '\":')
        content = content.replace(/'\}/g, '\"\}')
        content = content.replace(/',/g, '\",')
        var obj = JSON.parse(content); //convert values to object
        var keys = [];
        var fields = [];
        keys.push(obj["NetID"])
        fields.push(obj["CourseID"])
        fields.push(obj["Professor"])

        modal.find('.modal-title').text('Edit Entry: ' + keys.toString());
        $('.primary-key').hide()
    }
    
    if(isAdd) {
        modal.find('.modal-title').text('New Entry: ');
        $('.primary-key').show()
    }
  
});

$('#createAccountBtn').click(function () 
{
    document.location.href = "../signup";
    return false;
});

$('#loginBtn').click(function () 
{
    window.location.href = "../login";
    return false;
});
    
$('#main-search-button').click(function ()
{
    var searchKey = document.getElementById("main-input").value;
    if(":" + searchKey + ":" != "::")
    {
        document.location.href = "search/" + searchKey + "/10";
    }
    else
    {
        window.location.href = "search/IDK/10";
    }
});

$('#findCourseBtn').click(function ()
{
    let params = ""
    let tags = "" //gened tags
    if($('#flexRadioAdvComp').is(':checked')) {
        tags += "Advanced Composition,"
    }
    if($('#flexRadioWesternComp').is(':checked')) {
        tags += "Cultural Studies (Western-Comparative),"
    }
    if($('#flexRadioUsMin').is(':checked')) {
        tags += "Cultural Studies (US Minority),"
    }
    if($('#flexRadioNonWest').is(':checked')) {
        tags += "Cultural Studies (Non-Western),"
    }
    if($('#flexRadioHisPhil').is(':checked')) {
        tags += "Humanities & the Arts (Historical and Philosophical Perspectives),"
    }
    if($('#flexRadioLitArts').is(':checked')) {
        tags += "Humanities & the Arts (Literature and the Arts),"
    }
    if($('#flexRadioLifeSci').is(':checked')) {
        tags += "Natural Sciences & Technology (Life Sciences),"
    }
    if($('#flexRadioPhySci').is(':checked')) {
        tags += "Natural Sciences & Technology (Physical Sciences),"
    }
    if($('#flexRadioQuant1').is(':checked')) {
        tags += "Quantitative Reasoning 1,"
    }
    if($('#flexRadioQuant2').is(':checked')) {
        tags += "Quantitative Reasoning 2,"
    }
    if($('#flexRadioBehSci').is(':checked')) {
        tags += "Social & Behavioral Sciences (Behavioral Sciences),"
    }
    if($('#flexRadioSocSci').is(':checked')) {
        tags += "Social & Behavioral Sciences (Social Sciences),"
    }
    params += tags + ";"

    if($('#flexRadioDefault9').is(':checked')) { //yearFlag
        params += "1;"
    } else {
        params += "0;" 
    }

    if($('#flexRadioDefault10').is(':checked')) { //covidFlag
        params += "1;"
    } else {
        params += "0;" 
    }

    if($('#flexRadioDefault8').is(':checked')) { //gpaFlag
        params += "1;"
    } else {
        params += "0;" 
    }

    if($('#flexRadioDefault11').is(':checked')) { //ratingFlag
        params += "1;"
    } else {
        params += "0;" 
    }

    if($('#flexRadioDefault12').is(':checked')) { //work hours Flag
        params += "1;"
    } else {
        params += "0;" 
    }
    // alert(tags);
    params += $("#gpaValue").html() + ";"
    params += $("#yearValue").html() + ";"
    params += $("#ratingValue").html() + ";"
    params += $("#timeValue").html()
    document.location.href = "/genEdResults/" + params
})

$(function() {
    $("#genEdForm").submit(function() { return false; });
});

$('#signInBtn').click(function () 
{
    var NetID = document.getElementById("inputNetID").value;
    var Password = document.getElementById("inputPassword").value;

    if(":" + NetID + ":" != "::" && ":" + Password + ":" != "::")
    {
        $.ajax
        ({
            type: 'POST',
            url: '/authUser/' + NetID + "/" + Password,
            success: function (res) 
            {
                if(res.success == false)
                {
                    $("#response").text("Log In Failed! Try Again!");
                    $("#response-bg").css("background-color", "red");
                    $('.toast').toast('show');
                }
                else
                {
                    $("#response").text("");
                    document.location.href = ".."; 
                    return false;
                }
            }
        });

        return false;
    }
    else
    {        
        $("#response").text("Please Enter All Fields!");
        $("#response-bg").css("background-color", "orange");
        $('.toast').toast('show');
    }
});

$('#signUpBtn').click(function () 
{
    var NetID = document.getElementById("inputNetID").value;
    var Password = document.getElementById("inputPassword").value;

    if(":" + NetID + ":" != "::" && ":" + Password + ":" != "::")
    {
        $.ajax
        ({
            type: 'POST',
            url: '/signUp/' + NetID + "/" + Password,
            success: function (res) 
            {
                if(res.success)
                {
                    $("#response").text("Sign Up Successful!");
                    $("#response-bg").css("background-color", "green");
                    $('.toast').toast('show');
                    window.location.href = "..";
                    return false;
                }
                else if(res.exist)
                {
                    $("#response").text("User Already Exists!");
                    $("#response-bg").css("background-color", "red");
                    $('.toast').toast('show');
                }
            },
            error: function ()
            { 
                $("#response").text("User Already Exists!");
                $("#response-bg").css("background-color", "red");
                $('.toast').toast('show');
            }
        });

        $("#response").text("User Already Exists!");
        $("#response-bg").css("background-color", "red");
        $('.toast').toast('show');        
        // window.location.href = "..";
        return false;
    }
    else
    {
        $("#response").text("Please Enter All Fields!");
        $("#response-bg").css("background-color", "orange");
        $('.toast').toast('show');
    }
});

//misc

//gened selector options
$('#flexRadioDefault8').click(function() {
    if( $(this).is(':checked')) {
        $("#gpaSlider").show();
        $("#yearCol").show();
    } else {
        $("#gpaSlider").hide();
        $("#yearCol").hide();
    }
});

$('#flexRadioDefault9').click(function() {
    if( $(this).is(':checked')) {
        $("#yearSlider").show();
    } else {
        $("#yearSlider").hide();
    }
});

$('#flexRadioDefault11').click(function() {
    if( $(this).is(':checked')) {
        $("#ratingSlider").show();
    } else {
        $("#ratingSlider").hide();
    }
}); 

$('#flexRadioDefault12').click(function() {
    if( $(this).is(':checked')) {
        $("#timeSlider").show();
    } else {
        $("#timeSlider").hide();
    }
}); 

$("#gpaRange").on("change mousemove", function() {
    $("#gpaValue").html($(this).val()/10)
})

$("#yearRange").on("change mousemove", function() {
    $("#yearValue").html($(this).val())
})

$("#ratingRange").on("change mousemove", function() {
    $("#ratingValue").html($(this).val()/10)
})

$("#timeRange").on("change mousemove", function() {
    $("#timeValue").html($(this).val())
})


$('#main-input').keypress(function(e) 
{
    if (e.which == 13) // the enter key code
    {
        $('#main-search-button').click();
    }
});

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

//jQuery extension method:
jQuery.fn.filterByText = function(textbox) 
{
    return this.each(function() 
    {
        var select = this;
        var options = [];
        $(select).find('option').each(function() 
        {
            options.push
            ({
                value: $(this).val(),
                text: $(this).text()
            });
        });
        $(select).data('options', options);

        $(textbox).bind('change keyup', function() 
        {
            var options = $(select).empty().data('options');
            var search = $.trim($(this).val());
            var regex = new RegExp(search, "gi");

            $.each(options, function(i) 
            {
                var option = options[i];
                if (option.text.match(regex) !== null) 
                {
                    $(select).append($('<option>').text(option.text).val(option.value));
                }
            });
        });
    });
};

$('*[id*=professor-field]:visible').each(function() 
{
    $('select').filterByText($(this));
});
