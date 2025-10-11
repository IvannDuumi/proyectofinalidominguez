# 🧠 Proyecto Final Django — Iván Domínguez

## 📋 Descripción

Este proyecto fue desarrollado como **entrega final del curso de Python**.  
El objetivo fue construir una aplicación web completa con **registro de usuarios, autenticación, perfil personal editable y sistema de mensajería**, utilizando una arquitectura profesional basada en buenas prácticas de Django.

El sitio incluye un diseño oscuro con acentos dorados, navegación dinámica, y un sistema de plantillas reutilizable.

---

## 🚀 Funcionalidades principales

### 👤 Gestión de usuarios
- Registro de nuevos usuarios (`signup`)
- Inicio y cierre de sesión (`login` / `logout`)
- Perfil personal con:
  - Foto de avatar
  - Biografía
  - Fecha de nacimiento (con selector de calendario)
- Edición del perfil desde el sitio (`/accounts/profile/edit/`)

### 💬 Mensajería
- Acceso disponible solo para usuarios autenticados.
- Visualización del inbox (`/messaging/`).

### 🏠 Sitio principal
- Home con bienvenida personalizada (incluye nombre del usuario logueado)
- Secciones “Blog” y “Acerca de mí”
- Menú adaptable según el estado de autenticación
- Estilo coherente con `base.html` y diseño responsive.

---

