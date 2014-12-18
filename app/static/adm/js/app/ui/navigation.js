$(function () {
    /**
     * Side menu nav
     */
    var nav_dropdown_toggle = $('.nav-side-menu a.dropdown-toggle');
    nav_dropdown_toggle.on('click', function (e) {
        e.preventDefault();
        var parent_li = $(this).parents('li'),
            dropdown = $('ul.dropdown', parent_li);
        parent_li.toggleClass('open');
        if (!dropdown.is(':visible')) {
            dropdown.slideUp();
        } else {
            dropdown.slideDown();
        }

    });

    /**
     * Scroller for nav menu
     */

    $('.nav-side-menu-content').baron();

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

    var getSelectedRowId = function() {
        var selected_row = $('.clickable-row.selected');
        if(selected_row.length) {
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