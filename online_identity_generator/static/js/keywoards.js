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

        if (!((char_code > 47 && char_code < 58) || (char_code > 64 && char_code < 91) || (char_code > 96 && char_code < 122))) {
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