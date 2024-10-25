import sys
import os

# 현재 스크립트의 경로를 sys.path에 추가
sys.path.append('/apps/study_gatheringdatas/codes/bs4s/')

from get_classes import getfunctions as gf
from apscheduler.schedulers.background import BackgroundScheduler
from insert_mongo_collectingnews_underkg import main_1


temp = 'temp message'
import time
def main(message):
    #스케쥴러 등록
    scheduler = BackgroundScheduler()
    scheduler.add_job(main_1, trigger='interval', seconds=5, coalesce=True, max_instances=1)
    
    scheduler.start()
    
    #정지예방
    count = 0
    while True:
        # time.sleep(1)
        # print(f'{message} : count - {count}')
        
    
        # print(f'gf.message')
        count = count + 1
        pass
    return True
        


if __name__ == '__main__':
    main('task forever!')
    pass