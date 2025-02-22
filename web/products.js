const api_url = "http://34.224.158.46:8002"
const table = document.querySelector("tbody")
const form = document.getElementById("form-product")
const modal = new bootstrap.Modal(document.getElementById("addProductModal"))
let product_edit_id = null

const get_products = async () => {
	try {
		const response = await fetch(`${api_url}/products`)
		const { products } = await response.json()
		table.innerHTML = ""
		products.forEach((product) => {
			const row = document.createElement("tr")
			row.innerHTML = `
                <td>${product.id}</td>
                <td>${product.sku}</td>
                <td>${product.name}</td>
                <td>${product.description || "N/A"}</td>
                <td>${product.price}</td>
                <td>${product.category_name}</td>
								<td>${product.status}</td>
                <td>
                  <button class="btn btn-warning btn-sm edit-btn" data-id="${
						product.id
					}">Editar</button>
                  <button class="btn btn-danger btn-sm delete-btn" data-id="${
						product.id
					}">Eliminar</button>
                </td>
            `
			table.appendChild(row)
		})
	} catch (error) {
		console.error("Error loading products", error)
	}
}

// Fetch and store categories
const get_categories = async () => {
	try {
		const response = await fetch(`${api_url}/categories`)
		const data = await response.json()
		categories = data.categories

		const categorySelect = document.getElementById("category-select")
		categorySelect.innerHTML = ""

		categories.forEach((category) => {
			categorySelect.innerHTML += `<option value="${category.id}">${category.name}</option>`
		})
	} catch (error) {
		console.error("Error fetching categories:", error)
	}
}

document.addEventListener("DOMContentLoaded", get_products)

document
	.getElementById("addProductModal")
	.addEventListener("shown.bs.modal", get_categories);
