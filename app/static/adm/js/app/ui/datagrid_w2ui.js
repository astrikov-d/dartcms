/**
 * Created by astrikovd on 13.02.15.
 */

$(function () {
    /**
     * Grid buttons
     */

    var btn_update = $('.btn-update'),
        btn_delete = $('.btn-delete'),
        btn_children = $('.btn-children');

    var getSelectedRowId = function () {
        return w2ui.grid.getSelection();
    };

    btn_update.on('click', function (e) {
        e.preventDefault();
        if ($(this).hasClass('btn-disabled')) {
            $.pnotify({
                title: gettext('Warning'),
                text: gettext('Choose row for update'),
                type: 'info'
            });
            return false;
        }
        document.location.href = $(this).attr('href') + getSelectedRowId() + '/';
    });

    btn_delete.on('click', function (e) {
        e.preventDefault();
        if ($(this).hasClass('btn-disabled')) {
            $.pnotify({
                title: gettext('Warning'),
                text: gettext('Choose row for deletion'),
                type: 'info'
            });
            return false;
        }
        document.location.href = $(this).attr('href') + getSelectedRowId() + '/';
    });

    btn_children.on('click', function (e) {
        e.preventDefault();
        if ($(this).hasClass('btn-disabled')) {
            $.pnotify({
                title: gettext('Warning'),
                text: gettext('Choose row'),
                type: 'info'
            });
            return false;
        }
        document.location.href = $(this).attr('href') + getSelectedRowId() + '/';
    });
});