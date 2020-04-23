import requests
import time
import random
import logging

bundle_id_file = 'bundle_ids'
bundle_id_array = {}
with open(bundle_id_file, 'r') as f:
    bundle_id_array = f.readlines()

for bundle_id_txt in bundle_id_array:
    bundle_id = bundle_id_txt.strip()
    time.sleep(random.random() * 5)
    logging.warning(bundle_id + "request timestamp:" + str(int(round(time.time()*1000))))
    try:
        url = "https://play.google.com/store/apps/details?id=%s" % bundle_id
        logging.warning(url)
        res = requests.get(url)
        enconding = requests.utils.get_encodings_from_content(res.text)
        html_doc = res.content
        html_str = str(html_doc)
        str_s = html_str.split('itemprop="genre"')[1].split('class')[0].strip().split('/')[-1].strip('"')
        logging.warning("app_id:" + bundle_id + ":::category:" + str_s)
    except:
        logging.error("there is no detail data for bundle_id:%s in google play" % bundle_id)
        continue