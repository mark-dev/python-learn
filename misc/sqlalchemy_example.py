from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CrawlerDAO:
    engine = None

    def __init__(self,connection_string) -> None:
        self.engine = create_engine(connection_string)

    def listUsers(self, search_str):
        result = self.engine.execute(text("SELECT id,bio,rating from crawler_data where bio like :q limit 100"),
                                     q='%' + search_str + '%')
        return result