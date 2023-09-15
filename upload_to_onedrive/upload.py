import requests

from graph_auth import read_token
from graph_auth import ApiError


def upload(user_id: str, upload_file_path: str, upload_dest_file_path: str):
    # リクエスト先設定
    header = {"Authorization": f"Bearer {read_token()}"}
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/drive/items/root:/{upload_dest_file_path}:/content"

    # APIの実行
    response = requests.put(url, data=read_file(upload_file_path), headers=header)

    # レスポンスのチェック
    if response.status_code not in (200, 201):
        raise ApiError(response)

    return response


def read_file(file_path: str) -> bytes:
    """
    ファイルの内容をバイナリで読込む

    Returns
    -------
    0: bytes
        ファイル内容
    """
    with open(file_path, "rb") as file:
        file_content = file.read()
    return file_content
