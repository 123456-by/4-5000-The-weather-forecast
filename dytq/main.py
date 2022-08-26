import datetime
import logging

import requests

# enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# config
templete_id = ''
app_id = ''
app_secret = ''
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(app_id,app_secret)


def get_access_token():
    return requests.get(url).json().get('access_token')


love_start = datetime.datetime.strptime('yy-mm-dd', '%Y-%m-%d')  # 在一起的时候 格式不可错！例如：2023-09-21 填在第一个位置
now = datetime.datetime.now()

# already love days
love_days = (now - love_start).days

# birthday
birthday = datetime.datetime.strptime('yy-mm-dd', '%Y-%m-%d')  # 对方生日的时候 格式不可错！ 例如：2023-09-21 填在第一个位置
days_to_birthday = (birthday - now).days

# LEFT SOME TEXT U WANT TO DISPLAY
one_sentence = ''

# ur girls openid
touser = ''      #填写接收消息方的微信号


def wheater():
    return requests.get(
        'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=南昌').json()


def love_story():
    return requests.get('https://api.vvhan.com/api/love').text


data = {
    'touser': touser,
    'template_id': templete_id,
    'data': {
        'ur_sentence': {
            'value': one_sentence,
            'color': '#000'
        },
        'love_days': {
            'value': '我们已经恋爱了{}天啦 '.format(love_days),
            'color': '#000'
        },
        'days_to_birthday': {
            'value': '再过{}天就是你的生日啦!!!'.format(days_to_birthday) if days_to_birthday > 0 else '今天是宝宝的生日呀!!!',
            'color': '#000'
        },
        'weather': {
            'value': '今天天气：{}\n今天温度： 最低{}度,最高{}度\n今日阳光： 日出{},日落{}'.format(wheater().get('data')[0].get('narrative'),
                                                                          (wheater().get('data')[0].get('tem2')),
                                                                          (wheater().get('data')[0].get('tem1')),
                                                                          (wheater().get('data')[0].get('sunrise')),
                                                                          (wheater().get('data')[0].get('sunset'))),
            'color': '#000'
        },
        'love_story': {
            'value': love_story(),
            'color': '#FF0000'
        }
    }

}


def send_template_message():
    res = requests.post(
        'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(get_access_token()),
        json=data).json()
    if res.get('errcode') == 0:
        logger.info('send template message success')
        return res
    else:
        logger.error('send template message failed')
        logger.error(res)
        return res


if __name__ == '__main__':
    send_template_message()
