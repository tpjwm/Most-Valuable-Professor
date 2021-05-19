$(document).ready(function () 
{
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) 
    {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const NetID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (NetID === 'New User') {
            modal.find('.modal-title').text(NetID)
            $('#netid-form-display').removeAttr('NetID')
        } else {
            modal.find('.modal-title').text('Edit User ' + NetID)
            $('#netid-form-display').attr('NetID', NetID)
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-user').click(function () {
        const NetID = $('#netid-form-display').attr('NetID');
        const Password = $('#password-form-display').attr('Password');
        console.log($('#user-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: NetID ? '/edit/' + NetID + '/' + Password: '/create',
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
    });


    $('.remove').click(function () 
    {
        console.log('TEST')
        const remove = $(this)
        $.ajax
        ({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
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


    $('.state').click(function () 
    {
        const state = $(this)
        const tID = state.data('source')
        const new_state
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});