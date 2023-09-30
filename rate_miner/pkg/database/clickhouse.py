import clickhouse_driver


class ClickHouse:
    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        self.connection = clickhouse_driver.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("SHOW DATABASES;")
        print(self.cursor.fetchall())
