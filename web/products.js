const enlace_api = "http://34.224.158.46:8002"

const solicitar_lista = () => {
	fetch(enlace_api + "/products")
		.then((response) => response.json())
		.then((json) => {
			const products = json.products
			const table = document.querySelector("tbody") // Selecciona el tbody para insertar filas
			table.innerHTML = "" // Limpia la tabla antes de poblarla

			products.forEach((product) => {
				const row = document.createElement("tr")

				row.innerHTML = `
                    <td>${product.id}</td>
                    <td>${product.sku}</td>
                    <td>${product.name}</td>
                    <td>${product.description}</td>
                    <td>$${product.price.toFixed(2)}</td>
                    <td>${product.category_id}</td>
                    <td>${product.status}</td>
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
