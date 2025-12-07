---
marp: true
theme: product-docs
paginate: true
footer: "Product Documentation | © 2025"
---

<style>
/* @theme product-docs */
section {
  font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  background-color: #ffffff;
  color: #0d1b2a;
  padding: 40px;
}

h1, h2, h3 {
  font-weight: 700;
  color: #0a4a7a;
}

footer {
  font-size: 12px;
  color: #666666;
}

/* Simple code styling */
pre code {
  font-size: 0.9rem;
  border-radius: 6px;
  padding: 8px 10px;
}

/* A custom class for highlight slides */
section.highlight {
  background: #e8f3ff;
  border-left: 8px solid #1b6ca8;
}
</style>

<!-- _class: lead -->

# Product Documentation Presentation  
### Maintainable, Version-Controlled, Multi-Format

**Author:** 24ds2000081@ds.study.iitm.ac.in  

---

# Why Marp for Product Documentation?

- Documentation stored as **plain Markdown**
- **Version control friendly** (Git, GitHub)
- Export to **HTML, PDF, PPTX** via Marp CLI
- Ideal for **engineering-heavy products**
- Easy collaboration and reviews via pull requests

---

<!-- _class: highlight -->

# Documentation Goals

- Single source of truth for product behavior  
- Consistent structure across modules  
- Easy to update for new releases  
- Automatable in CI/CD pipelines  

---

# System Architecture (Example)

```mermaid
flowchart TD
  A[Client App] --> B[API Gateway]
  B --> C[Microservice A]
  B --> D[Microservice B]
  C --> E[(Primary DB)]
  D --> F[(Analytics DB)]
