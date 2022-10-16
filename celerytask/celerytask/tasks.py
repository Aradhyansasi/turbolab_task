import random
import string
import random
import csv
from celerytask.celery import app
from time import sleep

@app.task(bind=True)
def generate_csv(self, name, total):
    sleep(10)
    with open('./generate_file/data/'+name+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, int(total)):
            sleep(1)
            spamwriter.writerow([str(''.join(random.choices(string.ascii_lowercase +string.digits, k=7)))])

