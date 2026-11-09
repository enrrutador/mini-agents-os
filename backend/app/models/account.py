"""Modelos de Cuenta administradora y Página social."""

from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.character import Character


class Account(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Cuenta administradora de plataformas."""

    __tablename__ = "accounts"

    identifier: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    platform: Mapped[str] = mapped_column(String(50), nullable=False, index=True)  # facebook | ...
    connection_status: Mapped[str] = mapped_column(String(50), default="disconnected")
    auth_method: Mapped[Optional[str]] = mapped_column(String(50))
    last_connection_at: Mapped[Optional[str]] = mapped_column(String(50))
    authorization_status: Mapped[str] = mapped_column(String(50), default="pending")
    notes: Mapped[Optional[str]] = mapped_column(Text)

    # Relaciones (muchos a muchos se modelará más adelante con tabla intermedia si hace falta)
    pages: Mapped[List["Page"]] = relationship(
        "Page",
        back_populates="account",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Account {self.identifier} ({self.platform})>"


class Page(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Página social asociada a un personaje."""

    __tablename__ = "pages"

    platform_page_id: Mapped[Optional[str]] = mapped_column(String(200), index=True)
    name: Mapped[str] = mapped_column(String(300), nullable=False)
    url: Mapped[Optional[str]] = mapped_column(String(500))
    avatar_url: Mapped[Optional[str]] = mapped_column(String(500))
    platform: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    connection_status: Mapped[str] = mapped_column(String(50), default="disconnected")
    capabilities: Mapped[Optional[str]] = mapped_column(Text)  # JSON de capacidades disponibles
    notes: Mapped[Optional[str]] = mapped_column(Text)

    account_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("accounts.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    # Relaciones
    account: Mapped[Optional["Account"]] = relationship("Account", back_populates="pages")
    character: Mapped[Optional["Character"]] = relationship(
        "Character",
        back_populates="page",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"<Page {self.name}>"
