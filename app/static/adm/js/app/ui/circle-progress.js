/**
 * Created by Dmitry Astrikov on 21.01.15.
 */

$(function () {
    var circle_progress = $('.circle-progress');
    circle_progress.each(function (index, el) {
        var data_value = $(el).attr('data-value'),
            data_color = $(el).attr('data-color');

        $(el).circleProgress({
            value: data_value,
            fill: { gradient: [data_color] },
        }).on('circle-animation-progress', function (event, progress) {
                $(this).find('strong').html(data_value);
            });
    });
});
