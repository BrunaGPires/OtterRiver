import mysql.connector
from datetime import datetime


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='jogo_lontra'
        )
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                score INT NOT NULL,
                date VARCHAR(255) NOT NULL,
                time_seconds INT DEFAULT 0,
                time_display VARCHAR(10) DEFAULT '00:00'
            )
        ''')
        self.connection.commit()

    def save(self, score_dict: dict):
        if 'date' not in score_dict:
            score_dict['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if 'time_seconds' not in score_dict:
            score_dict['time_seconds'] = 0
        if 'time_display' not in score_dict:
            score_dict['time_display'] = '00:00'

        query = 'INSERT INTO dados (name, score, date, time_seconds, time_display) VALUES (%(name)s, %(score)s, %(date)s, %(time_seconds)s, %(time_display)s)'
        self.cursor.execute(query, score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        self.cursor.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10')
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()