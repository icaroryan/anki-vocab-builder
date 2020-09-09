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

function validation() {
    // If the select field exists
    if (input_select){

        // If it's OK
        if (input_word.value.length != 0 && input_select.value != "") {
            form.submit();
        }

        // If the search bar field is empty
        if (input_word.value.length == 0) {
            input_word.classList.add("invalid");
        }

        // If not empty
        else {
            // If it's with 'invalid' tag, replace it to 'valid', otherwise add the tag 'valid'
            input_word.classList.contains("invalid") ? input_word.classList.replace("invalid", "valid") : input_word.classList.add("valid");
        }

        // If the user didn't select any dictionary
        if (input_select.value == "") {
            dropdown.classList.add("invalid");
        }

        // If the dictionary was selected
        else {
            // 'invalid'? replace it to 'valid'. Otherwise add 'valid'
            dropdown.classList.contains("invalid") ? dropdown.classList.replace("invalid", "valid") : dropdown.classList.add("valid");
        }
    }

    // If there's no select field
    else {
        if (input_word.value.length != 0) {
            form.submit();
        }
    }
}

function google_search_engine(word) {
    // Automatically fill up the field with the word and click on the search button
    var iframe = document.querySelector("iframe#gimages");
    var doc = iframe.contentDocument || iframe.contentWindow.document;
    doc.getElementById("gsc-i-id1").value = word;
    doc.querySelector("button.gsc-search-button.gsc-search-button-v2").click()

}


// Initialization of elements Materialize
M.AutoInit();


// Use the icon as a way to submit
var form = document.getElementById("form");
var input_word = document.getElementById("word");
var dropdown = document.querySelector("input.select-dropdown.dropdown-trigger");
var input_select = document.getElementById("dictionaries");


// In case it's red, change it to green when the user changes the input
input_word.addEventListener("input", function() {
    if (input_word.value.length != 0 && input_word.classList.contains("invalid")) {
        input_word.classList.replace("invalid", "valid")
    }
})


// In case it's red, change it to green when the user changes the input
if (input_select) {
    input_select.addEventListener("change", function() {
        if (input_select.value != "" && dropdown.classList.contains("invalid")) {
            dropdown.classList.replace("invalid", "valid")
        }
    })
}


// Submit the form by clicking in the icon
document.getElementById("icon").addEventListener("click", function () {
    validation()
})

// Submit the form by pressing enter
document.addEventListener("keypress", function() {
    if (event.keyCode == 13) {
        validation()
    }
})


// Click on the default tab
document.getElementsByClassName("tabButton")[0].click();