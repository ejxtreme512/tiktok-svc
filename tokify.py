from TikTokApi import TikTokApi
from gevent import monkey
monkey.patch_all()
import string
import random


verifyFp = 'verify_kp3dk3o5_vO4w3sVy_2RCe_4SqH_BBuY_VINzWCvoX0GN'
did = ''.join(random.choice(string.digits) for num in range(10))


api = TikTokApi.get_instance(
    custom_verifyFp=verifyFp, use_test_endpoints=True, custom_did=did)

# dict_keys(['id', 'desc', 'createTime', 'video', 'author', 'music', 'challenges', 'stats', 'duetInfo', 'originalItem', 'officalItem', 'textExtra', 'secret', 'forFriend', 'digged', 'itemCommentStatus', 'showNotPass', 'vl1', 'itemMute', 'authorStats', 'privateItem', 'duetEnabled', 'stitchEnabled', 'shareEnabled', 'isAd'])
def trending():
    return api.trending()


def video_by_tiktok(tiktok):
    video_bytes = api.get_video_by_tiktok(tiktok)
    with open('tiktok_' + tiktok['id']+ '.mp4', 'wb') as o:
        o.write(video_bytes)


def get_tiktok_by_id(id):
    return api.get_tiktok_by_id(id)

# def get_tiktok_s_v_web_id():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     }
#     session = requests.Session()
#     response = session.get('http://www.tiktok.com')
#     print(session.cookies.get_dict())

# if __name__ == "__main__":
#     params = {}
#     trending = get_trending()
#     first_tiktok = trending[0]
#     get_video_by_tiktok(first_tiktok)