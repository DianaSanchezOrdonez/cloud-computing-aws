const api_url = "http://34.224.158.46:8000/customers"
const table = document.querySelector("tbody")
const form = document.getElementById("form-client")
const modal = new bootstrap.Modal(document.getElementById("addProductModal"))
let client_edit_id = null

const get_customers = async () => {
	try {
		const response = await fetch(api_url)
		const { customers } = await response.json()
		table.innerHTML = ""
		customers.forEach((customer) => {
			const row = document.createElement("tr")
			row.innerHTML = `
                <td>${customer.id}</td>
                <td>${customer.email}</td>
                <td>${customer.first_name}</td>
                <td>${customer.last_name}</td>
                <td>${customer.phone || "N/A"}</td>
                <td>${customer.address}</td>
                <td>
                  <button class="btn btn-warning btn-sm edit-btn" data-id="${
						customer.id
					}">Editar</button>
                  <button class="btn btn-danger btn-sm delete-btn" data-id="${
						customer.id
					}">Eliminar</button>
                </td>
            `
			table.appendChild(row)
		})

		// Add events to the buttons after creating the table
		document.querySelectorAll(".edit-btn").forEach((btn) => {
			btn.addEventListener("click", () =>
				get_customer_by_id(btn.dataset.id)
			)
		})

		document.querySelectorAll(".delete-btn").forEach((button) => {
			button.addEventListener("click", delete_customer)
		})
	} catch (error) {
		console.error("Error loading customers", error)
	}
}

const get_customer_by_id = async (id) => {
	try {
		const response = await fetch(`${api_url}/${id}`)
		const { customer } = await response.json()

		document.getElementById("email").value = customer.email
		document.getElementById("first_name").value = customer.first_name
		document.getElementById("last_name").value = customer.last_name
		document.getElementById("phone").value = customer.phone || ""
		document.getElementById("address").value = customer.address

		client_edit_id = id // Save the customer ID to edit
		modal.show()
	} catch (error) {
		console.error(`Error loading the customer with ${id}`, error)
	}
}

const delete_customer = async (event) => {
	const customer_id = event.target.getAttribute("data-id")

	if (!confirm("Are you sure you want to delete this customer?")) {
		return
	}

	try {
		const response = await fetch(`${api_url}/${customer_id}`, {
			method: "DELETE",
		})

		if (response.ok) {
			alert("Customer deleted successfully!")
			get_customers() // Reload customer list
		} else {
			alert("Failed to delete customer.")
		}
	} catch (error) {
		console.error("Error deleting customer", error)
	}
}

form.addEventListener("submit", async function (event) {
	event.preventDefault()

	const customer = {
		email: document.getElementById("email").value,
		first_name: document.getElementById("first_name").value,
		last_name: document.getElementById("last_name").value,
		phone: document.getElementById("phone").value || null,
		address: document.getElementById("address").value,
	}

	try {
		if (client_edit_id) {
			await fetch(`${api_url}/${client_edit_id}`, {
				method: "PUT",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(customer),
			})
		} else {
			await fetch(api_url, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(customer),
			})
		}

		modal.hide()
		get_customers()
		form.reset()
		client_edit_id = null // Reset edit state
	} catch (error) {
		console.error("Error saving the customer", error)
	}
})

document.addEventListener("DOMContentLoaded", get_customers)
