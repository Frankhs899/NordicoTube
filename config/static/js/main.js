console.log("El script main.js se ha cargado correctamente.");
var file_path_global;

//Obtiene datos del video
function obtenerInformacion() {
    console.log("El script main.js se ha cargado correctamente en obtener informacion.");
    var url = document.getElementById("urlInput").value;

    // Realizar la solicitud AJAX
    $.ajax({
        type: 'POST',
        url: '/obtener_informacion/',
        data: {
            'url': url,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            console.log("El script main.js se ha cargado correctamente en obtener informacion success.");
            // Actualizar el contenido en 'infoContainer'
            if ('video_info' in data) {
                $('#infoContainer #titulo').text(data.video_info.title);
                $('#infoContainer #duracion').text(data.video_info.duration);
            } else if ('error' in data) {
                // Manejar el error de alguna manera, por ejemplo, mostrar un mensaje de error
                console.error(data.error);
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            // Manejar errores de la solicitud AJAX
            console.error('Error en la solicitud AJAX:', textStatus, errorThrown);
        }
    });
}

//Descarga video
function iniciarDescarga(tipo) {
    console.log("El script main.js se ha cargado correctamente en descarga de video.");
    var url = document.getElementById("urlInput").value;

    // Muestra el modal con el mensaje 'Solicitud en trámite'
    mostrarModal('Solicitud en trámite por favor espere');

    // Realiza la solicitud AJAX para la descarga del video
    $.ajax({
        type: 'POST',
        url: '/video/',
        data: {
            'url': url,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data) {
            console.log("Respuesta exitosa:", data);
            if ('file_path' in data) {
                file_path = data.file_path; //OBTIENE file_path
                var baseUrl = window.location.origin;  // Obtiene la parte base de la URL (http://127.0.0.1:8000)
                var fileUrl = baseUrl + '/' + file_path;  // Construye la URL completa del archivo
                $('#linkContainer #descargaUsuario').attr('href', fileUrl);
                // Cambia el mensaje del modal a 'Solicitud realizada con éxito'
                mostrarModal('Solicitud realizada con éxito');
                // Muestra el botón para descargar el archivo
                $('#descargaUsuario').show();
            } else if ('error' in data) {
                // Muestra el mensaje de error en el modal
                mostrarModal('Ha ocurrido un error. Por favor, inténtelo más tarde.');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error en la solicitud AJAX:', textStatus, errorThrown);
            // Manejar errores de la solicitud AJAX
            console.error('Error en la solicitud AJAX:', textStatus, errorThrown);
        }
    });
}

//Funcion descarga audio
function iniciarDescargaA(tipo) {
    console.log("El script main.js se ha cargado correctamente en descarga de audio.");
    var url = document.getElementById("urlInput").value;

    // Muestra el modal con el mensaje 'Solicitud en trámite'
    mostrarModal('Solicitud en trámite por favor espere');

    // Realiza la solicitud AJAX para la descarga del video
    $.ajax({
        type: 'POST',
        url: '/audio/',
        data: {
            'url': url,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data) {
            console.log("Respuesta exitosa:", data);
            if ('file_path' in data) {
                file_path = data.file_path; //OBTIENE file_path
                var baseUrl = window.location.origin;  // Obtiene la parte base de la URL (http://127.0.0.1:8000)
                var fileUrl = baseUrl + '/' + file_path;  // Construye la URL completa del archivo
                $('#linkContainer #descargaUsuario').attr('href', fileUrl);

                // Cambia el mensaje del modal a 'Solicitud realizada con éxito'
                mostrarModal('Solicitud realizada con éxito');
                // Muestra el botón para descargar el archivo
                $('#descargaUsuario').show();
            } else if ('error' in data) {
                // Muestra el mensaje de error en el modal
                mostrarModal('Ha ocurrido un error. Por favor, inténtelo más tarde.');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error en la solicitud AJAX:', textStatus, errorThrown);
            // Manejar errores de la solicitud AJAX
            console.error('Error en la solicitud AJAX:', textStatus, errorThrown);
        }
    });
}


//Lanza modal
function mostrarModal(mensaje) {
    console.log("Función mostrarModal llamada con el mensaje:", mensaje);
    console.log("El script main.js se ha cargado correctamente en mostrar modal.");
    console.log("Mostrando modal con mensaje:", mensaje);
    // Actualiza el mensaje en el modal
    $('#mensajeModal').text(mensaje);
    // Muestra el modal
    $('#modal').removeClass('hidden');
    // $('#modal').addClass('is-active');
}

//Cierra modal
function cerrarModal() {
    console.log("El script main.js se ha cargado correctamente en cerrar modal.");
    // Cierra el modal
    $('#modal').addClass('hidden');
    // $('#modal').removeClass('is-active');
}

