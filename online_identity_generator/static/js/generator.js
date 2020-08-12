var keywoards = [];

function construct_tag(value) {
    return `<div onclick="remove_keywoard('${value}');" class="keywoard" id="keywoard_${value}"><p>${value}</p><img src="../../../static/images/icons/cross.svg"></div>`;
}

function add_keywoard() {
    var element = $("#new_keywoard_input");
    var value = element.val();

    // If there is no input stop doing shit
    if (value == "" || keywoards.includes(value)) {
        return;
    }

    for (var i = 0; i < value.length; i++) {
        var char_code = value.charCodeAt(i);

        if (!((char_code > 47 && char_code < 58) || (char_code > 64 && char_code < 91) || (char_code > 96 && char_code < 123))) {
            show_message("Please don't use special characters", "red");
            return;
        }
    }

    var first_keywoard = false;
    if (keywoards.length == 0) {
        first_keywoard = true;
    }

    keywoards.push(value);

    var keywoards_element = $("#keywoards");

    var keywoard_tag_html = construct_tag(value);


    if (first_keywoard) {
        keywoards_element.html(keywoard_tag_html);
    } else {
        keywoards_element.append(keywoard_tag_html);
    }

    element.val("");
}

function remove_keywoard(keywoard) {
    var index = keywoards.indexOf(keywoard);

    keywoards.splice(index, 1);

    var keywoards_element = $("#keywoards");

    console.log(keywoards_element.html());
    console.log(construct_tag(keywoard));

    console.log(keywoards_element.html().includes(construct_tag(keywoard)));

    keywoards_element.html(keywoards_element.html().replace(construct_tag(keywoard), ''));

    console.log(keywoards);
}

var selected_online_name = null;
var selected_username = null;

function select_choice(id) {
    var choice_element = $(`#${id}`);

    if (id.startsWith('online_name')) {
        if (selected_online_name != null) {
            selected_online_name.css('background-color', 'white');
            selected_online_name.css('color', 'var(--primary-color)');
            selected_online_name.css('border', '1px solid var(--primary-color)');
        }
        selected_online_name = choice_element;
        online_name = selected_online_name.children().html()

        post_data({
            "action": "online_name",
            "online_name": online_name,
        })

    } else {
        if (selected_username != null) {
            selected_username.css('background-color', 'white');
            selected_username.css('color', 'var(--primary-color)');
            selected_username.css('border', '1px solid var(--primary-color)');
        }
        selected_username = choice_element;

        username = selected_username.children().html();

        post_data({
            "action": "username",
            "username": username,
        })
    }
    choice_element.css('background-color', 'var(--green)');
    choice_element.css('color', 'white');
    choice_element.css('border', 'none')
}

function generate() {
    post_data({
        "action": "keywoards",
        "keywoards": keywoards
    });
}

function generator_ajax_handler(data) {
    // Function to handle displaying the data comming from the backend for the choices page
    // It's a little ugly code, I know, but it works

    if ('onlinenames' in data)
    {
        var onlinename_tags = ""

        data['onlinenames'].forEach(function (name) {
            onlinename_tags += `<div class="choice" id="online_name_choice_${name.replace(' ', '_')}" onclick="select_choice('online_name_choice_${name.replace(' ', '_')}');"><p>${name}</p></div>`;
        })

        $("#online_name").html(onlinename_tags);
    }
    else if ('usernames' in data)
    {
        var username_tags = ""

        data['usernames'].forEach(function (username) {
            username_tags += `<div class="choice" id="username_choice_${username}" onclick="select_choice('username_choice_${username}');"><p>${username}</p></div>`;
        })

        $("#username").html(username_tags);
    }
    else if ('email' in data) {
        var email = data['email']
        $("#email").html(`<b>${data['email']}</b>`)
    }


}