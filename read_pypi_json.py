import json


def read_pypi_json(file_path):
    # 打开并读取JSON文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 打印 last_update 时间
    #last_update = data.get('last_update', 'Unknown')
    last_update=data["last_update"]
    print("upgate_time:" +last_update)
    #print(f"Last Update: {last_update}")

    # 打印前 10 个项目的名称
    print("Top 10 Projects:")
    for i, project in enumerate(data.get('rows', [])[:10], start=1):
        print(f"{i}. {project.get('project', 'Unknown')}")


if __name__ == "__main__":
    file_path = 'top-pypi-packages-30-days.min.json'
    read_pypi_json(file_path)