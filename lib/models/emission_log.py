
from database import connect_db, get_cursor, commit_and_close

def log_emission(user_id, activity_id, duration, date, emissions):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("INSERT INTO emission_logs (user_id, activity_id, duration, date, emissions) VALUES (?, ?, ?, ?, ?)",
                       (user_id, activity_id, duration, date, emissions))
        conn.commit()
        cursor.execute("SELECT id, user_id, activity_id, duration, date, emissions FROM emission_logs WHERE user_id=?", (user_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error logging emission: {e}")
    finally:
        commit_and_close(conn)

def update_emission(emission_log_id, emissions=None, duration=None):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        if emissions:
            cursor.execute("UPDATE emission_logs SET emissions=? WHERE id=?", (emissions, emission_log_id))
        if duration:
            cursor.execute("UPDATE emission_logs SET duration=? WHERE id=?", (duration, emission_log_id))
        conn.commit()
        cursor.execute("SELECT id, user_id, activity_id, duration, date, emissions FROM emission_logs WHERE id=?", (emission_log_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error updating emission: {e}")
    finally:
        commit_and_close(conn)

def delete_emission(emission_log_id):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("DELETE FROM emission_logs WHERE id=?", (emission_log_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting emission: {e}")
        return False
    finally:
        commit_and_close(conn)

