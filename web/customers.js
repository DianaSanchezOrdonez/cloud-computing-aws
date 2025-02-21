const enlace_api = "http://34.224.158.46:8000"

const solicitar_lista = () => {
	fetch(enlace_api + "/customers")
		.then((response) => response.json())
		.then((json) => {
			const customers = json.customers
			const table = document.querySelector("tbody") // Selecciona el tbody para insertar filas
			table.innerHTML = "" // Limpia la tabla antes de poblarla

			customers.forEach((customer) => {
				const row = document.createElement("tr")

				row.innerHTML = `
                    <td>${customer.id}</td>
                    <td>${customer.email}</td>
                    <td>${customer.first_name}</td>
                    <td>${customer.last_name}</td>
                    <td>${customer.phone}</td>
                    <td>${customer.address}</td>
                    <td>
                        <button class="btn btn-warning btn-sm">Editar</button>
                        <button class="btn btn-danger btn-sm">Eliminar</button>
                    </td>
                `

				table.appendChild(row)
			})
		})
		.catch((err) => {
			console.error("Error al obtener productos:", err)
		})
}

// Llamar a la función cuando cargue la página
document.addEventListener("DOMContentLoaded", solicitar_lista)
