import os
import re  # 正则表达式提取文件
import jsonpath  # 解析json数据
import requests  # 发送请求
import pandas as pd  # 存取文件
import datetime  # 转换时间用


def trans_time(v_str):
    """转换GMT时间为标准格式"""
    GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
    ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
    return ret_time


def get_weibo_list(v_key_word, v_max_page):
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
    }

    for page in (1, v_max_page + 1):
        print('---开始爬取第{}页微博---'.format(page))
        # 请求地址
        url = 'https://m.weibo.cn/api/container/getIndex'
        # 请求参数
        params = {
            "containerid": "100103type=1&q={}".format(v_key_word),
            "page_type": "searchall",
            "page": page
        }
        # 发送请求
        r = requests.get(url, headers=headers, params=params)
        print(r.status_code)
        # print(r.json())
        # 解析json数据
        cards = r.json()["data"]["cards"]
        # 微博内容
        text_list = jsonpath.jsonpath(cards, '$..mblog.text')
        # 正则表达式数据清洗
        dr = re.compile(r'<[^>]+>', re.S)
        text2_list = []
        if not text_list:
            continue
        if type(text_list) == list and len(text_list) > 0:
            for text in text_list:
                text2 = dr.sub('', text)
                print(text2)
                text2_list.append(text2)
        # 微博创建时间
        time_list = jsonpath.jsonpath(cards, '$..mblog.created_at')
        time_list = [trans_time(v_str=i) for i in time_list]
        # 微博作者
        author_list = jsonpath.jsonpath(cards, '$..mblog.user.screen_name')
        # 微博id
        id_list = jsonpath.jsonpath(cards, '$..mblog.id')
        # 微博bid
        bid_list = jsonpath.jsonpath(cards, '$..mblog.bid')
        # 转发数
        reposts_count_list = jsonpath.jsonpath(cards, '$..mblog.reposts_count')
        # 评论数
        comments_count_list = jsonpath.jsonpath(cards, '$..mblog.comments_count')
        # 点赞数
        attitudes_count_list = jsonpath.jsonpath(cards, '$..mblog.attitudes_count')

        df = pd.DataFrame({
            '页码': [page] * len(id_list),
            '微博id': id_list,
            '微博作者': author_list,
            '发布时间': time_list,
            '微博内容': text2_list,
            '转发数': reposts_count_list,
            '评论数': comments_count_list,
            '点赞数': attitudes_count_list
        })
        if os.path.exists(v_weibo_file):
            header = None
        else:
            header = ['页码', '微博id', '微博作者', '发布时间', '微博内容', '转发数', '评论数', '点赞数']

        # 保存到csv文件
        df.to_csv(v_weibo_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
        print('csv文件{}保存成功'.format(v_weibo_file))


if __name__ == '__main__':
    # 爬取前几页
    max_search_page = 100
    search_key_word = '调休'
    v_weibo_file = '微博清单_{}_前{}页.csv'.format(search_key_word, max_search_page)
    # 如果csv文件已经存在，先删除
    if os.path.exists(v_weibo_file):
        os.remove(v_weibo_file)
        print('微博清单已经存在，已删除{}'.format(v_weibo_file))
    # 调用爬取微博函数
    get_weibo_list(v_key_word=search_key_word, v_max_page=max_search_page)
    # 数据清洗-去重
    df = pd.read_csv(v_weibo_file)
    # 删除重复数据
    df.drop_duplicates(subset=['微博id'], inplace=True, keep='first')
    # 再次保存到文件中
    df.to_csv(v_weibo_file, index=False, encoding='utf_8_sig')
    print('数据清洗完成')
