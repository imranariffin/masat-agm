var prev_data;

$(function () {
    callAjax();
});

function callAjax() {

    var dum_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    $.ajax({
        type: 'GET',
        url: '/resultAPI',
        success: function(data) {
                $.each(data, function(i, pos) {
                    var col_arr = new Array();

                    $.each(pos.ls, function (j, candidate) {
                        console.log("candidate: ");
                        console.log(candidate);
                        candidate[0] = dum_names[j];
                        col_arr.push(candidate);
                    });

                    var chart = c3.generate({
                        bindto: '#' + pos.position + '_chart',
                        data:                                                                           {
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
            setTimeout(callAjax, 2500);
        },
        dataType: 'json',
    });
}