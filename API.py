from pydantic import BaseSettings, SecretStr

class sit(BaseSettings):
    bot_tok = SecretStr
    class config:
        env_file = '.env'
        env_coding = 'UTF-8'

config = sit()