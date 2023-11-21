document.addEventListener('DOMContentLoaded', function(){
    let Reg = document.querySelector(".register")
    let modal = document.getElementById("RegisterModal")
    let close = document.querySelector("#RegisterModal .close")

    let Log_modal = document.getElementById('loginModal');
    let closeBtn = document.querySelector('#loginModal .close');

    Reg.addEventListener("click", function(){
        modal.style.display = "block"
        Log_modal.style.display = "none"
    })

    close.addEventListener('click', function() {
        modal.style.display = 'none';
      });
})
