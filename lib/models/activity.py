
from database import connect_db, get_cursor, commit_and_close

def log_activity(name, emission_factor):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("INSERT INTO activities (name, emission_factor) VALUES (?, ?)",
                       (name, emission_factor))
        conn.commit()
        cursor.execute("SELECT id, name, emission_factor FROM activities WHERE name=?", (name,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error logging activity: {e}")
    finally:
        commit_and_close(conn)

def update_activity(activity_id, name=None, emission_factor=None):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        if name:
            cursor.execute("UPDATE activities SET name=? WHERE id=?", (name, activity_id))
        if emission_factor:
            cursor.execute("UPDATE activities SET emission_factor=? WHERE id=?", (emission_factor, activity_id))
        conn.commit()
        cursor.execute("SELECT id, name, emission_factor FROM activities WHERE id=?", (activity_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error updating activity: {e}")
    finally:
        commit_and_close(conn)

def delete_activity(activity_id):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("DELETE FROM activities WHERE id=?", (activity_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting activity: {e}")
        return False
    finally:
        commit_and_close(conn)

def get_activity_by_name(name):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("SELECT id, name, emission_factor FROM activities WHERE name=?", (name,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error fetching activity by name: {e}")
    finally:
        commit_and_close(conn)

