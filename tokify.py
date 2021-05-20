from TikTokApi import TikTokApi

import string
import random

did = ''
verifyFp = 'verify_kow9scyc_MbZkKA9W_IyVN_4KoG_Bbs3_dOiZmXemrTz3'


api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True, custom_did='')

# dict_keys(['id', 'desc', 'createTime', 'video', 'author', 'music', 'challenges', 'stats', 'duetInfo', 'originalItem', 'officalItem', 'textExtra', 'secret', 'forFriend', 'digged', 'itemCommentStatus', 'showNotPass', 'vl1', 'itemMute', 'authorStats', 'privateItem', 'duetEnabled', 'stitchEnabled', 'shareEnabled', 'isAd'])


# for tok in tiktoks:
#     print(tok['id'])

def getTrending():
    tiktoks = api.trending()
    print(tiktoks[0].keys())


def getTok(id):
    pass



if __name__ == "__main__":
    params = {}
    getTrending()


