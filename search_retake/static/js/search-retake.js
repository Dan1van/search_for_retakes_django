let send_data = {};

$(document).ready(function () {
    resetFilters();
    getAPIData();
    getDisciplines();


    $('#discipline').change(function () {
        let teacher_select = $('#teacher');

        teacher_select.val('_None');
        send_data['teacher'] = '';

        if (this.value === '_None') {
            send_data['discipline'] = '';
            teacher_select.attr('disabled', 'disabled')
        } else {
            send_data['discipline'] = this.value;
            teacher_select.removeAttr('disabled')
        }

        getTeachers(this.value);
        getAPIData();
    });

    $('#teacher').change(function () {
        if (this.value === '_None') {
            send_data['teacher'] = '';
        } else {
            send_data['teacher'] = this.value;
        }

        getAPIData();
    });

    $('#course').change(function () {
        let group_select = $('#group');

        send_data['group'] = '';
        group_select.val('_None');

        if (this.value === '_None') {
            send_data['course'] = '';
            group_select.attr('disabled', 'disabled')
        } else {
            send_data['course'] = this.value;
            group_select.removeAttr('disabled')
        }

        getGroups(this.value);
        getAPIData();
    });

    $('#group').change(function () {
        if (this.value === '_None') {
            send_data['group'] = '';
        } else {
            send_data['group'] = this.value;
        }

        getAPIData();
    });

    $("#next").click(function () {
        let url = $(this).attr("url");
        if (!url)
            $(this).prop('all', true);

        $(this).prop('all', false);
        $.ajax({
            method: 'GET',
            url: url,
            success: function (result) {
                putTableData(result);
            },
            error: function(response){
                console.log(response)
            }
        });
    });

    $("#previous").click(function () {
        let url = $(this).attr("url");
        if (!url)
            $(this).prop('all', true);

        $(this).prop('all', false);
        $.ajax({
            method: 'GET',
            url: url,
            success: function (result) {
                putTableData(result);
            },
            error: function(response){
                console.log(response)
            }
        });
    });
});

function resetFilters() {
    $('#discipline').val('_None');
    $("#teacher").val('_None');
    $("#course").val("_None");
    $("#group").val("_None");


    send_data['discipline'] = '';
    send_data['teacher'] = '';
    send_data['group'] = '';
    send_data['format'] = 'json';
}

function putTableData(result) {
    if (result['results'].length > 0) {
        $('#no_result').hide();
        $('#list_data').show();
        $('#listing').html('');
        $.each(result['results'], function(a, b) {
           let row;
           row = `<tr>`;
           row += `<td>${b.discipline}</td>`;
           row += `<td>${b.teacher}</td>`;
           row += `<td>${b.group}</td>`;
           row += `<td>${b.audience}</td>`;
           row += `<td>${b.date}</td>`;
           row += `</tr>`;
           $('#listing').append(row);
        });
    } else {
        $('#list_data').hide();
        $('#no_result').show();
    }

    let prev_url = result["previous"];
    let next_url = result["next"];

    if (prev_url === null) {
        $("#previous").parent().addClass("disabled");
        $("#previous").prop('disabled', true);
    } else {
        $("#previous").parent().removeClass("disabled");
        $("#previous").prop('disabled', false);
    }
    if (next_url === null) {
        $("#next").parent().addClass("disabled");
        $("#next").prop('disabled', true);
    } else {
        $("#next").parent().removeClass("disabled");
        $("#next").prop('disabled', false);
    }

    $("#previous").attr("url", result["previous"]);
    $("#next").attr("url", result["next"]);

    $("#result-count span").html(result["count"]);
}

function getAPIData() {
    let url = $('#list_data').attr("url");
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        // beforeSend: function(){
        //     $("#no_results h5").html("Loading data...");
        // },
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            // $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
        }
    });
}

function getDisciplines() {
    let url = $('#discipline').attr('url');
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (response) {
            let disciplines_option = "<option value='_None' selected>---------</option>";
            $.each(response['disciplines'], function (a, b) {
                disciplines_option += `<option value="${b[0]}">${b[1]}</option>`
            });

            $('#discipline').html(disciplines_option);
        },
        error: function (response) {
            console.log('response')
        }
    });
}

function getTeachers(discipline) {
    let url = $('#teacher').attr('url');

    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'discipline': discipline
        },
        success: function (response) {
            let teachers_option = "<option value='_None' selected>---------</option>";
            $.each(response['teachers'], function (a, b) {
                teachers_option += `<option value="${b[0]}">${b[1]}</option>`
            });
            $('#teacher').html(teachers_option);
        },
        error: function (response) {
            console.log(response);
        }
    });
}

function getGroups(course) {
    let url = $('#group').attr('url');

    $.ajax({
        method: 'GET',
        url: url,
        data: {
            'course': course
        },
        success: function (response) {
            let groups_option = "<option value='_None' selected>---------</option>";
            $.each(response['groups'], function (a, b) {
                groups_option += `<option value="${b[0]}">${b[1]}</option>`
            });
            $('#group').html(groups_option);
        },
        error: function (response) {
            console.log(response);
        }
    });
}