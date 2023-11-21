function login(event) {
  event.preventDefault();
  
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // Перевірка, чи правильний логін та пароль
  if (username === "Fryyzi" && password === "1234567") {
    localStorage.setItem("username", username);
    window.location.href = "profile.html";
    localStorage.setItem("firstName");
    localStorage.setItem("lastName", "Хомнюк");
  } else {
    alert("Невірний логін або пароль");
  }
}