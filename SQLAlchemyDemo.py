from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'lg'


class DB:
    # 创建对象的基类
    Base = declarative_base()
    # 初始化数据库连接
    engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/py')

    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)

    # 定义User对象
    class User(Base):
        # 表的名字
        __tablename__ = 'user'
        # 表的结构
        id = Column(String(10), primary_key=True)
        name = Column(String(20), nullable=False, unique=True)

    @staticmethod
    def add_user():
        session = DB.DBSession()
        new_user = DB.User(id='1', name='marry')
        session.add(new_user)
        session.commit()

    @staticmethod
    def query_user(user_id):
        session = DB.DBSession()
        user_query = session.query(DB.User).filter(user_id).one()
        session.close()

        return user_query

    @staticmethod
    def query_users():
        session = DB.DBSession()
        user_list = session.query(DB.User).all()
        session.close()

        return user_list


if __name__ == '__main__':
    DB.add_user()
