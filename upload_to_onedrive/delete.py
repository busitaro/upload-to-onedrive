import requests
import json

from graph_auth import read_token
from graph_auth import ApiError


def delete(user_id: str, target_path: str):
    item_info = __get_item_information(user_id, target_path)
    return __delete_file(user_id, item_info["id"])


def empty_folder(user_id: str, target_forlder_path: str):
    # 子アイテムの情報を取得
    item_info = __get_item_information(user_id, target_forlder_path)
    children = __get_children_item(user_id, item_info["id"])["value"]

    for child in children:
        __delete_file(user_id, child["id"])


def __delete_file(user_id: str, item_id: str):
    # リクエスト先設定
    header = {"Authorization": f"Bearer {read_token()}"}
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/drive/items/{item_id}"

    # APIの実行
    response = requests.delete(url, headers=header)

    # レスポンスのチェック
    if response.status_code not in [204]:
        raise ApiError(response)

    return response


def __get_item_information(user_id: str, target_path: str):
    # リクエスト先設定
    header = {"Authorization": f"Bearer {read_token()}"}
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/drive/root:/{target_path}"

    # APIの実行
    response = requests.get(url, headers=header)

    # レスポンスのチェック
    if response.status_code not in [200]:
        raise ApiError(response)

    return json.loads(response._content.decode("utf-8"))


def __get_children_item(user_id: str, target_folder_id: str):
    # リクエスト先設定
    header = {"Authorization": f"Bearer {read_token()}"}
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/drive/items/{target_folder_id}/children"

    # APIの実行
    response = requests.get(url, headers=header)

    return json.loads(response._content.decode("utf-8"))
