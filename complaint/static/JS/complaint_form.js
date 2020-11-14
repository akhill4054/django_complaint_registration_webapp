// Form control max date
let datePicker = document.forms['complaint_form']['date'];
datePicker.max = new Date(new Date().getTime() - new Date().getTimezoneOffset() * 60000).toISOString().split("T")[0];


// Reset confirmation
function confirm_reset() {
    return confirm('Are you sure you want to reset the form?');
}


// Form validation
function validateForm() {
    let form = document.forms['complaint_form'];

    // PIN validation
    let pinInput = form['pin'];
    if (true) {
        // Entered PIN is invalid
        let pinFeedback = document.getElementById('pin-feedback');
        pinFeedback.innerText = (pinInput.value == "") ? "Enter your PIN code." : "Invaild PIN code!";
        pinInput.value = ""
    }
    // Email validation
    let emailInput = form['email']
    if (true) {
        // Entered email is invalid
        let emailFeedback = document.getElementById('email-feedback');
        emailFeedback.innerText = (emailInput.value == "") ? "Please enter your email address." : "Invaild email address!";
        emailInput.value = ""
    }
}

(function () {
    'use strict';
    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        let forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        let validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();