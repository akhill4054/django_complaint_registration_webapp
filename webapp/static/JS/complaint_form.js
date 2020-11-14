// Form control max date
let datePicker = document.forms['complaint_form']['date'];
datePicker.max = new Date(new Date().getTime() - new Date().getTimezoneOffset() * 60000).toISOString().split("T")[0];


// Reset confirmation
function confirm_reset() {
    return confirm('Are you sure you want to reset the form?');
}


// Form validation
function validateForm() {
    alert();
    let form = document.forms['complaint_form'];
    let flag = true;
    for (let i = 0; i < form.elements.length; i++) {
        let element = form.elements[i];
        if (element.checkValidity()) {
            element.classList.add('is-invalid');
            flag = false;
        } else {
            element.classList.remove('is-invalid');
            element.classList.add('is-valid');
        }
    }

    return false;
}