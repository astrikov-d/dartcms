$(function () {
    var permissionToggle = $('.check-permissions');

    permissionToggle.on('click', function (e) {
        e.preventDefault();
        var state = $(this).attr('data-state');
        var checkboxes = $('input[type="checkbox"]', $(this).parents('.module-permissions'));

        if (state === 'off') {
            checkboxes.prop('checked', true);
            $(this).attr('data-state', 'on');
        } else {
            checkboxes.prop('checked', false);
            $(this).attr('data-state', 'off');
        }
    });
});