/**
 * Created by Dmitry Astrikov on 30.10.14.
 */

$(function() {
    $('.tt').tooltip();

    var popover_toggle = $('.popover-toggle');
    popover_toggle.popover();
    popover_toggle.on('click', function(e){
        e.preventDefault();
    });

});