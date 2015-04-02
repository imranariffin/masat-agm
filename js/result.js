var prev_data;

$(function () {
    callAjax();
});

function callAjax() {
    $.ajax({
        type: 'GET',
        url: '/resultAPI',
        success: function(data) {
                $.each(data, function(i, pos) {
                    var col_arr = new Array();

                    $.each(pos.ls, function (j, candidate) {
                        col_arr.push(candidate)
                    });

                    var chart = c3.generate({
                        bindto: '#' + pos.position + '_chart',
                        data: {
                            columns: col_arr,
                            type: 'pie'
                        },
                        pie: {
                            label: {
                                format: function (value, ratio, id) {
                                    return d3.format('')(value);
                                }
                            }
                        }
                    });
                });
        },
        complete: function() {
            setTimeout(callAjax, 1100);
        },
        dataType: 'json',
    });
}