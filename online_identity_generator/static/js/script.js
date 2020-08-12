function show_message(msg, color) {
    var error_element = $("#message");
    error_element.css('display', 'flex');
    error_element.css('background-color', color);
    $("#message_msg").html(msg);
}

function hide(msg) {
    var error_element = $("#message");
    error_element.css('display', 'none');
}