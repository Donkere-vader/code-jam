var handlers = {
    "generator": generator_ajax_handler
};

function post_data(data) {
    var formData = new FormData();

    jQuery.each(data, function(key) {
        formData.append(key, data[key]);
    });

    $.post({
        url: '../../ajax',
        data: formData,
        type: 'POST',
        processData: false,
        contentType: false //,
    }, function (data) {
        if ('msg' in data)
        {
            show_message(data['msg'], 'green')
        }
        else if ('error' in data)
        {
            show_message(data['error'], 'red')
        }
        if ('handler' in data) {
            handlers[data['handler']](data) // Call the correct handler function
        }
    });
}