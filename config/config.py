POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "admin"
POSTGRES_DATABASE = "test_rpn"

POSTGRES_CONNECTION_STRING = "postgresql://%s:%s@%s:%s/%s" % (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DATABASE,
)
