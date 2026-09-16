from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

    foundry_project_endpoint: str = Field(
        validation_alias="FOUNDRY_PROJECT_ENDPOINT"
    )
    foundry_model: str = Field(
        default="gpt-4.1",
        validation_alias="FOUNDRY_MODEL",
    )

    content_understanding_endpoint: str = Field(
        validation_alias="AZURE_CONTENTUNDERSTANDING_ENDPOINT"
    )
    content_understanding_analyzer_id: str = Field(
        default="shopping-list-image-v1",
        validation_alias="CONTENT_UNDERSTANDING_ANALYZER_ID",
    )
    content_understanding_completion_model: str = Field(
        default="gpt-4.1",
        validation_alias="CONTENT_UNDERSTANDING_COMPLETION_MODEL",
    )

    application_insights_connection_string: str | None = Field(
        default=None,
        validation_alias="APPLICATIONINSIGHTS_CONNECTION_STRING",
    )
    enable_instrumentation: bool = Field(
        default=True,
        validation_alias="ENABLE_INSTRUMENTATION",
    )
    enable_sensitive_data: bool = Field(
        default=False,
        validation_alias="ENABLE_SENSITIVE_DATA",
    )

    agent_name: str = "shopping-agent"


@lru_cache
def get_settings() -> Settings:
    return Settings()