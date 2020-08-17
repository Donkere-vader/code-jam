function toggle(id) {
    var element = $("#mobile_nav");
    if (element.css("display") != 'none') {
        element.css("display", "none");
    } else {
        element.css("display", "inherit");
    }
}