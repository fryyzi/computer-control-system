document.addEventListener('DOMContentLoaded', function() {
    let loginBtn = document.querySelector('.Login_bnt');
    let modal = document.getElementById('loginModal');
    let closeBtn = document.querySelector('#loginModal .close');

    let Reg_modal = document.getElementById("RegisterModal")
    let Reg_close = document.querySelector("#RegisterModal .close")
  
    loginBtn.addEventListener('click', function() {
      modal.style.display = 'block';
      Reg_modal.style.display = 'none'
    });
  
    closeBtn.addEventListener('click', function() {
      modal.style.display = 'none';
    });
  });