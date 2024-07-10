from graph_auth import ApiError

from .delete import __get_item_information


def exist(user_id: str, target_path: str) -> bool:
    """
    ファイルの存在チェックを行う

    Params
    -------
    user_id: str
        ユーザID
    target_path: str
        True: ファイルが存在 / False: ファイルが存在しない
    """
    try:
        __get_item_information(user_id, target_path)
        result = True
    except ApiError:
        result = False
    return result
