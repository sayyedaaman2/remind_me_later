const showPasswordButton = document.getElementById('show-password-btn');
const emailInput = document.querySelector('input[name="email"]');
const passwordInput = document.querySelector('input[name="password"]');
const showPasswordIcon = document.getElementById('show-password-icon');




showPasswordButton.addEventListener('click',(event)=>{

    if(passwordInput.type === 'password'){
        passwordInput.type = 'text';
        showPasswordIcon.src = '/static/image/view.png'
    }else{
        passwordInput.type = 'password'
        showPasswordIcon.src = '/static/image/hide.png'

    }

})


emailInput.addEventListener('change', (event) => {
    const value = event.target.value;
    if (!validateEmail(value) && value !== "") {
        emailInput.style.border = "3px solid red"; // Assuming you want to set a red border for valid emails
    } else {
        emailInput.style.border = "0px"; // Assuming you want to remove the border for invalid emails
    }
});

passwordInput.addEventListener('change',(event)=>{
    const value = event.target.value;
    const minmum8digitRegex = /^.{8,}$/

    if(!minmum8digitRegex.test(value)){
        passwordInput.style.border = "3px solid red"; // Assuming you want to set a red border for valid emails
    } else {
        passwordInput.style.border = "0px"; // Assuming you want to remove the border for invalid emails
    } 

})



const validateEmail = (email)=>{
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    return emailRegex.test(email);
}