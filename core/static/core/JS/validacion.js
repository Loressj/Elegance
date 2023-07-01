//VALIDACION RECUPERAR CONTRASEÑA
document
  .getElementById("resetPasswordForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var emailInput = document.getElementById("typeEmail");
    var email = emailInput.value;

    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("Por favor, introduce una dirección de correo electrónico válida.");
      return;
    }
    alert(
      "Se han enviado los pasos a seguir al correo indicado para restablecer la contraseña."
    );
    window.location.href = "/index.html";
  });
