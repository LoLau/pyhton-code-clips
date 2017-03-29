from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'lg'
# 创建对象的基类
Base = declarative_base()
DBSession = None


def init_db():
    # 初始化数据库连接
    engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/py')

    Base.metadata.create_all(engine)

    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)


# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'
    # 表的结构
    id = Column(String(10), primary_key=True)
    name = Column(String(20), nullable=False, unique=True)


def add_user():
    session = DBSession()
    new_user = User(id='1', name='marry')
    session.add(new_user)
    session.commit()


def query_user(user_id):
    session = DBSession()
    user_query = session.query(User).filter(user_id).one()
    session.close()

    return user_query


def query_users():
    session = DBSession()
    user_list = session.query(User).all()
    session.close()

    return user_list

if __name__ == '__main__':
    init_db()
    add_user()

# user = query_user('1')
# print(user.name)
