
from enum import Enum, unique

"""
    Activity枚举类，用来存放需要测试的activity集合
"""
@unique
class Activities(Enum):

    MESSAGE = "com.android.mms/.ui.ConversationList"

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

    QQ = "qq"

    WECHAT = "wechat"

    TENCENT_VIDEO = "com.tencent.news/com.tencent.news.activity.SplashActivity"

    JD_SHOPPING = "jd"

    DOUYIN = "dy"

    TAOBAO = ""

    TENCENT_NEWS = "news"
