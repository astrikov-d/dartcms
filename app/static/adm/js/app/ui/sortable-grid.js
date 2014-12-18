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
        }
    });
});