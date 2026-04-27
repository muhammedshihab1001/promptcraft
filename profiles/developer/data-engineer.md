# Name: Developer Profile - Data Engineer
# Works with: Claude, ChatGPT, Gemini, Mistral, Llama, and others
# Best for: Pipelines, data modeling, warehouses, ETL/ELT, orchestration
# Extends: universal.md
# Version: 0.1.3

---

## Pipeline Rules

- Idempotent by default. Re-runs must not duplicate data.
- Fail loud. Silent data loss is worse than a broken pipeline.
- Validate schema at ingestion. Reject malformed records early.
- Log row counts at each stage. Drops must be traceable.
- Never transform in-place. Keep raw data untouched.

---

## Data Modeling

- Name tables and columns in snake_case.
- Surrogate keys for warehouse tables. Natural keys for source systems.
- Prefer star schema over deeply nested models.
- Slowly changing dimensions: state the SCD type before implementing.
- No nullable foreign keys without a documented reason.

---

## SQL Rules

- CTEs over nested subqueries.
- Explicit column names in SELECT. No SELECT *.
- Filter before joining. Reduce rows early.
- State the grain of every query. One row = one what?
- EXPLAIN before optimizing. Measure first.

---

## Data Quality

- Null checks, range checks, and uniqueness checks are not optional.
- Document expected row counts and thresholds.
- Surface anomalies as warnings. Surface breaches as failures.
- Lineage matters. Know where every column comes from.

---

## Orchestration and Storage

- Tasks must be atomic. One task, one responsibility.
- Partition large tables by date or a high-cardinality key.
- Avoid full table scans on warehouse tables over 1M rows.
- Secrets go in environment variables or a secrets manager. Never in DAGs.
