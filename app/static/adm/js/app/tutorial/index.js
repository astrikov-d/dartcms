/**
 * Created by Dmitry Astrikov on 21.03.14.
 */

$(function () {
    $('#id-start-tutorial-btn').on('click', function (e) {
        e.preventDefault();
        bootstro.start('.bootstro', {
            finishButtonText: 'Все понятно, верните меня на сайт',
            nextButtonText: 'Дальше',
            prevButtonText: 'Назад'
        });
    });
});