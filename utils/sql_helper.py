import pymysql


def is_user_deleted_in_backend(db_config, username):
    """Checks if a user is deleted from the database."""
    connection = pymysql.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        db=db_config["db"]
    )
    try:
        with connection.cursor() as cursor:
            query = "SELECT COUNT(*) AS count FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result["count"] == 0  # User is deleted if count is 0
    finally:
        connection.close()
