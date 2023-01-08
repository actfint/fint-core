#  Copyright (c) 2023 actfint
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
from typing import Any, Dict, Optional, Tuple

from pydantic import BaseModel
from starlette.websockets import WebSocket


class User(BaseModel):
    user_id: str
    permissions: Optional[Dict[str, Any]]


class Anonymous(User):
    user_id: str = "anonymous"


def current_user():
    return Anonymous()


def websocket_auth(websocket: WebSocket) -> Optional[Tuple[WebSocket, User]]:
    return websocket, Anonymous()


async def update_user():
    async def _(*args, **kwargs):
        pass

    return _
