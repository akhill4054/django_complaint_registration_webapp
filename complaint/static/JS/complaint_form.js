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
    let flag = true;
    
    for (let i = 0; i < form.elements.length; i++) {
        let element = form.elements[i];
        if (!element.checkValidity()) {
            element.classList.add('is-invalid');
            flag = false;
        } else {
            element.classList.remove('is-invalid');
            element.classList.add('is-valid');
        }
    }

    // PIN code validation
    let pinInput = form['pin'];
    let pinFeedback = document.getElementById('pin-feedback');
    if (pinInput.value == "") {
        pinFeedback.innerText = 'Please enter your email address.';
    } else if (!/^\d{6}$/.test(pinInput.value)) {
        // Entered PIN is invalid
        pinInput.classList.add('is-invalid');
        pinFeedback.innerText = 'Entered PIN code is invalid!';
        flag = false;
    }

    // Email validation
    let emailInput = form['email'];
    let emailFeedback = document.getElementById('email-feedback');
    if (emailInput.value === "") {
        emailFeedback.innerText = 'Enter your PIN code.';
    } else if (!/[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/.test(emailInput.value)) {
        // Entered PIN is invalid
        emailInput.classList.add('is-invalid');
        emailFeedback.innerText = 'Entered email address is invalid!';
        flag = false;
    }

    // Phone validation
    let phoneInput = form['phone'];
    if (phone.value != "" && !/^\d{10}$/.test(phoneInput.value)) {
        // Entered phone number is invalid
        phoneInput.classList.add('is-invalid');
        flag = false;
    }

    return flag;
}