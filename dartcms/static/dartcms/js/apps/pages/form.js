$(function () {
    /**
     * Module params laoding.
     */
    var loadModuleParams = function () {
        var selected_module = $('#id_module').val(),
            moduleParamsSelect = $('#id_module_params'),
            context = $('#id-context-variables'),
            page_pk = context.attr('data-page-pk'),
            loading_url = context.attr('data-loading-url');


        moduleParamsSelect.html('');

        $.ajax({
            url: loading_url,
            dataType: 'json',
            data: {
                selected_module: selected_module,
                pk: page_pk
            }
        }).done(function (response) {
            if (response.result) {
                if (response.data.length) {
                    for (var i = 0; i < response.data.length; i++) {
                        if (response.data[i].selected)
                            moduleParamsSelect.append('<option selected value="' + response.data[i].value + '" >' + response.data[i].label + '</option>');
                        else
                            moduleParamsSelect.append('<option value="' + response.data[i].value + '" >' + response.data[i].label + '</option>');
                    }
                    moduleParamsSelect.parents('.form-group').show();
                } else {
                    moduleParamsSelect.parents('.form-group').hide();
                }
            }
        });
    };

    $('#id_module').on('change', function (e) {
        loadModuleParams();
    });
    loadModuleParams();

    /**
     * Security toggling.
     */
    var toggleUserGroups = function () {
        var security_type = $('#id_security_type').val(),
            userGroupsSelect = $('#id_user_groups');

        if (security_type == 'DEFAULT' || security_type == 'BY_PARENT') {
            userGroupsSelect.parents('.form-group').hide();
        } else {
            userGroupsSelect.parents('.form-group').show();
        }
    };

    $('#id_security_type').on('change', function (e) {
        toggleUserGroups();
    });
    toggleUserGroups();
});