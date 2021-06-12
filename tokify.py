import string
import io
import random

from gevent import monkey
monkey.patch_all()
from TikTokApi import TikTokApi



verifyFp = 'verify_kpomzw4d_aUN9f4zp_j2tw_4Ujv_82bg_UbxY6yQiPFUH'
did = ''.join(random.choice(string.digits) for num in range(10))


api = TikTokApi.get_instance(
    custom_verifyFp=verifyFp, use_test_endpoints=False, custom_did=did)


def tiktok_by_id(id):
    return api.get_tiktok_by_id(id)


# This is a list of dictionaries. Each dictionary contains dict_keys(['id', 'desc', 'createTime', 'video', 'author', 'music', 'challenges', 'stats', 'duetInfo', 'originalItem', 'officalItem', 'textExtra', 'secret', 'forFriend', 'digged', 'itemCommentStatus', 'showNotPass', 'vl1', 'itemMute', 'authorStats', 'privateItem', 'duetEnabled', 'stitchEnabled', 'shareEnabled', 'isAd'])
def trending():
    # Return a list of trending tiktoks
    return api.trending()


def video_by_id(id):
    # Given an Id, return a downloadable tiktok mp4 file
    print('video by id')
    tiktok = tiktok_by_id(id)
    return video_by_tiktok(tiktok['itemInfo']['itemStruct'])


def video_by_tiktok(tiktok):
    print('video by tiktok')
    video_bytes = api.get_video_by_tiktok(tiktok)
    mem = io.BytesIO()
    mem.write(video_bytes)
    mem.seek(0)
    return mem


def tiktoks_by_user(username):
    count = 30
    tiktoks = api.byUsername(username, count=count)
    return tiktoks 

# def get_tiktok_s_v_web_id():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     }
#     session = requests.Session()
#     response = session.get('http://www.tiktok.com')
#     print(session.cookies.get_dict())


if __name__ == "__main__":
    user_videos = tiktoks_by_user('abbieherbert_')
    print(user_videos)
    