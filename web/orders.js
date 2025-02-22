const api_url = "http://34.224.158.46:8001"
const table = document.querySelector("tbody")
const modal = new bootstrap.Modal(document.getElementById("addProductModal"))

const get_orders = async () => {
	try {
		const response = await fetch(`${api_url}/orders`)
		const { orders } = await response.json()
		table.innerHTML = ""

		orders.forEach((order) => {
			const row = document.createElement("tr")
			row.innerHTML = `
                <td>${order.id}</td>
                <td>${order.cliente_id}</td>
                <td>${order.status}</td>
                <td>$${order.total_amount.toFixed(2)}</td>
                <td>
                  <button class="btn btn-info btn-sm detail-btn" data-id="${
						order.id
					}">Ver Detalle</button>
                </td>
            `
			table.appendChild(row)

			const detailRow = document.createElement("tr")
			detailRow.id = `order-detail-${order.id}`
			detailRow.style.display = "none"
			detailRow.innerHTML = `
				<td colspan="5">
					<strong>Detalle Orden:</strong>
					<table class="table table-bordered mt-2">
						<thead>
							<tr>
								<th>Producto</th>
								<th>Cantidad</th>
								<th>Precio Unitario</th>
								<th>Total</th>
							</tr>
						</thead>
						<tbody id="order-items-${order.id}">
							<tr><td colspan="4" class="text-center">Cargando...</td></tr>
						</tbody>
					</table>
				</td>
			`
			table.appendChild(detailRow)
		})

		document.querySelectorAll(".detail-btn").forEach((btn) => {
			btn.addEventListener("click", async (e) => {
				const orderId = e.target.getAttribute("data-id")
				const detailRow = document.getElementById(
					`order-detail-${orderId}`
				)
				const itemsTable = document.getElementById(
					`order-items-${orderId}`
				)

				if (detailRow.style.display === "table-row") {
					detailRow.style.display = "none"
					return
				}

				detailRow.style.display = "table-row"

				try {
					const response = await fetch(`${api_url}/order_items`)
					const { order_items } = await response.json()

					itemsTable.innerHTML = ""
					const itemsFiltered = order_items.filter(
						(item) => item.order_id == orderId
					)

					if (itemsFiltered.length === 0) {
						itemsTable.innerHTML = `<tr><td colspan="4" class="text-center">No hay productos en esta orden</td></tr>`
					} else {
						itemsFiltered.forEach((item) => {
							const itemRow = `
								<tr>
									<td>${item.product_id}</td>
									<td>${item.quantity}</td>
									<td>$${item.unit_price.toFixed(2)}</td>
									<td>$${item.total_price.toFixed(2)}</td>
								</tr>
							`
							itemsTable.innerHTML += itemRow
						})
					}
				} catch (error) {
					console.error("Error loading order detail", error)
				}
			})
		})
	} catch (error) {
		console.error("Error loading orders", error)
	}
}

document.addEventListener("DOMContentLoaded", get_orders)
