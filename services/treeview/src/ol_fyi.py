import clickhouse_connect

from config import Config
from typing import Dict, List, AnyStr


def get_address_parent_relations_olfyi():

    query=f"""
        SELECT
            "create_account"."version",
            hex("user_transaction"."sender") as "parent",
            hex("create_account"."created_address") as "address",
            "create_account"."timestamp_usecs"
        FROM "create_account"
        LEFT JOIN "user_transaction" ON "user_transaction"."version" = "create_account"."version"
        """

    client = clickhouse_connect.get_client(
        host = Config.OLFYI_HOST,
        port = Config.OLFYI_PORT,
        username = Config.OLFYI_USERNAME,
        password = Config.OLFYI_PASSWORD,
        database = Config.OLFYI_DATABASE
    )

    result = client.query(query)

    return result.result_rows


def build_tree(dictionary: Dict, address: AnyStr) -> List:

    list_out = []
    current = address

    while True:
        list_out.append(dictionary[current]['parent'])
        current = dictionary[current]['parent']

        if current == '00000000000000000000000000000000':
            break
    
    list_out.reverse()

    return list_out
