try:
    from models import SessionMetaData
    from exceptions import *
    from async_session import AsyncSession
    from sync_session import SyncSession
except ModuleNotFoundError:
    from .models import SessionMetaData
    from .exceptions import *
    from .async_session import AsyncSession
    from .sync_session import SyncSession
