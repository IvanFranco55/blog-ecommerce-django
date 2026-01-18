# 📝 Django Blog CMS - Plataforma de Contenidos

Este proyecto es un Sistema de Gestión de Contenidos (CMS) desarrollado con **Django**. Permite la creación de artículos, interacción mediante comentarios y una gestión avanzada de perfiles de usuario con avatares personalizados.

El foco principal del proyecto fue implementar un sistema robusto de **autenticación y permisos**, asegurando que cada usuario solo pueda gestionar sus propios recursos.

🔗 **Demo en vivo:** [https://ivanf55.pythonanywhere.com](https://ivanf55.pythonanywhere.com)

---

## 🚀 Funcionalidades Clave

### 👤 Gestión de Usuarios (Auth)
* **Registro y Autenticación:** Sistema completo de Login, Logout y Registro de nuevos usuarios.
* **Perfiles Personalizados:** Cada usuario tiene su propia página de perfil.
* **Avatar:** Posibilidad de subir y editar una foto de perfil (imagen de avatar).
* **Edición de Datos:** Los usuarios pueden actualizar su información personal.

### ✍️ Artículos y Contenido
* **CRUD de Artículos:** Creación, Lectura, Actualización y Eliminado de posts.
* **Sistema de Permisos:** Lógica de seguridad donde **solo el autor** puede editar o borrar sus propios artículos.
* **Filtros y Búsqueda:** Herramientas para buscar artículos por categorías, fecha o palabras clave.

### 💬 Interacción (Comentarios)
* **Sistema de Comentarios:** Los usuarios logueados pueden comentar en los artículos.
* **Gestión de Comentarios:** Los usuarios pueden editar o eliminar sus propios comentarios.

---

## 🛠 Tecnologías Utilizadas

* **Backend:** Python, Django.
* **Frontend:** HTML5, CSS3, Bootstrap (Plantillas Jinja2).
* **Base de Datos:** SQLite (Entorno local) / MySQL (Producción).
* **Gestión de Archivos:** Manejo de archivos estáticos y media (imágenes de perfil).

---

## ⚙️ Instalación Local

Si querés correr este proyecto en tu propia máquina:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/IvanFranco55/blog-ecommerce-django.git](https://github.com/IvanFranco55/blog-ecommerce-django.git)
   cd blog-ecommerce-django
Crear un entorno virtual:

Bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Realizar migraciones:

Bash
python manage.py migrate
Correr el servidor:

Bash
python manage.py runserver
📸 Capturas de Pantalla
(Espacio reservado para capturas del Home, el Perfil de Usuario y la vista de Detalle del Artículo)

📫 Contacto
Ivan Franco - Backend Developer LinkedIn
