from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Classe para gerenciar as configurações da aplicação.
    Ela lê as variáveis de um arquivo .env.
    """
    model_config = SettingsConfigDict(
        env_file='.env',   
        extra='ignore'     
    )

    DATABASE_URL: str  
    API_SECRET_KEY: str
    API_ALGORITHM: str



settings = Settings()
