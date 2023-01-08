#  Copyright (c) 2023 actfint
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/8

from typing import Optional, Tuple

from starlette.websockets import WebSocket

from .auth import User
from .logger import logger

logger.warning("Using Anonymous user, everyone can access this server")


class Anonymous(User):
    user_id: str = "anonymous"


def current_user():
    logger.warning("Using Anonymous user, everyone can access this server")
    return Anonymous()


def websocket_auth(websocket: WebSocket) -> Optional[Tuple[WebSocket, User]]:
    logger.warning("Using Anonymous user, everyone can access this server")
    return websocket, Anonymous()


async def update_user():
    async def _(*args, **kwargs):
        pass

    return _
