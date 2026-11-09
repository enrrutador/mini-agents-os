# Documento Maestro · Versión 1.0

**PROYECTO: SISTEMA OPERATIVO DE COMUNIDADES DE MINI-AGENTES**

Documento maestro de arquitectura y desarrollo  
Versión: 1.0  
Fecha: 9 de noviembre de 2026

---

## 1. VISIÓN GENERAL

### 1.1. Objetivo

Desarrollar un sistema capaz de administrar comunidades sociales formadas por cientos o miles de personajes artificiales, cada uno con identidad pública, personalidad, memoria, historial y comportamiento individual.

Los personajes tendrán presencia en redes sociales existentes, comenzando por Facebook mediante sus Páginas.

Cada personaje podrá tener su propia identidad pública, publicar contenido, participar en conversaciones, comentar, reaccionar y mantener relaciones con otros participantes, utilizando las funciones que cada plataforma permita.

El sistema estará dirigido por un LLM central que actuará como cerebro y orquestador de todas las operaciones.

No se busca construir un chatbot ni una automatización convencional de publicaciones.

Se busca desarrollar un **sistema operativo de comunidades de agentes sociales**.

### 1.2. Principios fundamentales

1. Arquitectura multiagente coordinada por un LLM central.
2. Identidades independientes y modificables.
3. Administración de una cantidad variable de cuentas y Páginas.
4. Soporte para múltiples comunidades.
5. Memoria individual y colectiva.
6. Capacidad de utilizar múltiples proveedores y modelos de inteligencia artificial.
7. Independencia respecto del proveedor de LLM.
8. Infraestructura modular y escalable.
9. Optimización de recursos y costos.
10. Posibilidad de incorporar nuevas redes sociales sin reconstruir el sistema.

### 1.3. Escenario de referencia

Una comunidad temática sobre gatos con 600 personajes.

Cada personaje tiene: Nombre, Identidad pública, Página social asociada, Fotografía o avatar, Personalidad, Forma de expresarse, Intereses, Memoria individual, Historial de publicaciones, Relaciones con otros personajes, Nivel de actividad.

El sistema puede administrar esta comunidad y, simultáneamente, otras comunidades de temáticas completamente diferentes.

---

## 2. ARQUITECTURA GENERAL

El sistema se dividirá en seis grandes capas.

**Capa 1. Inteligencia central**  
LLM central · Enrutador de modelos · Planificador · Motor de decisiones · Gestión de personalidades · Memoria contextual · Evaluación de resultados

**Capa 2. Administración**  
Gestor de cuentas · Gestor de Páginas · Gestor de personajes · Gestor de comunidades · Administrador de relaciones · Planificador temporal

**Capa 3. Orquestación**  
Cola de tareas · Distribución de trabajos · Trabajadores independientes · Gestión de prioridades · Control de concurrencia · Recuperación de tareas

**Capa 4. Ejecución**  
Conectores de plataformas · Integraciones oficiales · Herramientas de lectura · Herramientas de publicación · Herramientas de interacción permitidas · Navegación asistida cuando corresponda

**Capa 5. Persistencia**  
Base de datos principal · Memoria individual · Memoria colectiva · Historial de actividad · Almacenamiento de archivos · Registro de eventos

**Capa 6. Interfaz**  
Panel administrativo · Administración de comunidades · Administración de personajes · Administración de cuentas y Páginas · Configuración de proveedores de IA · Monitoreo de tareas · Estadísticas y actividad

El sistema será independiente de una plataforma específica y de un proveedor específico de inteligencia artificial.

---

## 3. SISTEMA MULTI-LLM Y MULTIPROVEEDOR

Este módulo es uno de los componentes centrales del proyecto.

No se utilizará un único proveedor obligatorio.

El administrador podrá conectar varios proveedores, agregar diferentes modelos y seleccionar manualmente cuál utilizar.

### 3.1. Gestión de proveedores

El sistema deberá permitir registrar múltiples proveedores de inteligencia artificial.

Ejemplos: OpenAI, Google Gemini, Anthropic, OpenRouter, NVIDIA NIM, Proveedores compatibles con OpenAI API, Servidores locales, Otros.

