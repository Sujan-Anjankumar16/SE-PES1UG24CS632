"""Manage tower maintenance records and service status."""


import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE towers ("
    "id INTEGER PRIMARY KEY, site TEXT, "
    "last_service INTEGER, faults INTEGER)"
)

Service_Count = 0


def add_tower(site, last_service, faults=0):
    """Add a tower record to the database."""
    query = (
        "INSERT INTO towers (site, last_service, faults) "
        "VALUES (?, ?, ?)"
    )
    conn.execute(query, (site, last_service, faults))
    conn.commit()


def service_tower(tower_id, year):
    """Record a tower service and reset its fault count."""
    try:
        cursor = conn.execute(
            "UPDATE towers SET last_service = ?, faults = 0 WHERE id = ?",
            (year, tower_id),
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"Service failed: {error}")
        return False


def overdue(year):
    """Return tower sites overdue for service in the given year."""
    rows = conn.execute("SELECT site, last_service FROM towers").fetchall()
    result = []
    for site, last in rows:
        if year - last >= 2:
            result.append(site)
    return result


def risk_level(tower_id):
    """Return the risk level for the specified tower."""
    row = conn.execute(
        "SELECT faults FROM towers WHERE id = ?", (tower_id,)
    ).fetchone()

    if row is None:
        return "unknown"
    if row[0] > 3:
        return "high"
    return "normal"


def snapshot():
    """Return a snapshot of all tower records."""
    return conn.execute("SELECT * FROM towers").fetchall()


def main():
    """Run the tower maintenance demonstration."""
    service_count = 0
    add_tower("Ridge-A", 2021, 5)
    add_tower("Coast-B", 2024)

    if service_tower(2, 2025):
        service_count += 1

    total = len(snapshot())
    print(overdue(2025), risk_level(1), total, service_count)


main()
