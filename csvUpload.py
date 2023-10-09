import csv

csv_file_name = None

def add_to_csv(file,marked,total):
    lst = [file]
    for i in marked:
        lst.append(f"opt : {marked[i]}")
    lst.append(total)
    with open(f'E:/Projects/OMR Scanner/{csv_file_name}.csv','a',newline='') as f:
        obj = csv.writer(f)
        obj.writerows([lst])
        f.close()

def create_csv():
    lst = ['NAME']
    for i in range(1,101):
        lst.append(f"Ques {i}")
    lst.append('TOTAL')
    with open(f'E:/Projects/OMR Scanner/{csv_file_name}.csv','w',newline='') as f:
        obj = csv.writer(f)
        obj.writerows([lst])

def get_total(marked,master_key_bubbles):
    total = 0
    for i in master_key_bubbles:
        if master_key_bubbles[i] == marked[i]:
            total += 1
    return total

def set_csv_file_name(test_name,subject_name,class_name):
    global csv_file_name
    csv_file_name = test_name.get() + subject_name.get() + class_name.get()