import random
import string
import random
import csv
from celerytask.celery import app


@app.task()
def generate_csv(name, total):
    with open('./generate_file/data/'+name+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, int(total)):
            spamwriter.writerow([str(''.join(random.choices(string.ascii_lowercase +string.digits, k=7)))])

