/**
 * Created by astrikovd on 13.02.15.
 */

$(function () {
    /**
     * Grid buttons
     */

    var btn_update = $('.btn-update'),
        btn_delete = $('.btn-delete'),
        btn_children = $('.btn-children'),
        clickable_row = $('.clickable-row');

    clickable_row.on('click', function (e) {
        e.preventDefault();
        if ($(this).hasClass('selected')) {
            clickable_row.removeClass('selected');
            btn_update.addClass('btn-disabled');
            btn_delete.addClass('btn-disabled');
            btn_children.addClass('btn-disabled');
            $(this).removeClass('selected');
        } else {
            clickable_row.removeClass('selected');
            btn_update.removeClass('btn-disabled');
            btn_delete.removeClass('btn-disabled');
            btn_children.removeClass('btn-disabled');
            $(this).addClass('selected');
        }
    });

    clickable_row.on('dblclick', function (e) {
        $(this).addClass('selected');
        if (btn_update.length > 0) {
            btn_update.removeClass('btn-disabled');
            btn_update.click();
        } else {
            if (btn_children.length > 0) {
                btn_children.removeClass('btn-disabled');
                btn_children.click();
            }
        }
    });

    var getSelectedRowId = function () {
        var selected_row = $('.clickable-row.selected');
        if (selected_row.length) {
            return parseInt(selected_row.attr('data-pk'));
        } else {
            return null;
        }
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
        var url = $(this).attr('href').split('?');
        if (url.length > 1) {
            document.location.href = url[0] + getSelectedRowId() + '/?' + url[1];
        } else {
            document.location.href = url[0] + getSelectedRowId() + '/';
        }
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
        var url = $(this).attr('href').split('?');
        if (url.length > 1) {
            document.location.href = url[0] + getSelectedRowId() + '/?' + url[1];
        } else {
            document.location.href = url[0] + getSelectedRowId() + '/';
        }
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
        var url = $(this).attr('href').split('?');
        if (url.length > 1) {
            document.location.href = url[0] + getSelectedRowId() + '/?' + url[1];
        } else {
            document.location.href = url[0] + getSelectedRowId() + '/';
        }
    });
});