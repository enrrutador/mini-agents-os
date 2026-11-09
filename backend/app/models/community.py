"""Modelo de Comunidad."""

from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.character import Character


class Community(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Comunidad independiente de personajes."""

    __tablename__ = "communities"

    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    theme: Mapped[Optional[str]] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text)
    editorial_rules: Mapped[Optional[str]] = mapped_column(Text)
    activity_config: Mapped[Optional[str]] = mapped_column(Text)  # JSON como texto por ahora
    status: Mapped[str] = mapped_column(String(50), default="active", index=True)

    # Relaciones
    characters: Mapped[List["Character"]] = relationship(
        "Character",
        back_populates="community",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Community {self.name}>"
