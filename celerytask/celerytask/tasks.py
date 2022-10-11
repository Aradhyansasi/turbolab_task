import random
import string
import random
import csv
from celerytask.celery import app
from time import sleep
from celery import Task

@app.task(bind=True)
def generate_csv(self, name, total):
    self.update_state(state = 'Started')
    # sleep(10)
    with open('./generate_file/data/'+name+'.csv', 'w', newline='') as csvfile:
        self.update_state(state = 'Progress' , meta = {'progress' : 10})
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        self.update_state(state = 'Progress' , meta = {'progress' : 20})
        for i in range(0, int(total)):
            sleep(1)
            spamwriter.writerow([str(''.join(random.choices(string.ascii_lowercase +string.digits, k=7)))])
        self.update_state(state = 'Completed' , meta = {'progress' : 10})


@app.task(bind=True)
def error_handler(request, exc, traceback):
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          request.id, exc, traceback))

@app.task(bind=True)
def status(s):
    print(str(s) , 'status')
