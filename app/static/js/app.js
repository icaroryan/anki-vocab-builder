function open_page() {
    var elmts = document.getElementsByClassName("tabContentContainer")
    for (var i = 0; i < elmts.length; i +=1) {
        elmts[i].style.display = "none";
    }

    
}

// document.getElementsByClassName("tabButton").addEventListener("click", open_page())