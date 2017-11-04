var modal = document.getElementById('scrum-add-new-modal');
var btn = document.getElementById("scrum-modal-open");
var span = document.getElementsByClassName("scrum-modal-close")[0];

if (btn) {
    btn.onclick = function() {
        modal.style.display = "block";
    };
}


if (span) {
    span.onclick = function () {
        modal.style.display = "none";
    };
}

if (modal) {
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}