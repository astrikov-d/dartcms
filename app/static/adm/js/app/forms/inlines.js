/**
 * Created by Dmitry Astrikov on 21.01.15.
 */

$(function(){
    var add_inlines_btn = $('.add-more-inlines-btn');
    add_inlines_btn.click(function() {
        var formset_wrapper = $(this).parents('.inlines-wrapper'),
            total_forms_input = $('input[type="hidden"]:first', formset_wrapper),
            total_forms_count = total_forms_input.val(),
            inlines = $('.inlines', formset_wrapper),
            empty_form = $('.empty-formset-form', formset_wrapper);

        inlines.append(empty_form.html().replace(/__prefix__/g, total_forms_count));
        total_forms_input.val(parseInt(total_forms_count) + 1);
    });
});