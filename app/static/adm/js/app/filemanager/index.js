/**
 * Created by Dmitry Astrikov on 20.02.14.
 */

$(function () {

    /**
     * Reload folders list.
     */
    function reloadFoldersList() {
        var current_folder = $('.folder.active').attr('data-folder-id');
        $.ajax({
            url: "/filemanager/get-folders/"
        }).done(function (data) {
                $('#id-folders-list').html('');
                $(data).each(function (index, element) {
                    $('#id-folders-list').append(
                        '<a href="#" class="list-group-item folder" data-folder-id="' + element.pk + '">' + element.name + '</a>'
                    );
                });
                initFoldersList();
                $('.folder[data-folder-id=' + current_folder + ']').click();
            });
    }

    /**
     * Initialization folders controls.
     */
    function initFoldersList() {
        $('.folder').on('click', function (e) {
            $('.folder').removeClass('active');
            e.preventDefault();
            var folder_id = $(this).attr('data-folder-id');
            reloadFilesList(folder_id);
            $(this).addClass('active');
            selected_folder_id = folder_id;
        });

        $(".folder").on("contextmenu", function (e) {
            e.stopPropagation();
            cm_folder_id = $(this).attr('data-folder-id');
            folder_context_menu.css({
                display: "block",
                left: e.pageX,
                top: e.pageY - 80
            });
            return false;
        });
    }

    initFoldersList();

    /**
     * Reload files list.
     * @param folder_id
     */
    function reloadFilesList(folder_id) {
        $.ajax({
            url: "/filemanager/get-files/",
            data: {
                folder_id: folder_id
            }
        }).done(function (data) {
                if (data.length) {
                    var files_list = "";
                    $(data).each(function (index, element) {
                        files_list +=
                            '<tr>' +
                                '<td>' + element.name + '</td>' +
                                '<td>' +
                                '<a class="item-control insert-file" href="#" data-file-path="/data/' + element.path + '"><span class="glyphicon glyphicon-ok"></span></a>' +
                                '<a class="item-control remove-file" href="#" data-file-id="' + element.pk + '"><span class="glyphicon glyphicon-remove"></span></a>' +
                                '<a class="item-control download-file" target="_blank" href="/data/' + element.path + '"><span class="glyphicon glyphicon-download"></span></a>' +
                                '</td>' +
                                '</tr>';
                    });
                    $('#id-files-list').html("<table class='table table-striped'>" + files_list + "</table>");
                    initFilesList();
                } else {
                    $('#id-files-list').html("<p class='help-block'>В этой папке пока пусто</p>");
                }
            });
    }

    /**
     * Initialization of files list controls.
     */
    function initFilesList() {
        $('.insert-file').on('click', function(e){
            e.preventDefault();
            var app_url = window.location.href,
                arr = app_url.split("/"),
                full_url = arr[0] + "//" + arr[2];
            top.tinymce.activeEditor.windowManager.getParams().setUrl($(this).attr('data-file-path'));
            top.tinymce.activeEditor.windowManager.close();
        });
        $('.remove-file').on('click', function(e){
            e.preventDefault();
            var file_id = $(this).attr('data-file-id');
            bootbox.confirm('Вы уверены? Это действие нельзя будет отменить.', function(result){
                if(result) {
                    $.ajax({
                        type: "POST",
                        url: "/filemanager/remove-file/",
                        data: {
                            file_id: file_id
                        }
                    }).done(function (data) {
                            if (data.result == 'success') {
                                // Reload folders.
                                reloadFilesList(selected_folder_id);
                            } else {
                                bootbox.alert(data.errors.name);
                            }
                        });
                }
            });
        });
    }

    /**
     * Create folder.
     */
    $('#id-create-folder-btn').on('click', function (e) {
        e.preventDefault();
        bootbox.prompt('Введите имя папки', function (result) {
            if (result != '') {
                $.ajax({
                    type: "POST",
                    url: "/filemanager/create-folder/",
                    data: {
                        name: result
                    }
                }).done(function (data) {
                        if (data.result == 'success') {
                            // Reload folders.
                            reloadFoldersList();
                        } else {
                            bootbox.alert(data.errors.name);
                        }
                    });
            } else {
                bootbox.alert('Введите имя папки');
            }
        });
    });

    /**
     * File uploading form
     */
    var selected_folder_id = null;
    $('#id_path').on('change', function (e) {
        var upload_form = $('#id-file-upload-form');
        upload_form.ajaxForm({
            type: "POST",
            url: '/filemanager/send-file/',
            dataType: 'json',
            data: {
                selected_folder_id: selected_folder_id
            },
            success: function (response) {
                if (response.result == 'success')
                    reloadFilesList(selected_folder_id);
                else
                    bootbox.alert('Ошибка загрузки файла');
            }
        });
        upload_form.submit();
    });

    $('#id-upload-file-btn').on('click', function (e) {
        e.preventDefault();
        if (selected_folder_id == null) {
            bootbox.alert("Сначала выберите папку");
        } else {
            $('#id_path').click();
        }
    });

    /**
     * Context menu.
     */
    var folder_context_menu = $("#id-folder-context-menu"),
        cm_folder_id = null;

    $('body').on('click', function (e) {
        folder_context_menu.hide();
    });

    $('.context-menu-link').on('click', function (e) {
        if ($(this).hasClass('rename-folder')) {
            bootbox.prompt('Введите новое имя для этой папки', function (result) {
                if (result) {
                    $.ajax({
                        type: "POST",
                        url: "/filemanager/rename-folder/",
                        data: {
                            folder_id: cm_folder_id,
                            name: result
                        }
                    }).done(function (data) {
                            if (data.result == 'success') {
                                // Reload folders.
                                reloadFoldersList();
                            } else {
                                bootbox.alert(data.errors.name);
                            }
                        });
                }
            });
        }
        if ($(this).hasClass('remove-folder')) {
            bootbox.confirm('Вы уверены? Это приведет к удалению всех файлов внутри этой папки', function (result) {
                if (result) {
                    $.ajax({
                        type: "POST",
                        url: "/filemanager/remove-folder/",
                        data: {
                            folder_id: cm_folder_id
                        }
                    }).done(function (data) {
                            if (data.result == 'success') {
                                // Reload folders.
                                reloadFoldersList();
                            } else {
                                bootbox.alert(data.errors.name);
                            }
                        });
                }
            });
        }
        folder_context_menu.hide();
    })

});
