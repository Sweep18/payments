$(document).ready(function () {

    $('#pay').submit(function (e) {
        e.preventDefault();
        $.ajax({
            data: $(this).serialize(),
            type: 'POST',
            url: '/payment/',
            dataType: 'json',
            async: false,
            complete: function (response) {
                data = response.responseJSON;
            }
        });
        $("#message").text(data['message']);
    });

});