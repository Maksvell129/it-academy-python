from abc import abstractmethod, ABC


class Database(ABC):
    @abstractmethod
    def save(self, **kwargs):
        raise NotImplementedError


class MySQLDatabase(Database):
    def save(self, user):
        pass


class PostgresSQLDatabase(Database):

    def save(self, user):
        pass


class OracleSQLDatabase(Database):
    def save(self, user):
        pass


class UserService:
    def __init__(self, database: Database | None = None):
        self.database = database if database else PostgresSQLDatabase()

    def save_user(self, user):
        self.database.save(user)


service1 = UserService()
service2 = UserService(database=MySQLDatabase())
service3 = UserService(database=OracleSQLDatabase())