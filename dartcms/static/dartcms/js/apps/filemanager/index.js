$(function () {
    /**
     * FM tree init.
     */

    var context = $('#id-context-variables'),
        index_url = context.attr('data-index-url');

    $('#id-fm-tree').tree({
        url: index_url + 'get-tree/',
        method: 'get',
        onContextMenu: function (e, node) {
            e.preventDefault();
            $(this).tree('select', node.target);
            $('#id-fm-tree-menu').menu('show', {
                left: e.pageX,
                top: e.pageY
            });
        },
        onClick: function (node) {
            var helper = $('#id-helper'),
                fm_grid = $('#id-fm-grid');
            helper.hide();
            $('#id-folder-id').val(node.id);
            fm_grid.datagrid({
                method: "GET",
                fitColumns: true,
                singleSelect: true,
                border: false,
                onDblClickRow: function () {
                    var row = fm_grid.datagrid('getSelected');
                    top.tinymce.activeEditor.windowManager.getParams().setUrl('/' + row.path);
                    top.tinymce.activeEditor.windowManager.close();
                },
                toolbar: [
                    {
                        iconCls: 'icon-add',
                        text: gettext('Insert'),
                        handler: function () {
                            var row = fm_grid.datagrid('getSelected');
                            if (row) {
                                top.tinymce.activeEditor.windowManager.getParams().setUrl('/' + row.path);
                                top.tinymce.activeEditor.windowManager.close();
                            } else {
                                $.messager.alert(gettext('Warning'), gettext('Choose File'));
                            }
                        }
                    },
                    {
                        iconCls: 'icon-remove',
                        text: gettext('Remove'),
                        handler: function () {
                            var row = fm_grid.datagrid('getSelected');
                            if (row) {
                                $.ajax({
                                    type: "POST",
                                    url: index_url + 'delete-file/?folder_id=' + node.id + '&file_id=' + row.id,
                                    dataType: "json",
                                    data: {
                                        csrfmiddlewaretoken: $.cookie('csrftoken')
                                    }
                                }).done(function (data) {
                                        if (data.result) {
                                            $('#id-fm-grid').datagrid('reload');
                                        } else {
                                            $.messager.alert('Внимание', data.errors.name);
                                        }
                                    });
                            } else {
                                $.messager.alert(gettext('Warning'), gettext('Choose File'));
                            }
                        }
                    },
                    {
                        iconCls: 'icon-upload',
                        text: gettext('Upload'),
                        handler: function () {
                            var file_selector = $('#id-select-file');
                            file_selector.click();
                        }
                    },
                    {
                        iconCls: 'icon-download',
                        text: gettext('Download'),
                        handler: function () {
                            var row = fm_grid.datagrid('getSelected');
                            if (row) {
                                window.open('/' + row.path);
                            } else {
                                $.messager.alert(gettext('Warning'), gettext('Choose File'));
                            }
                        }
                    }
                ],
                url: index_url + 'get-files/?folder_id=' + node.id,
                columns: [
                    [
                        {field: 'name', title: gettext('File Name'), width: 250},
                        {field: 'path', title: gettext('Path'), width: 400},
                        {field: 'date_created', title: gettext('Upload Date'), width: 400}
                    ]
                ]
            });
        }
    });

    /**
     * File uploading form
     */
    $('#id-file-uploads-form').ajaxForm({
        type: "POST",
        url: index_url + 'send-file/',
        data: {
            csrfmiddlewaretoken: $.cookie('csrftoken')
        },
        dataType: 'json',
        success: function (response) {
            $('#id-fm-grid').datagrid('reload');
        }
    });
    $('#id-select-file').on('change', function (e) {
        $('#id-file-uploads-form').submit();
    });

    /**
     * FM browse context menu
     */
    $('#id-fm-browse-wrapper').bind('contextmenu', function (e) {
        e.preventDefault();
        $('#id-fm-browse-menu').menu('show', {
            left: e.pageX,
            top: e.pageY
        });
    });

    /**
     * Dialogs.
     */
    $('#id-create-folder-dlg').dialog({
        modal: true,
        closed: true,
        iconCls: 'icon-save',
        buttons: [
            {
                text: 'Ок',
                iconCls: 'icon-ok',
                handler: function () {
                    var folder_name = $('#id-folder-name').val();
                    if (folder_name != '') {
                        $.ajax({
                            type: "POST",
                            url: index_url + 'create-folder/',
                            dataType: "json",
                            data: {
                                csrfmiddlewaretoken: $.cookie('csrftoken'),
                                name: folder_name
                            }
                        }).done(function (data) {
                                if (data.result) {
                                    $('#id-folder-name').val('');
                                    $('#id-fm-tree').tree('reload');
                                    $('#id-create-folder-dlg').dialog('close');
                                } else {
                                    $.messager.alert(gettext('Warning'), data.errors.name);
                                }
                            });
                    } else {
                        $.messager.alert(gettext('Warning'), gettext('Input folder name'));
                    }
                }
            },
            {
                text: 'Отмена',
                handler: function () {
                    $('#id-create-folder-dlg').dialog('close');
                }
            }
        ]
    });

    $('#id-rename-folder-dlg').dialog({
        modal: true,
        closed: true,
        iconCls: 'icon-save',
        onBeforeOpen: function () {
            var node = $('#id-fm-tree').tree('getSelected');
            $('#id-new-folder-name').val(node.text);
        },
        buttons: [
            {
                text: 'Ok',
                iconCls: 'icon-ok',
                handler: function () {
                    var node = $('#id-fm-tree').tree('getSelected'),
                        folder_name = $('#id-new-folder-name').val();
                    if (folder_name != '') {
                        $.ajax({
                            type: "POST",
                            url: index_url + 'rename-folder/?folder_id=' + node.id,
                            dataType: "json",
                            data: {
                                name: folder_name,
                                csrfmiddlewaretoken: $.cookie('csrftoken')
                            }
                        }).done(function (data) {
                                if (data.result) {
                                    $('#id-new-folder-name').val('');
                                    $('#id-fm-tree').tree('reload');
                                    $('#id-rename-folder-dlg').dialog('close');
                                } else {
                                    $.messager.alert(gettext('Warning'), data.errors.name);
                                }
                            });
                    } else {
                        $.messager.alert(gettext('Warning'), gettext('Input folder name'));
                    }
                }
            },
            {
                text: 'Cancel',
                handler: function () {
                    $('#id-rename-folder-dlg').dialog('close');
                }
            }
        ]
    });

    $('#id-remove-folder-dlg').dialog({
        modal: true,
        closed: true,
        iconCls: 'icon-save',
        buttons: [
            {
                text: 'Ok',
                iconCls: 'icon-ok',
                handler: function () {
                    var node = $('#id-fm-tree').tree('getSelected');
                    $.ajax({
                        type: "POST",
                        url: index_url + 'delete-folder/?folder_id=' + node.id,
                        dataType: "json",
                        data: {
                            csrfmiddlewaretoken: $.cookie('csrftoken')
                        }
                    }).done(function (data) {
                            if (data.result) {
                                var fm_tree = $('#id-fm-tree');
                                $('#id-fm-grid').datagrid('getPanel').panel('destroy');
                                $('#id-helper').show().after('<div id="id-fm-grid"></div>');
                                fm_tree.tree('reload');
                                $('#id-remove-folder-dlg').dialog('close');
                            }
                        });
                }
            },
            {
                text: 'Cancel',
                handler: function () {
                    $('#id-remove-folder-dlg').dialog('close');
                }
            }
        ]
    });
});
