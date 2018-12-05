#简单
# import wordcloud
#
# w = wordcloud.WordCloud(width=1000,height=500,background_color='white')
#
# w.generate('life is short you need python')
# w.to_file('2.png')

#复杂
#coding:utf-8h.jpg
import jieba
import wordcloud
from scipy.misc import imread
img = imread('../h.jpg')


includes = ['将军','却说','二人','不可','荆州','如此','不能',
            '商议','如何','主公','军士','左右','军马','引兵',
            '次日','大喜','天下','于是','东吴','今日','不敢',
            '魏兵','人马','不知','汉中','陛下','一人','众将',
            '只见','蜀兵','大叫','上马','此人','后人','城中']
def get_text():
    f = open('../三国演义.txt',encoding='utf-8',errors='ignore').read()
    words = jieba.lcut(f)
    ls = []
    for i in words:
        if len(i)==1 or i in includes:
            continue
        elif i in ['丞相']:
            ls.append('曹操')
        elif i in ['孔明曰','孔明']:
            ls.append('诸葛亮')
        elif i in ['玄德曰', '玄德']:
            ls.append('刘备')
        elif i in ['关公', '云长']:
            ls.append('关羽')
        elif i in ['都督']:
            ls.append('周瑜')
        else:
            ls.append(i)
    return ' '.join(ls)

txt = get_text()
w = wordcloud.WordCloud(font_path = 'C:/Users/Windows/fonts/simkai.ttf',width=1000,height=500,background_color='white',mask=img)
w.generate(txt)
w.to_file('hm.jpg')
