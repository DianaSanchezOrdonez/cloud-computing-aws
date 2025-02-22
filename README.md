# Proyecto de Cloud Computing: Microservicios con Contenedores en AWS

## Descripción del Proyecto
Este proyecto implementa una arquitectura de **microservicios** utilizando **contenedores** en AWS para la empresa de **aditivos de cemento**. 

## Tecnologías Utilizadas
- **Lenguaje:** Python (FastAPI)
- **Base de datos:** MySQL
- **Contenedores:** Docker
- **Orquestación de contenedores:** Docker Compose
- **Infraestructura en la nube:** Amazon Web Services (AWS)
- **Servicios de AWS:**
  - EC2 (Instancias para los microservicios)

## Arquitectura del Proyecto
El sistema está compuesto por los siguientes microservicios:

1. **Servicio de Clientes:** Gestiona los clientes de la empresa.
2. **Servicio de Productos:** Maneja el catálogo de productos.
3. **Servicio de Órdenes:** Administra las compras realizadas por los clientes.

Cada microservicio corre en un **contenedor independiente** y se comunica con otros servicios a través de peticiones HTTP.

## Despliegue en AWS
### Requisitos Previos
- Cuenta en AWS
- AWS CLI configurado
- Docker y Docker Compose

### Pasos para el Despliegue
1. **Configurar la infraestructura en AWS:**
   - Crear una instancia **EC2** para alojar los contenedores de microservicios.
   - Configurar **grupos de seguridad** para permitir el tráfico entre los microservicios y el acceso público necesario.
   - Crear una base de datos **MySQL** con Adminer.
2. **Configurar la instancia de EC2:**
   - Conectarse por SSH a la instancia.
   - Clonar el repositorio del proyecto.

## Endpoints Principales
- **Clientes:** `http://<IP-EC2>:8000/customers`
- **Productos:** `http://<IP-EC2>:8002/products`
- **Órdenes:** `http://<IP-EC2>:8001/orders`

## Integrantes del Proyecto
- **[Maria Grados]** 
- **[Yina Solis]**
- **[Paola Casabona]** 
- **[Diana Sanchez]**
- **[Robert Buleje]**

## Mejoras Futuras
- Implementación de Kubernetes para mejor escalabilidad.
- Uso de AWS Lambda para algunas operaciones serverless.
- Mejorar la seguridad con AWS Secrets Manager.

---
### ¡Listo para llevar la empresa de aditivos de cemento a la nube con microservicios escalables en AWS! 🚀

