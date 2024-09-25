function realizarReserva() {
    const nombre = document.getElementById('nombre').value;
    const fecha = document.getElementById('fecha').value;
    const horario = document.getElementById('horario').value;

    fetch('/api/reservas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre, fecha, horario }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Reserva creada: ' + data.message);
        // Limpiar el formulario o hacer otras acciones
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
