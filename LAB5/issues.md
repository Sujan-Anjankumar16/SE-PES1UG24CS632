# Lab 5 — Static Code Analysis Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security | 18–22 | The INSERT statement now uses placeholders rather than inserting values directly into SQL text. | Use a parameterized query with `?`, then pass values separately to `conn.execute()`. |
| Unsafe pickle deserialization | Security | 63–65 | The snapshot function no longer uses `pickle.loads()` or `pickle.dumps()`; it returns query results directly. | Remove `pickle` and return `fetchall()` results directly. |
| Hardcoded password | Security | 4–13 | The final code has no hardcoded password; the old `NOC_PASSWORD` value has been removed. | Remove the unused hardcoded credential from the source. |
| Specific exception handling | Code quality | 35–37 | The service operation catches `sqlite3.Error` rather than a broad `Exception`. | Catch the database-specific exception and return `False` if the operation fails. |
| Missing-row handling | Bug prevention | 52–57 | `risk_level()` checks whether the query returned `None` before accessing `row[0]`. | Return `"unknown"` when the tower ID does not exist. |
| Function naming convention | Code quality | 16, 26, 40, 50, 63, 68 | Function names use snake_case, such as `add_tower`, `service_tower`, and `risk_level`. | Use snake_case for function names and update their call sites. |
| Long SQL statements | Formatting | 7–11, 29–32, 52–54 | SQL statements and function calls are split across multiple lines for readability and line-length compliance. | Use parenthesized strings and multiline function calls. |
| Unnecessary else | Code quality | 58–60 | `risk_level()` returns directly after the `if` block, without an unnecessary `else`. | Return `"normal"` after the `if` block. |
| Unnecessary serialization | Maintainability | 63–65 | SQLite query results are returned directly; serializing and deserializing them is unnecessary. | Remove the unnecessary pickle serialization and deserialization. |
| Missing docstrings | Code quality | 16–17, 26–27, 40–41, 50–51, 63–64, 68–69 | Functions have concise docstrings describing their purpose. | Add a short docstring to each function describing its purpose. |