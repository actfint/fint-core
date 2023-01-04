#  Copyright (c) 2023 actfint
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4

from pydantic import BaseModel


class User(BaseModel):
    user_id: str
