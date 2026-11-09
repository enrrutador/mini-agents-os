"""Modelos de Personaje y Ficha de Personalidad."""

from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.community import Community
    from app.models.account import Page


class Character(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Personaje individual con identidad propia."""

    __tablename__ = "characters"

    name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(150))
    avatar_url: Mapped[Optional[str]] = mapped_column(String(500))
    internal_biography: Mapped[Optional[str]] = mapped_column(Text)
    public_identity: Mapped[Optional[str]] = mapped_column(Text)
    linguistic_style: Mapped[Optional[str]] = mapped_column(Text)
    interests: Mapped[Optional[str]] = mapped_column(Text)  # JSON o texto
    status: Mapped[str] = mapped_column(
        String(50),
        default="en_preparacion",
        index=True,
    )  # en_preparacion | activo | inactivo | suspendido | pendiente_config | error_integracion
    activity_level: Mapped[int] = mapped_column(Integer, default=5)  # 1-10

    # FK
    community_id: Mapped[str] = mapped_column(
        ForeignKey("communities.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    page_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("pages.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    # Relaciones
    community: Mapped["Community"] = relationship("Community", back_populates="characters")
    page: Mapped[Optional["Page"]] = relationship("Page", back_populates="character")
    personality: Mapped[Optional["PersonalityProfile"]] = relationship(
        "PersonalityProfile",
        back_populates="character",
        uselist=False,
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Character {self.name}>"


class PersonalityProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Ficha de personalidad editable de un personaje."""

    __tablename__ = "personality_profiles"

    character_id: Mapped[str] = mapped_column(
        ForeignKey("characters.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )

    temperament: Mapped[Optional[str]] = mapped_column(String(100))
    expressiveness_level: Mapped[int] = mapped_column(Integer, default=5)  # 1-10
    typical_comment_length: Mapped[Optional[str]] = mapped_column(String(50))  # short | medium | long
    vocabulary: Mapped[Optional[str]] = mapped_column(Text)
    spelling_style: Mapped[Optional[str]] = mapped_column(String(50))  # formal | informal | con_errores
    emoji_usage: Mapped[Optional[str]] = mapped_column(String(50))  # none | low | medium | high
    preferred_topics: Mapped[Optional[str]] = mapped_column(Text)
    secondary_topics: Mapped[Optional[str]] = mapped_column(Text)
    interests: Mapped[Optional[str]] = mapped_column(Text)
    humor_type: Mapped[Optional[str]] = mapped_column(String(100))
    tendency_to_ask: Mapped[int] = mapped_column(Integer, default=5)  # 1-10
    tendency_to_reply: Mapped[int] = mapped_column(Integer, default=5)  # 1-10
    activity_level: Mapped[int] = mapped_column(Integer, default=5)  # 1-10
    social_relations_notes: Mapped[Optional[str]] = mapped_column(Text)

    # Relación
    character: Mapped["Character"] = relationship("Character", back_populates="personality")

    def __repr__(self) -> str:
        return f"<PersonalityProfile character={self.character_id}>"
