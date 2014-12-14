/**
 * Created by Dmitry Astrikov on 21.03.14.
 */
$(function () {
    var loadModuleParams = function () {
        var selected_module = $('#id_module').val(),
            module_params_select = $('#id_module_params'),
            page_pk_holder = $('#id_page_pk'),
            page_pk = null;

        if (page_pk_holder.length) {
            page_pk = page_pk_holder.html();
        }

        module_params_select.html('');

        $.ajax({
            url: "/pagemap/load-module-params/",
            dataType: 'json',
            data: {
                selected_module: selected_module,
                pk: page_pk
            }
        }).done(function (response) {
                if (response.result == 'success') {
                    if (response.data.length) {
                        for (var i = 0; i < response.data.length; i++) {
                            if (response.data[i].selected)
                                module_params_select.append('<option selected value="' + response.data[i].value + '" >' + response.data[i].label + '</option>');
                            else
                                module_params_select.append('<option value="' + response.data[i].value + '" >' + response.data[i].label + '</option>');
                        }
                        module_params_select.parents('.form-group').show();
                    } else {
                        module_params_select.parents('.form-group').hide();
                    }
                }
            });
    };

    $('#id_module').on('change', function(e){
        loadModuleParams();
    });
    loadModuleParams();
});
