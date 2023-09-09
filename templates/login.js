// Login functionalities
// console.log(`connected`)
document.getElementById('login-btn').addEventListener('click', function(){
    const emailInput = document.getElementById('email');
    const email = emailInput.value;

    const passwordInput = document.getElementById('password');
    const password = passwordInput.value;
     if (email === 'abc@blog.com' && password === 'abc123'){
         window.location.href = 'index.html';
     } else {
         alert('Your email and password is wrong.');
     }
 })