$('.date').datepicker({
    multidate: true
});
$('.date').datepicker('setDates', [new Date(2014, 2, 5), new Date(2014, 3, 5)])

$('#datepicker').datepicker({
    multidate: true
});
$('#datepicker').on('changeDate', function() {
    $('#my_hidden_input').val(
        $('#datepicker').datepicker('getFormattedDate')
    );
});

$('.input-daterange input').each(function() {
    $(this).datepicker('clearDates');
});