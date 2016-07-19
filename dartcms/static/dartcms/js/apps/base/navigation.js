$(function () {
    /**
     * Side menu nav
     */
    $('#id-navmenu').on('hide.bs.dropdown', function () {
        return false;
    });
    $('li.dropdown a').on('click', function (e) {
        e.stopPropagation();
        $(this).parent().toggleClass('open');
    });
});