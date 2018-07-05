
from enum import Enum, unique


@unique
class Activities(Enum):
    """
        自定义Activity枚举类，用来存放需要测试的activity集合
        注意：activity的书写顺序即为用例执行顺序（因为按照遍历顺序来执行用例），如需改动用例执行顺序在此处改动即可
    """

    # MESSAGE = "com.android.mms/.ui.ConversationList"

    MESSAGE = "com.google.android.apps.messaging/.ui.ConversationListActivity"

    CONTACTS = "com.android.contacts/.activities.PeopleActivity"

    CAMERA = "com.mediatek.camera/.CameraLauncher"

    GALLERY = "com.android.gallery3d/.app.GalleryActivity"

    SETTINGS = "com.android.settings/.Settings"

    MUSIC = "com.android.music/.MusicBrowserActivity"

    # CALCULATOR = "com.android.calculator2/.Calculator"

    CALCULATOR = "com.google.android.calculator/com.android.calculator2.Calculator"

    SYSTEM_CLOCK = "com.android.deskclock/.DeskClock"

    FILE_MANAGER = "com.mediatek.filemanager/.FileManagerOperationActivity"

    BROWSER = "com.android.browser/.BrowserActivity"

    DIALER = "com.android.dialer/.DialtactsActivity"

    # QQ
    QQ = "com.tencent.mobileqq/.activity.SplashActivity"

    # 微信
    WECHAT = "com.tencent.mm/com.tencent.mm.ui.LauncherUI"

    # 抖音
    DOUYIN = "com.ss.android.ugc.aweme/.main.MainActivity"

    # 快手
    KUAISHOU = "com.smile.gifmaker/com.yxcorp.gifshow.HomeActivity"

    # 优酷
    YOUKU = "com.youku.phone/com.youku.ui.activity.HomePageActivity"

    # 爱奇艺
    AIQIYI = "com.qiyi.video/org.qiyi.android.video.MainActivity"

    # 淘宝
    TAOBAO = "com.taobao.taobao/com.taobao.tao.homepage.MainActivity3"

    # 腾讯新闻
    TENCENT_NEWS = "com.tencent.news/.activity.SplashActivity"

    # 支付宝
    ALIPAY = "com.eg.android.AlipayGphone/.AlipayLogin"

    # 美团
    MEITUAN = "com.sankuai.meituan/com.meituan.android.pt.homepage.activity.MainActivity"

    # 消消乐
    XIAOXIAOLE = "com.happyelements.AndroidAnimal.qq/com.happyelements.hellolua.MainActivity"

