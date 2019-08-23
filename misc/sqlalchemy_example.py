from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/tcrawler')

class DataBaseWrapper:
    def listUsers(self):
        result = engine.execute("SELECT id,bio,rating from crawler_data where bio like '%%велоси%%' limit 100")
        return result