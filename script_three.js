function validate(event) {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgbox = document.getElementById("message");

    let message = "";
    if (email === ""){
        message = "please enter an email";
        msgbox.style.color = "red";
    }
    else if (password === ""){
        message = "please enter the password";
        msgbox.style.color = "red";
    }
    else if (age === ""){
        message = "please enter your age";
    msgbox.style.color = "red";
}
else {
    message = "login successful";
    msgbox.style.color = "green";
}
msgbox.innerText = message;
}
