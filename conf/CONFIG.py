import os
import sys

# WOW窗口类名
WOW_CLASS_NAME = 'GxWindowClass'
WOW_EXE_NAME = 'WowClassic.exe'
# 重置窗口参数
WOW_WINDOWS_MOVE_PARAM = (-8, 0, 1024, 768, 0)
# 截屏框参数和保存名称 1366*78屏幕可能部分被遮挡，截屏参数稍微小点
SHOOT_BOX_POS = (0, 0, 1009, 720)
SHOOT_BOX_POS = (0, 31, 1009, 720)
SHOOT_FILE_NAME = 'shoot.png'


# if bool(windll.kernel32.SetConsoleTextAttribute(__out, 0x7)) or not IS_DEV:


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        cwd = sys._MEIPASS
    else:
        cwd = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(cwd)
    return os.path.join(base_path, relative_path)


OFFLINE_SAMPLE_FILE_NAME = resource_path(os.path.join('res', 'offline_box_sample.png'))
ROLE_SAMPLE_FILE_NAME = (resource_path(os.path.join('res', 'role_sample.png')),
                         resource_path(os.path.join('res', 'role_sample_2.png')))
CHANNEL_SAMPLE_FILE_NAME = resource_path(os.path.join('res', 'channel_sample.png'))
# 服务器排队样本图片
SERVICE_WATING_SAMPLE_FILE_NAME = resource_path(os.path.join('res', 'wating_sample.png'))
# 服务器连接样本图片
SERVICE_CONNECT_SAMPLE_FILE_NAME = (resource_path(os.path.join('res', 'connect_service_sample.png')),
                                    resource_path(os.path.join('res', 'connect_service_sample_2.png')))
# 服务器刷新样本图片
SERVICE_REFRESH_SAMPLE_FILE_NAME = (resource_path(os.path.join('res', 'refresh_service_sample.png')),
                                    resource_path(os.path.join('res', 'refresh_service_sample_2.png')))
# 服务器登录样本图片
SERVICE_LOGIN_SAMPLE_FILE_NAME = (resource_path(os.path.join('res', 'login_service_sample.png')),
                                  resource_path(os.path.join('res', 'login_service_sample_2.png')))
# 服务器战斗中
SERVICE_IN_BATTLE_SAMPLE_FILE_NAME = resource_path(os.path.join('res', 'in_battle.png'))

# 账号未认证样本图片
UNAUTH_SAMPLE_FILE_NAME = (resource_path(os.path.join('res', 'unauth_sample.png')),
                           resource_path(os.path.join('res', 'unauth_sample.png')))

WARNING_MP3_FILE = resource_path(os.path.join('res', 'warning.mp3'))
ICON_FILE = resource_path(os.path.join('res', 'ic.ico'))
# TODO: 偏移量需要自动获取窗口标题
OFF_SET_Y = 31
# OFFLINE_BOX_POS = SERVICE_CONNECT_BOX_POS = SERVICE_REFRESH_BOX_POS = SERVICE_LOGIN_BOX_POS = (345, 354, 745, 435)
OFFLINE_BOX_POS = SERVICE_CONNECT_BOX_POS = SERVICE_REFRESH_BOX_POS = SERVICE_LOGIN_BOX_POS = (345, 323, 745, 404)
# ROLE_LOGIN_BOX_POS = (425, 690, 580, 715)
ROLE_LOGIN_BOX_POS = (425, 659, 580, 684)
# SERVICE_WATING_BOX_POS = (345, 306, 745, 484)
SERVICE_WATING_BOX_POS = (345, 275, 745, 453)
# 服务器选择截图区域
# CHANNEL_BOX_POS = (225, 160, 785, 625)
CHANNEL_BOX_POS = (225, 129, 785, 594)
# 战场选择截图区域
# CHANNEL_BOX_POS = (225, 160, 785, 625)
SERVICE_IN_BATTLE_BOX_POS = (873, 133, 900, 160)
# 战网登录WOW位置
BATTLE_LOGIN_POS = (300, 700)
# wow角色进入位置
ROLE_LOGIN_POS = (450, 711)
# 申请战场
BATTLE_APPLY_POS = (196, 528)
# 进入战场
BATTLE_ENTRY_POS = (433, 213)
# 退出战场
BATTLE_EXIT_POS = (509, 556)
# 默认值
SLEEP_MIN_TIME_DEFAULT = 30
SLEEP_MAX_TIME_DEFAULT = 50
SKILLS_DEFAULT = '1|Q'
LOGIN_LOADING_TIME_DEFAULT = 20
CLEAR_SHOOT_FILE_DEFAULT = False
COMPARE_VALUE_DEFAULT = 0.65
CHECK_OFFLINE_INTERVAL_DEFAULT = 30
PARAM_DEFAULT_DICT = {'skills': SKILLS_DEFAULT,
                      'is_random_action': True,
                      'is_warning': False,
                      'is_auto_login': True,
                      'login_loadtime': LOGIN_LOADING_TIME_DEFAULT,
                      'clear_shoot_file': CLEAR_SHOOT_FILE_DEFAULT,
                      'compare_value': COMPARE_VALUE_DEFAULT,
                      'check_offline_interval': CHECK_OFFLINE_INTERVAL_DEFAULT,
                      'sleep_min_time': SLEEP_MIN_TIME_DEFAULT,
                      'sleep_max_time': SLEEP_MAX_TIME_DEFAULT,
                      'hiden_mode': True,
                      'app_id': '',
                      'api_key': '',
                      'scret_key': ''
                      }
