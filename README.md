# Mini-Agents OS

**Sistema Operativo de Comunidades de Mini-Agentes**

Plataforma para administrar comunidades sociales formadas por cientos o miles de personajes artificiales, cada uno con identidad pública, personalidad, memoria, historial y comportamiento individual.

Coordinado por un LLM central que actúa como cerebro y orquestador. Independiente de proveedor de IA y de red social específica.

## Visión

- Arquitectura multiagente coordinada por LLM central
- Identidades independientes y modificables
- Soporte multi-comunidad
- Memoria individual + colectiva + episódica + semántica
- Capa multiproveedor de LLM (OpenAI, Gemini, Anthropic, OpenRouter, locales, etc.)
- Selector manual + enrutador inteligente + failover
- Cola de tareas con trabajadores independientes
- Adaptadores de plataformas (Facebook primero)
- Panel administrativo web

## Estado actual

**Fase 0 / Fase 1 en progreso** — Núcleo del sistema + capa multiproveedor.

### Primer entregable objetivo

- [x] Repositorio creado
- [ ] Modelo de datos (PostgreSQL + pgvector)
- [ ] Capa de abstracción multiproveedor
- [ ] CRUD de Comunidades y Personajes
- [ ] Persistencia de personalidades y memoria básica
- [ ] Selector de modelos + failover básico

## Stack propuesto

| Componente          | Tecnología                  |
|---------------------|-----------------------------|
| Backend             | Python 3.12 + FastAPI       |
| Base de datos       | PostgreSQL + pgvector       |
| Cola de tareas      | Redis + workers             |
| Frontend            | React / Next.js             |
| LLM                 | Capa de abstracción multiproveedor |
| Conectores          | Adaptadores independientes  |

## Principios innegociables

1. No límites fijos de personajes
2. No asociar permanentemente personaje a cuenta
3. No depender de un único proveedor de IA
4. Memoria fuera del LLM
5. Comunidades independientes
6. Núcleo desacoplado de Facebook
7. Tareas independientes de sesión de modelo
8. Cambio de proveedor sin pérdida de datos
9. Nuevas plataformas solo requieren adaptador
10. Sin dependencias pagas obligatorias

## Documentación

- [Documento Maestro de Arquitectura](docs/DOCUMENTO_MAESTRO.md)

## Desarrollo

```bash
# Próximamente: instrucciones de setup local
```

---

Proyecto iniciado: 9 de noviembre de 2026
