$(function () {

    // Validation related.
    $.validator.setDefaults({
        errorElement: "span",
        errorClass: "help-block",
        highlight: function (element, errorClass, validClass) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).closest('.form-group').removeClass('has-error');
        },
        errorPlacement: function (error, element) {
            if (element.parent('.input-group').length || element.prop('type') === 'checkbox' || element.prop('type') === 'radio') {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        }
    });

    $('form').each(function (index, element) {
        $(element).validate();
    });

    // Multiselect.
    $('select[multiple="multiple"]').multiselect({
        allSelectedText: gettext('All selected'),
        nonSelectedText: gettext('None selected'),
        nSelectedText: gettext(' options selected'),
        selectAllText: gettext('Select all'),
        includeSelectAllOption: true
    });
});
