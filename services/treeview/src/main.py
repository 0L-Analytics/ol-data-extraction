import datetime
import json

from ol_fyi import get_address_parent_relations_olfyi, build_tree
from config import Config


if __name__ == "__main__":
    rows = get_address_parent_relations_olfyi()

    raw_data_dict = {}
    result_list = []
    
    for row in rows:
        raw_data_dict[row[2]] = {
            "parent": row[1],
            "timestamp": row[3],
            "datetime": f"{datetime.datetime.fromtimestamp(row[3] / 1000000, datetime.timezone.utc)}"
        }
    
    # print(raw_data_dict)

    for address in raw_data_dict.keys():
        result_list.append({"account": address, "parent_tree": build_tree(raw_data_dict, address)}) 

    # print(result_list)

    with open(f'{Config.DATA_PATH}data.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)