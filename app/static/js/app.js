function open_page(btn) {
    // Remove the class "active" from all Buttons and TabContent
    var active_buttons = document.getElementsByClassName("active_button");
    var active_contents = document.getElementsByClassName("active_content");

    if (active_contents.length && active_buttons.length > 0) {
        active_buttons[0].classList.remove("active_button");
        active_contents[0].classList.remove("active_content");
    }

    // Add the class "active" in the clicked button (change the button background)
    document.getElementById(btn).classList.add("active_button");

    // Add the class "active" in the respective tab_content, according to the clicked button (Show the specific content (display:block))
    document.getElementById(btn + "_embed").classList.add("active_content")
    
}

// Initialization of elements Materialize
M.AutoInit();


// Use the icon as a way to submit
var form = document.getElementById("form");
document.getElementById("icon").addEventListener("click", function () {
    form.submit();
})

// Submit by enter key and check if all field are filled up
var input_word = document.getElementById("word");
var input_select = document.getElementById("dictionaries")
document.addEventListener("keypress", function() {
    if (event.keyCode == 13) {
        if (input_word.value.length != 0 && input_select.value != "") {
            form.submit();
        }
        else {
            alert("You should fill all the fields");
        }
    }
})


// Click on the default tab
document.getElementsByClassName("tabButton")[0].click();