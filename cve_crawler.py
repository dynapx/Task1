import requests
import json

def read_cve(keyword):

    try:
        r = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}')
        return r.json()
    except Exception as e:
        print(f"read cve error occurred:{keyword} {e}")
        return None


def read_keyword(filepath):
    with open(filepath, 'r') as file:
        keywords = [line.strip() for line in file if line.strip()]
    return keywords




def write_json(data,filepath):
    with open(filepath, 'w') as file:
       json.dump(data,file,indent=4)

def process_data(filepath):
    keywords = read_keyword(filepath)
    for keyword in keywords:
        cves = read_cve(keyword)
        write_json(cves, f"{keyword}.json")
        print(f"Processed {keyword}")



process_data("repos.txt")