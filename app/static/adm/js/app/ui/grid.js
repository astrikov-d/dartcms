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
        btn_multiple_action = $('.btn-multiple-action'),
        clickable_row = $('.clickable-row');

    clickable_row.on('click', function (e) {
        e.preventDefault();

        if (!$(this).hasClass('multiple')) {
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
        } else {
            var selectedRows = $('tr.selected');
            if (selectedRows.length > 1) {
                btn_update.addClass('btn-disabled');
                btn_delete.addClass('btn-disabled');
                btn_children.addClass('btn-disabled');
                btn_multiple_action.removeClass('btn-disabled');
            } else {
                if (selectedRows.length == 1) {
                    btn_update.removeClass('btn-disabled');
                    btn_delete.removeClass('btn-disabled');
                    btn_children.removeClass('btn-disabled');
                    btn_multiple_action.removeClass('btn-disabled');
                } else {
                    btn_update.addClass('btn-disabled');
                    btn_delete.addClass('btn-disabled');
                    btn_children.addClass('btn-disabled');
                    btn_multiple_action.addClass('btn-disabled');
                }
            }
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

    var isMouseDown = false,
        isHighlighted = false,
        multipleSelectRows = $('.clickable-row.multiple');

    multipleSelectRows.mousedown(function () {
        isMouseDown = true;
        $(this).toggleClass("selected");
        isHighlighted = $(this).hasClass("selected");
        return false;
    }).mouseover(function () {
            if (isMouseDown) {
                $(this).toggleClass("selected", isHighlighted);
            }
        });

    $(document).mouseup(function () {
        isMouseDown = false;
        var selectedRows = $('tr.selected');
        if (selectedRows.length > 1) {
            btn_multiple_action.removeClass('btn-disabled');
        } else {
            btn_multiple_action.addClass('btn-disabled');
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

    var getSelectedRowIds = function () {
        var selected_rows = $('.clickable-row.multiple.selected');
        if (selected_rows.length) {
            var selected_ids = [];
            selected_rows.each(function (index, element) {
                selected_ids[index] = parseInt($(element).attr('data-pk'));
            });
            return selected_ids.join('-');
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

    btn_multiple_action.on('click', function (e) {
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
            document.location.href = url[0] + getSelectedRowIds() + '/?' + url[1];
        } else {
            document.location.href = url[0] + getSelectedRowIds() + '/';
        }
    });
});