"""Modelos para la capa multiproveedor de LLM."""

from typing import Optional

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class LLMProvider(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Proveedor de inteligencia artificial."""

    __tablename__ = "llm_providers"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    display_name: Mapped[str] = mapped_column(String(150), nullable=False)
    base_url: Mapped[Optional[str]] = mapped_column(String(500))
    api_type: Mapped[str] = mapped_column(String(50), default="openai")  # openai | anthropic | gemini | custom
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_local: Mapped[bool] = mapped_column(Boolean, default=False)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    # Relaciones
    models: Mapped[list["LLMModel"]] = relationship(
        "LLMModel",
        back_populates="provider",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<LLMProvider {self.name}>"


class LLMModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Modelo específico de un proveedor."""

    __tablename__ = "llm_models"

    provider_id: Mapped[str] = mapped_column(
        ForeignKey("llm_providers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)  # ej: gpt-4o-mini
    display_name: Mapped[str] = mapped_column(String(200), nullable=False)
    technical_id: Mapped[str] = mapped_column(String(200), nullable=False)  # id exacto para la API
    max_context: Mapped[Optional[int]] = mapped_column(Integer)
    capabilities: Mapped[Optional[str]] = mapped_column(Text)  # JSON: ["chat", "tools", "vision"]
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    is_free: Mapped[bool] = mapped_column(Boolean, default=False)
    cost_input_per_1k: Mapped[Optional[float]] = mapped_column(Float)
    cost_output_per_1k: Mapped[Optional[float]] = mapped_column(Float)
    rate_limit_rpm: Mapped[Optional[int]] = mapped_column(Integer)
    priority: Mapped[int] = mapped_column(Integer, default=100)  # menor = más prioritario
    last_checked_at: Mapped[Optional[str]] = mapped_column(String(50))

    provider: Mapped["LLMProvider"] = relationship("LLMProvider", back_populates="models")

    def __repr__(self) -> str:
        return f"<LLMModel {self.name}>"


class ModelAssignment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Asignación de modelo a una función del sistema."""

    __tablename__ = "model_assignments"

    function_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )  # orchestration | complex_reasoning | content_generation | classification | fallback
    model_id: Mapped[str] = mapped_column(
        ForeignKey("llm_models.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    model: Mapped[Optional["LLMModel"]] = relationship("LLMModel")

    def __repr__(self) -> str:
        return f"<ModelAssignment {self.function_name}>"
