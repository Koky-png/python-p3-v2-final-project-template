from database import connect_db, get_cursor, commit_and_close


def create_user(name, email, location):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("INSERT INTO users (name, email, location) VALUES (?, ?, ?)",
                       (name, email, location))
        conn.commit()
        cursor.execute("SELECT id, name, email, location FROM users WHERE email=?", (email,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
    finally:
        commit_and_close(conn)

def update_user(user_id, name=None, email=None, location=None):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        if name:
            cursor.execute("UPDATE users SET name=? WHERE id=?", (name, user_id))
        if email:
            cursor.execute("UPDATE users SET email=? WHERE id=?", (email, user_id))
        if location:
            cursor.execute("UPDATE users SET location=? WHERE id=?", (location, user_id))
        conn.commit()
        cursor.execute("SELECT id, name, email, location FROM users WHERE id=?", (user_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error updating user: {e}")
    finally:
        commit_and_close(conn)

def delete_user(user_id):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")
        return False
    finally:
        commit_and_close(conn)

def get_user_by_email(email):
    conn = connect_db()
    if conn is None:
        return None
    cursor = get_cursor(conn)
   
    try:
        cursor.execute("SELECT id, name, email, location FROM users WHERE email=?", (email,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error fetching user by email: {e}")
    finally:
        commit_and_close(conn)

