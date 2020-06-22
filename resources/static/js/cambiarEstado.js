function cambiarEstadoComedero() {
    $.ajax({
        url: "/granjaIoT/cambiar_estado_comedero",
        type: 'GET',
        success: function (res) {
            if ($("#texto_comedero").hasClass("text-danger")) {
                document.getElementById("texto_comedero").className = "text-success";
                document.getElementById("boton_comedero").className = "btn btn-danger btn-lg";
                document.getElementById("texto_comedero").innerHTML = "Comedero abierto";
                document.getElementById("boton_comedero").innerText = "Cerrar comedero";
            } else {
                document.getElementById("texto_comedero").className = "text-danger";
                document.getElementById("boton_comedero").className = "btn btn-success btn-lg";
                document.getElementById("texto_comedero").innerHTML = "Comedero cerrado";
                document.getElementById("boton_comedero").innerText = "Abrir comedero";
            }
        },
        error: function (e) {
            alert("Error en el envio de los datos");
        }
    });
}


function cambiarEstadoBebedero() {
    $.ajax({
        url: "/granjaIoT/cambiar_estado_bebedero",
        type: 'GET',
        success: function (res) {
            if ($("#texto_bebedero").hasClass("text-danger")) {
                document.getElementById("texto_bebedero").className = "text-success";
                document.getElementById("boton_bebedero").className = "btn btn-danger btn-lg";
                document.getElementById("texto_bebedero").innerHTML = "Bebedero abierto";
                document.getElementById("boton_bebedero").innerText = "Cerrar bebedero";
            } else {
                document.getElementById("texto_bebedero").className = "text-danger";
                document.getElementById("boton_bebedero").className = "btn btn-success btn-lg";
                document.getElementById("texto_bebedero").innerHTML = "Bebedero cerrado";
                document.getElementById("boton_bebedero").innerText = "Abrir bebedero";
            }
        },
        error: function (e) {
            alert("Error en el envio de los datos");
        }
    });
}