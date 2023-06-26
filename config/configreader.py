from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    bot_token: str
    postgres_dsn: PostgresDsn
    tshock_server_host: str
    tshock_server_port: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = Config()
