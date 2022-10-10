from mimetypes import init
import random
import string
import random
import csv
from celerytask.celery import app
# from celery import Celery

# app = Celery('celerytask', broker='amqp://myuser:mypassword@localhost:5672/myvhost')

# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

@app.task()
def generate_csv(name, total):
    print('Im being called')
    with open('./generate_file/data/'+name+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, int(total)):
            spamwriter.writerow([str(''.join(random.choices(string.ascii_lowercase +string.digits, k=7)))])

