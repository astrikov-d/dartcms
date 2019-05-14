$(function () {
    var body = $('body');

    body.on($.modal.OPEN, function (event, modal) {
        mceInit();
    });

    body.on($.modal.AFTER_CLOSE, function (event, modal) {
        $('.form-modal').remove();
        mceDestroy();
    });
});


var openFormModal = function (url, onSubmitSuccess, onSubmitError, onOpen) {
    $.get(url, function (html) {
        $(html).appendTo('body').modal({
            modalClass: "modal form-modal"
        });
        var formModal = $('.form-modal');
        formModal.css('top', 0);
        formModal.css('width', $('.page-content').width());
        formModal.css('min-height', $('.page-content').height());
        $('form', formModal).attr('action', url);
        initModalControls(formModal, onSubmitSuccess, onSubmitError);
        if (typeof initDatePickers === "function") {
            initDatePickers();
        }
        if (onOpen) {
            onOpen(formModal);
        }
    });
    return false;
};

var initModalControls = function (modal, onSubmitSuccess, onSubmitError) {
    // Modals closing
    var closeModalButton = $('.btn-close-modal', modal);
    closeModalButton.on('click', function (e) {
        e.preventDefault();
        $.modal.close();
    });

    // Forms related
    var form = $('form', modal);
    form.each(function (index, element) {
        $(element).validate({
            submitHandler: function (form) {
                $(form).ajaxSubmit({
                    method: 'POST',
                    dataType: 'json',
                    beforeSubmit: function () {
                        $('.errorlist').remove();
                    },
                    success: function (response) {
                        if (response.result) {
                            var msg = '';

                            if (response.action == 'DELETE') {
                                msg = gettext('Record successfully deleted');
                                $('#id-datagrid').datagrid('reload');
                            } else {
                                if (response.action == 'INSERT') {
                                    msg = gettext('Record successfully inserted');
                                } else {
                                    msg = gettext('Record successfully updated');
                                }
                            }

                            new PNotify({
                                title: gettext('Success'),
                                text: msg,
                                icon: 'fa fa-check-circle'
                            });
                            $.modal.close();

                            if (onSubmitSuccess) {
                                onSubmitSuccess(response);
                            }
                        } else {
                            if (response.hasOwnProperty('errors')) {

                                $.each(response.errors, function (field, errors) {
                                    if (field == '__all__') {
                                        $(form).prepend('<ul class="errorlist"><li>' + errors.join(', ') + '</li></ul>');
                                    } else {
                                        $('#id_' + field).after('<ul class="errorlist"><li>' + errors.join(', ') + '</li></ul>');
                                    }

                                    if ($('.errorlist').length && $('.nav-tabs').length) {
                                        var tab_id = $('.errorlist').parents('.tab-pane').attr('id');
                                        $('a[href="#' + tab_id + '"]').tab('show');
                                    }
                                });

                                $('.jquery-modal').animate({
                                    scrollTop: $(".errorlist:first").offset().top
                                }, 0);

                            } else if (response.hasOwnProperty('error')) {
                                var errorMsg = '';

                                if (response.error == 'PROTECTED') {
                                    errorMsg = gettext('Cannot delete the object: related objects exist');
                                }

                                new PNotify({
                                    title: gettext('Error'),
                                    text: errorMsg,
                                    icon: 'fa fa-exclamation-circle',
                                    type: 'error'
                                });
                                $.modal.close();
                            }

                            if (onSubmitError) {
                                onSubmitError();
                            }
                        }
                    }
                });
            }
        });
    });

    var selects = $('select.chosen', form);
    var select_param = {
        allSelectedText: gettext('All selected'),
        nonSelectedText: gettext('None selected'),
        nSelectedText: gettext(' options selected'),
        selectAllText: gettext('Select all'),
        filterPlaceholder: gettext('Search...'),
        includeSelectAllOption: true,
        maxHeight: 400
    };
    selects.each(function () {
        var select = $(this);
        select_param.enableCaseInsensitiveFiltering = $('option', select).length > 10;
        select.multiselect(select_param);
    });

    // Inlines
    var add_inlines_btn = $('.add-more-inlines-btn');
    add_inlines_btn.click(function () {
        var formset_wrapper = $(this).parents('.inlines-wrapper'),
            total_forms_input = $('input[type="hidden"]:first', formset_wrapper),
            total_forms_count = total_forms_input.val(),
            inlines = $('.inlines', formset_wrapper),
            empty_form = $('.empty-formset-form', formset_wrapper),
            form = $(empty_form.html().replace(/__prefix__/g, total_forms_count)),
            close = $('<a href="#" class="close-formset" title="close">&times;</a>');

        form.append(close);
        inlines.append(form);

        total_forms_input.val(parseInt(total_forms_count) + 1);

        close.click(function () {
            $(this).parent().remove();
            total_forms_count = total_forms_input.val();
            total_forms_input.val(parseInt(total_forms_count) - 1);
        });
    });
};
