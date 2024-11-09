$(function() {
    $('.region').on('click', function(event) {
        $('#snippet-card').show();
        var code = $(this).data('code');
        var name = $(this).data('name');
        $('#code').text('https://feiertage.vladmos.com/calendar/' + code);
        $('#card-title').text('Custom iCal feed for ' + name);
    });

    var copyToClipboard = function(text) {
        var tempTextarea = $('<textarea>');
        $('body').append(tempTextarea);
        tempTextarea.val(text).select();
        document.execCommand('copy');
        tempTextarea.remove();
    }

    $('#copy').on('click', function(event) {
        copyToClipboard($('code').text());
        $('#copy').text('Copied');
        setTimeout(function() {
            $('#copy').text('Copy');
        }, 1000);
    })
});
