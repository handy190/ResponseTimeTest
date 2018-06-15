
from enum import Enum, unique

@unique
class Activities(Enum):
    """
        自定义Activity枚举类，用来存放需要测试的activity集合
        注意：activity的书写顺序即为用例执行顺序（因为按照遍历顺序来执行用例），如需改动用例执行顺序在此处改动即可
    """

    MESSAGE = "com.android.mms/.ui.ConversationList"

    # MESSAGE = "com.google.android.apps.messaging/.ui.ConversationListActivity"

    CONTACTS = "com.android.contacts/.activities.PeopleActivity"

    CAMERA = "com.mediatek.camera/.CameraLauncher"

    GALLERY = "com.android.gallery3d/.app.GalleryActivity"

    SETTINGS = "com.android.settings/.Settings"

    MUSIC = "com.android.music/.MusicBrowserActivity"

    CALCULATOR = "com.android.calculator2/.Calculator"

    SYSTEM_CLOCK = "com.android.deskclock/.DeskClock"

    FILE_MANAGER = "com.mediatek.filemanager/.FileManagerOperationActivity"

    BROWSER = "com.android.browser/.BrowserActivity"

    DIALER = "com.android.dialer/.DialtactsActivity"

    QQ = "com.tencent.mobileqq/.activity.SplashActivity"

    WECHAT = "com.tencent.mm/.app.WeChatSplashActivity"

    TENCENT_VIDEO = "com.tencent.news/com.tencent.news.activity.SplashActivity"

    JD_SHOPPING = "com.jingdong.app.mall/.MainFrameActivity"

    DOUYIN = "com.ss.android.ugc.aweme/.main.MainActivity"

    TAOBAO = "com.taobao.taobao/com.taobao.tao.homepage.MainActivity3"

    TENCENT_NEWS = "com.tencent.news/.activity.SplashActivity"

    ALIPAY = "com.eg.android.AlipayGphone/.AlipayLogin"

    XIAOXIAOLE = "com.happyelements.AndroidAnimal.qq/com.happyelements.hellolua.MainActivity"