from werobot.robot import werobot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()

robot = werobot.WeRoBot(token="kidult00", enable_session=True,
                        session_storage=session_storage)

@robot.text
def hello_world():
    return '豆瓣查书功能开发ing'

# robot.run()