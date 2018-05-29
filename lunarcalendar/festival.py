# -*- coding: utf-8 -*-
''' all included festivals are defined here '''
from __future__ import unicode_literals
import datetime
from dateutil.easter import easter
from dateutil.rrule import rrule, MONTHLY, SU, TH
from .converter import Lunar
from .basefestival import Festival
from .solarterm import QingMing, DongZhi


# ######### Solar Festival ##########


NewYear = Festival(
        lambda year: datetime.date(year, 1, 1),
        en="New Year's Day",
        zh_hans="元旦,新年",
        )

Valentine = Festival(
        lambda year: datetime.date(year, 2, 14),
        en="Valentine's Day",
        zh_hans="情人节",
        )

WomenDay = Festival(
        lambda year: datetime.date(year, 3, 8),
        en="Women's Day",
        zh_hans="妇女节",
        )

ArborDay = Festival(
        lambda year: datetime.date(year, 3, 12),
        en="Arbor Day",
        zh_hans="植树节",
        )

ChingMing = Festival(
        lambda year: QingMing(year),
        en="Ching Ming Festival",
        zh_hans="清明节,踏青节",
        )

LabourDay = Festival(
        lambda year: datetime.date(year, 5, 1),
        en="Labour Day",
        zh_hans="劳动节",
        )

YouthDay = Festival(
        lambda year: datetime.date(year, 5, 4),
        en="Youth Day in China",
        zh_hans="青年节",
        )

NurseDay = Festival(
        lambda year: datetime.date(year, 5, 12),
        en="International Nurses Day",
        zh_hans="护士节",
        )

MotherDay = Festival(
        lambda year: rrule(MONTHLY, count=1, bymonth=5, byweekday=SU(2), dtstart=datetime.datetime(year, 5, 1))[0].date(),
        en="Mother's Day",
        zh_hans="母亲节",
        )

ChildrenDay = Festival(
        lambda year: datetime.date(year, 6, 1),
        en="Children's Day",
        zh_hans="儿童节",
        )

FatherDay = Festival(
        lambda year: rrule(MONTHLY, count=1, bymonth=6, byweekday=SU(3), dtstart=datetime.datetime(year, 6, 1))[0].date(),
        en="Father's Day",
        zh_hans="父亲节",
        )

TeacherDay = Festival(
        lambda year: datetime.date(year, 9, 10),
        en="Teacher's Day",
        zh_hans="教师节,老师节",
        )

NationDay = Festival(
        lambda year: datetime.date(year, 10, 1),
        en="National Day of the People's Republic of China",
        zh_hans="国庆节",
        )

Halloween = Festival(
        lambda year: datetime.date(year, 10, 31),
        en="Halloween",
        zh_hans="万圣节前夜",
        )

Thanksgiving = Festival(
        lambda year: rrule(MONTHLY, count=1, bymonth=11, byweekday=TH(4), dtstart=datetime.datetime(year, 11, 1))[0].date(),
        en="Thanksgiving Day",
        zh_hans="感恩节"
        )

ChristmasEve = Festival(
        lambda year: datetime.date(year, 12, 24),
        en="Christmas Eve",
        zh_hans="平安夜,圣诞夜,圣诞节前夕",
        )

ChristmasDay = Festival(
        lambda year: datetime.date(year, 12, 25),
        en="Christmas Day",
        zh_hans="圣诞节,圣诞,耶诞节,基督弥撒"
        )

Easter = Festival(
        lambda year: easter(year),
        en="Easter",
        zh_hans="复活节,主复活日",
        )

# ######### Lunar Festival ##########


LaBa = Festival(
        lambda year: Lunar(year, 12, 8).to_date(),
        en="LaBa Festival",
        zh_hans="腊八节",
        )

NewYearEve = Festival(
        lambda year: Lunar(year+1, 1, 1).to_date() - datetime.timedelta(days=1),
        en="New Year's Eve",
        zh_hans="除夕,除夕夜,大年夜,年夜,年三十,除夜,岁除,大晦日",
        )

ChineseNewYear = Festival(
        lambda year: Lunar(year, 1, 1).to_date(),
        en="Chinese New Year",
        zh_hans="春节,中国新年,年结,岁首,新春,正旦,正月朔日,过新年,过年")

Lantern = Festival(
        lambda year: Lunar(year, 1, 15).to_date(),
        en="Lantern Festival",
        zh_hans="元宵节,上元节,小正月,元夕,灯节,灯笼节",
        )

DragonHead = Festival(
        lambda year: Lunar(year, 2, 2).to_date(),
        en="Dragon Head Festival",
        zh_hans="龙抬头,龙头节,春龙节,春耕节,农事节",
        )

DragonBoat = Festival(
        lambda year: Lunar(year, 5, 5).to_date(),
        en="Dragon Boat Festival",
        zh_hans="端午节,龙舟节,端阳节,端日节,午日节,粽子节,五日节,五月节,天中节,菖蒲节",
        )

Qixi = Festival(
        lambda year: Lunar(year, 7, 7).to_date(),
        en="Qixi Festival",
        zh_hans="七夕节,七巧节,乞巧节,七姐诞,七娘生",
        )

Ghost = Festival(
        lambda year: Lunar(year, 7, 15).to_date(),
        en="Ghost Festival",
        zh_hans="中元节,鬼节,施孤,七月半,盂兰盆节",
        )

MidAutumn = Festival(
        lambda year: Lunar(year, 8, 15).to_date(),
        en="Mid-Autumn Festival",
        zh_hans="中秋节,月夕,秋节,仲秋节,八月节,八月会,追月节,玩月节,拜月节,女儿节,团圆节,赏月节",
        )

ChongYang = Festival(
        lambda year: Lunar(year, 9, 9).to_date(),
        en="Double Ninth Festival",
        zh_hans="重阳节,重九节,晒秋节,踏秋,老人节,敬老节,登山节,登高节",
        )

Hanyi = Festival(
        lambda year: Lunar(year, 10, 1).to_date(),
        en="HanYi Festival",
        zh_hans="寒衣节,十月朝,祭祖节,冥阴节,鬼头日,包袱节",
        )

DongJie = Festival(
        lambda year: DongZhi(year),
        en="Dong Festival",
        zh_hans="冬至,冬节",
        )


# ######### data ##########
festivals = [f for _, f in globals().items() if isinstance(f, Festival)]
zh_festivals = [f for f in festivals if f.get_lang('zh_hans')]
