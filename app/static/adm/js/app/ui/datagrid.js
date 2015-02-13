/**
 * Created by astrikovd on 13.02.15.
 */

function datetimeFormatter(value, row, index) {
    return moment(value).format('DD.MM.YYYY HH:MM:SS');
}

function dateFormatter(value, row, index) {
    return moment(value).format('DD.MM.YYYY');
}

function timeFormatter(value, row, index) {
    return moment(value).format('HH:MM:SS');
}

function stringFormatter(value, row, index) {
    return value;
}

function booleanFormatter(value, row, index) {
    if(value) {
        return '<i class="fa fa-check-circle"></i>';
    } else {
        return '<i class="fa fa-remove"></i>';
    }
}

$(function () {
    /**
     * Grid buttons
     */

    var btn_update = $('.btn-update'),
        btn_delete = $('.btn-delete'),
        btn_children = $('.btn-children'),
        datagrid = $('.datagrid'),
        selected_row_id = null;

    datagrid.bootstrapTable({
        onClickRow: function (row, el) {
            var datagrid_rows = $('tr', datagrid);
            if (el.hasClass('selected')) {
                btn_update.addClass('btn-disabled');
                btn_delete.addClass('btn-disabled');
                btn_children.addClass('btn-disabled');
                datagrid_rows.removeClass('selected');
                selected_row_id = null;
            } else {
                datagrid_rows.removeClass('selected');
                btn_update.removeClass('btn-disabled');
                btn_delete.removeClass('btn-disabled');
                btn_children.removeClass('btn-disabled');
                el.addClass('selected');
                selected_row_id = row.id;
            }
        }
    });

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
        if (selected_row_id != null) {
            var url = $(this).attr('href').split('?');
            if(url.length > 1) {
                document.location.href = url[0] + selected_row_id + '/?' + url[1];
            } else {
                document.location.href = url[0] + selected_row_id + '/';
            }
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
        if (selected_row_id != null) {
            var url = $(this).attr('href').split('?');
            if(url.length > 1) {
                document.location.href = url[0] + selected_row_id + '/?' + url[1];
            } else {
                document.location.href = url[0] + selected_row_id + '/';
            }
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
        if (selected_row_id != null) {
            var url = $(this).attr('href').split('?');
            if(url.length > 1) {
                document.location.href = url[0] + selected_row_id + '/?' + url[1];
            } else {
                document.location.href = url[0] + selected_row_id + '/';
            }
        }
    });

});