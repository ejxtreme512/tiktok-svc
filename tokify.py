from TikTokApi import TikTokApi

import string
import random
import requests


verifyFp = 'verify_kow9scyc_MbZkKA9W_IyVN_4KoG_Bbs3_dOiZmXemrTz3'
did = ''.join(random.choice(string.digits) for num in range(10))


api = TikTokApi.get_instance(
    custom_verifyFp=verifyFp, use_test_endpoints=True, custom_did='')

# dict_keys(['id', 'desc', 'createTime', 'video', 'author', 'music', 'challenges', 'stats', 'duetInfo', 'originalItem', 'officalItem', 'textExtra', 'secret', 'forFriend', 'digged', 'itemCommentStatus', 'showNotPass', 'vl1', 'itemMute', 'authorStats', 'privateItem', 'duetEnabled', 'stitchEnabled', 'shareEnabled', 'isAd'])
def get_trending():
    tiktoks = api.trending()
    return tiktoks


def get_video_by_tiktok(tiktok):
    video_bytes = api.get_video_by_tiktok(tiktok)
    with open('tiktok_' + tiktok['id']+ '.mp4', 'wb') as o:
        o.write(video_bytes)


def get_tiktok_by_id(id):
    return api.get_tiktok_by_id(id)

def get_tiktok_s_v_web_id():
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    session = requests.Session()
    response = session.get('http://www.tiktok.com'), headers=headers
    print(session.cookies.get_dict())

if __name__ == "__main__":
    params = {}
    print(get_tiktok_s_v_web_id())
