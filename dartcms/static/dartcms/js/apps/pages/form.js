$(function () {
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
});