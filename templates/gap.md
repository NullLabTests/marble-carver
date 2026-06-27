# Known gaps

> **Last updated:** {{YYYY-MM-DD}}
> **Maintainer:** {{Your name or agent ID}}

Gaps are honest, temporary, and specific. A gap is not a failure — it is a
carving that hasn't been made yet.

---

## Gap format

```yaml
id: {{GAP-001}}
description: "{{Specific, precise description of what we don't know}}"
assumption: "{{What we are currently assuming instead (if anything)}}"
importance: {{critical | important | nice_to_know}}
related_attempts: [attempt_001, attempt_003]
related_refs: [KEY_002]
status: {{open | partially_resolved | closed}}
resolved_by: {{attempt or audit note that closed this gap}}
date_opened: {{YYYY-MM-DD}}
date_closed: {{YYYY-MM-DD}}
```

---

## Open gaps

### {{GAP-001}}: {{Short title}}

- **Description:** {{}}
- **Current assumption:** {{}}
- **Importance:** {{}}
- **Related attempts:** {{}}
- **Opened:** {{}}

### {{GAP-002}}: {{Short title}}

- **Description:** {{}}
- **Current assumption:** {{}}
- **Importance:** {{}}
- **Related attempts:** {{}}
- **Opened:** {{}}

---

## Closed gaps

### {{GAP-XXX}}: {{Short title}} ✅

- **Resolved by:** {{attempt_XXX.md}} / {{audit_XXX.md}}
- **Resolution:** {{What we now know}}
- **Closed:** {{YYYY-MM-DD}}
