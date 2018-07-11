
from enum import Enum, unique


@unique
class Activities(Enum):
    """
        自定义Activity枚举类，用来存放需要测试的activity集合
        注意：activity的书写顺序即为用例执行顺序（因为按照遍历顺序来执行用例），如需改动用例执行顺序在此处改动即可
    """

    # MESSAGE = "com.android.mms/.ui.ConversationList"

    # MESSAGE = "com.android.mms/com.qiku.android.mms.ui.MmsConversationListActivity"

    MESSAGE = "com.google.android.apps.messaging/.ui.ConversationListActivity"

    CONTACTS = "com.android.contacts/.activities.PeopleActivity"

    # CONTACTS = "com.qiku.android.contacts/com.qiku.android.contacts.ui.main.ContactMainActivity"

    # CAMERA = "com.mediatek.camera/.CameraLauncher"
    CAMERA = "com.android.camera2/com.android.camera.CameraLauncher"
    # CAMERA = "com.android.camera/com.android.camera.Camera"

    GALLERY = "com.android.gallery3d/.app.GalleryActivity"

    # GALLERY = "com.android.gallery3d/com.android.gallery3d.app.Gallery"

    SETTINGS = "com.android.settings/.Settings"

    MUSIC = "com.android.music/.MusicBrowserActivity"


    # MUSIC = "com.qiku.music/com.qiku.music.main.activity.MainActivity"

    # CALCULATOR = "com.android.calculator2/.Calculator"
    CALCULATOR = "com.google.android.calculator/com.android.calculator2.Calculator"
    # CALCULATOR = "com.android.calculator2/com.android.calculator2.view.BaseActivity"

    SYSTEM_CLOCK = "com.android.deskclock/.DeskClock"
    # SYSTEM_CLOCK = "com.qiku.android.xtime/qiku.xtime.ui.main.XTimeActivity"

    # FILE_MANAGER = "com.mediatek.filemanager/.FileManagerOperationActivity"
    FILE_MANAGER = "com.sprd.fileexplorer/com.sprd.fileexplorer.activities.FileExploreActivity"
    # FILE_MANAGER = "com.qiku.android.filebrowser/com.qiku.android.filebrowser.activity.LeadingActivity"

    # BROWSER = "com.android.browser/.BrowserActivity"
    # BROWSER = "com.qihoo.browser/com.qihoo.browser.BrowserActivity"
    CHROME = "com.android.chrome/com.google.android.apps.chrome.Main"

    DIALER = "com.android.dialer/.DialtactsActivity"
    # DIALER = "com.qiku.android.contacts/com.qiku.android.contacts.dial.DialActivity"

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