### 3.2. Gestión de modelos

Cada proveedor podrá ofrecer varios modelos. El sistema registrará: Nombre del proveedor, Nombre del modelo, Identificador técnico, Endpoint, Tipo de API, Capacidades, Contexto máximo, Disponibilidad, Estado de conexión, Costos conocidos, Límites de utilización, Prioridad, Fecha de última comprobación.

### 3.3. Selector manual de modelos

Desde el panel administrativo se podrá seleccionar proveedor/modelo, cambiar en cualquier momento, asignar modelos por función (Orquestación, Razonamiento complejo, Generación de contenido, Clasificación, Respaldo).

### 3.4. Enrutador inteligente + Failover

Selección según tipo de tarea, capacidad, preferencia por gratuitos, costos, detección de errores/límites, cambio automático, reintentos controlados, registro del modelo utilizado.

El cambio de modelo no debe provocar pérdida de memoria ni duplicación de operaciones.

### 3.5. Independencia del proveedor

Las personalidades, memorias, tareas, relaciones y configuraciones no deben quedar almacenadas exclusivamente en el proveedor de IA. Toda esa información pertenece a la base de datos del proyecto.

---

## 4. LLM CENTRAL Y ORQUESTADOR

El LLM central será el cerebro operativo. Responsable de interpretar objetivos, planificar actividades, consultar información, utilizar herramientas y coordinar los diferentes módulos.

Utilizará herramientas mediante tool calling.

Contexto dinámico: no se enviará toda la información de todos los personajes. Solo personalidad, memoria relevante, publicación/conversación actual, relaciones pertinentes, contexto de comunidad e instrucción.

---

## 5-20. Resumen de módulos clave

- **Gestor de Identidades y Personajes**: sin límite artificial. Fichas de personalidad editables. Estados: En preparación, Activo, Inactivo, Suspendido, etc.
- **Gestor de Cuentas y Páginas**: separación estricta Cuenta ↔ Página ↔ Personaje. Relaciones muchos a muchos.
- **Sistema Multi-Comunidad**: independencia total entre comunidades.
- **Sistema de Memoria**: Individual + Colectiva + Episódica + Semántica + Estructurada.
- **Motor de Personalidad y Comportamiento**: voz reconocible, selección contextual de participantes, relaciones reales registradas, evolución diferenciada.
- **Motor de Orquestación y Tareas**: cola persistente, trabajadores independientes, concurrencia, reintentos, idempotencia.
- **Conectores de Redes Sociales**: adaptadores independientes. Facebook primero (Páginas). Nuevas plataformas solo requieren adaptador.
- **Base de Datos**: PostgreSQL + pgvector recomendado.
- **Panel Web**: Dashboard + secciones completas de administración y configuración multiproveedor.
- **Monitoreo**: logs estructurados, métricas por comunidad/personaje/proveedor/modelo.
- **Economía**: priorizar costo cero. Proveedores gratuitos, locales, caché, contextos compactos, modelos pequeños para tareas sencillas.

## Fases de desarrollo

1. Núcleo del sistema (modelo de datos + CRUD)
2. Infraestructura multi-LLM
3. Inteligencia y memoria
4. Motor de tareas
5. Integración social (Facebook)
6. Panel administrativo
7. Escalabilidad (pruebas hasta 600+ personajes)

## Principios que no deben cambiarse

1. No límites fijos de personajes
2. No asociar permanentemente un personaje a una cuenta
3. No depender de un único proveedor de IA
4. No almacenar la memoria exclusivamente dentro del LLM
5. No mezclar comunidades
6. No acoplar el cerebro a Facebook
7. No hacer que las tareas dependan de una sesión activa del modelo
8. No perder información al cambiar de proveedor
9. No reconstruir el sistema para incorporar nuevas plataformas
10. No introducir dependencias pagas obligatorias

---

**Resultado final esperado**: plataforma central capaz de administrar múltiples comunidades sociales con cientos o miles de personajes artificiales, cada uno con identidad, personalidad, memoria e historial propios. Un LLM central coordinará mediante herramientas. Multiproveedor, modular, persistente, escalable y adaptable a diferentes redes sociales.
