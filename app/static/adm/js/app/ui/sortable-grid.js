$(function () {
    $(".sortable-tree").sortable({
        handle: '.sortable-tree-row-handle',
        onDrop: function ($item, container, _super) {
            $item.removeClass("dragged").removeAttr("style");
            $("body").removeClass("dragging");

            //Send ajax request after drop event.
            var elem_id = $item.attr('data-id'),
                parent_id = $item.parents('li').attr('data-id'),
                sort = $item.prevAll().length + 1;

            $.ajax({
                type: "POST",
                url: 'move/' + elem_id + '/',
                data: {
                    sort: sort,
                    parent: parent_id
                }
            }).done(function (response) {
                    $.pnotify({
                        title: gettext('Warning'),
                        text: gettext('Node successfully moved'),
                        type: 'info'
                    });
                });

            // Remove disabled class from the new parent's toggle
            var dropped_to = $(container.el).parents('li').first(),
                child_toggle = $('> div > .sortable-tree-row-children-toggle-wrapper > .sortable-tree-row-children-toggle', dropped_to);
            child_toggle.removeClass('disabled');
            if($('> ul', dropped_to).is(':visible')) {
                child_toggle.addClass('open');
            } else {
                child_toggle.removeClass('open');
            }

            // Check that item has children
            if(!$('li', $item).length > 0) {
                $('.sortable-tree-row-children-toggle', $item).addClass('disabled').removeClass('open');
            }

        },
        onDragStart: function ($item, container, _super, event) {
            $item.css({
                height: $item.height(),
                width: $item.width()
            });
            $item.addClass("dragged");
            $("body").addClass("dragging");

            // Check that old parent still has children. If it's not, add disabled class to its toggle.
            var dragged_from = $(container.el).parents('li').first();
            if($('> ul > li', dragged_from).length == 1) {
                $('> div > .sortable-tree-row-children-toggle-wrapper > .sortable-tree-row-children-toggle', dragged_from).addClass('disabled').removeClass('open');
            }
        }
    });

    var children_toggle = $('.sortable-tree-row-children-toggle');
    children_toggle.on('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        if ($(this).hasClass('disabled')) {
            return false;
        }
        $(this).toggleClass('open');

        var parent_li = $(this).closest('li'),
            children_ul = parent_li.children('ul').first();
        children_ul.toggle();
    });
});