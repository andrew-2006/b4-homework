# импортируем необходимые нам модули
import datetime
# импортируем библиотеку sqlalchemy и некоторые сущности из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения  с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"

# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
    #Описывает структуру таблицы user
    
    # указываем имя таблицы
    __tablename__ = 'user'
    # Задаем колонки в формате
    # название_колонки = sa.Column(ТИП_КОЛОНКИ)
    # идентификатор строки
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():
    #Устанавливает соединение к базе данных, создает таблицы, если их еще нет, и возвращает объект сессии 

    #создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    #создаем фабрику сессию
    Base.metadata.create_all(engine)
    #cоздаем сессию
    session = sessionmaker(engine)
    return session()

def request_data():
    #Запрашивает у пользователя данные и добавляет их в список users
    
    print("Привет! Я запишу твои данные!")
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Какого ты пола? (варианты: Male, Female) ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")    
    birthdate = input("Введи, пожалуйста, дату рождения в формате ГГГГ-ММ-ДД. Например, 1999-01-01: ")
    height = input("А какой у тебя рост в метрах? (Для разделения целой и десятичной части используется точка)")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    #Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Твои данные сохранены в базе данных. Спасибо!")

if __name__ == "__main__":
    main()
