from sqlalchemy import create_engine
from sqlalchemy.sql import text
import psycopg2
import allure
@allure.epic('Тестирование интерфейса сервиса YouGile')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('UI-тесты на авторизацию, управлению проектами и задачами')
class Test:
    def test(self):
        skript={"select by id": text("select * from company where id=14737")}
        db_url = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'
        db=create_engine(db_url)
        with db.connect() as connection:
            result = connection.execute(skript["select by id"])
        print(result.fetchall())
        assert result.fetchall()[0][0] == 14737
