from TikTokApi import TikTokApi
import random
import io
import string
from gevent import monkey
monkey.patch_all()


custom_verify_fp = 'verify_kow9scyc_MbZkKA9W_IyVN_4KoG_Bbs3_dOiZmXemrTz3'
did = ''.join(random.choice(string.digits) for num in range(10))


api = TikTokApi.get_instance(
    custom_verifyFp=custom_verify_fp, use_test_endpoints=False, custom_did=did)


def tiktoks_by_user(username, count=30):
    return api.by_username(username, count=count)


def tiktoks_by_trending(count=30):
    # Return a list of trending tiktoks
    return api.trending(count=count)


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


def user_by_username(user):
    return api.get_user(user)


def tiktok_by_id(id):
    return api.get_tiktok_by_id(id)


# def get_tiktok_s_v_web_id():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     }
#     session = requests.Session()
#     response = session.get('http://www.tiktok.com')
#     print(session.cookies.get_dict())
