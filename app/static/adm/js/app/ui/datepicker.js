/**
 * Created by Dmitry Astrikov on 10.03.14.
 */

$(function () {
    $(".datetime").datetimepicker({format: 'dd.mm.yyyy hh:ii:ss', language: 'ru', weekStart: 1, autoclose: true});
    $(".date").datetimepicker({format: 'dd.mm.yyyy', language: 'ru', weekStart: 1, minView: 2, autoclose: true});
    $(".time").datetimepicker({format: 'hh:ii:ss', language: 'ru', weekStart: 1, startView: 1, minView: 0, autoclose: true});
});