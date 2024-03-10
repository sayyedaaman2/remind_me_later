const showPasswordButton = document.getElementById('show-password-btn');
const emailInput = document.querySelector('input[name="email"]');
const passwordInput = document.querySelector('input[name="password"]');
const showPasswordIcon = document.getElementById('show-password-icon');
const formData = document.querySelector('form');



formData.addEventListener('submit',(event)=>{
    event.preventDefault();
    const formElements = event.target.elements;
    const formValues = {};

    for (let i = 0; i < formElements.length; i++) {
        const element = formElements[i];

        // Check if the element is an input field (you may need to adjust this condition based on your form structure)
        if (element.tagName === 'INPUT') {
            const name = element.name;
            const value = element.value;
            formValues[name] = value;
        }
    }

    console.log("Form submit");
    console.log(formValues);
})

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