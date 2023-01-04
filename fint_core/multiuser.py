#  Copyright (c) 2023 actfint
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4

from pathlib import Path


class MultiuserManager(object):
    async def get_user_file_path(self, user, path, *args, **kwargs) -> Path:
        raise NotImplementedError
