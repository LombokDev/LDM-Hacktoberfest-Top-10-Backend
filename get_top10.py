from apscheduler.schedulers.blocking import BlockingScheduler

import get_and_post

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', seconds=30)
def run_job():
    get_and_post.run()


scheduler.start()
