from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str = ""
    llm_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"

    langfuse_secret_key: str = ""
    langfuse_public_key: str = ""
    langfuse_host: str = ""

    weaviate_host: str = "localhost"
    weaviate_port: int = 8080
    weaviate_api_key: str = ""

    otel_exporter_otlp_endpoint: str = ""
    otel_service_name: str = "rag-observability"
    app_env: str = "production"
    app_version: str = "1.0.0"

    log_level: str = "INFO"
    cost_alert_threshold_usd: float = 0.05

    eval_faithfulness_min: float = 0.80
    eval_answer_relevancy_min: float = 0.75
    eval_context_precision_min: float = 0.70
    eval_context_recall_min: float = 0.70


settings = Settings()
