from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class DatabaseManager:
    """Manages database connections and sessions."""

    def __init__(self, dsn: str):
        self.engine = create_async_engine(dsn)
        self.session_factory = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get a database session. Caller must handle commit/rollback."""
        async with self.session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    async def close(self):
        """Close database connections."""
        await self.engine.dispose()
