import os, shutil, hashlib
import datetime
import time


class Backup:
    total_file_counter=0

    def __init__(self, storage_dir, backup_dir):
        self.storage_dir=storage_dir
        self.backup_dir=backup_dir
        self.backup_d()


    def list_dir(self, dir_path):
        file_list=[]
        for file in os.listdir(dir_path):
            file_list.append(file)
        return file_list


    def get_md5_from_file(self, file):
        md5_sum='000000000000'
        try:
            md5_sum=hashlib.md5(open(file, 'rb').read()).hexdigest()
            return md5_sum
        except FileNotFoundError:
            return md5_sum

    def find_last_backup(self):
        return self.list_dir(self.backup_dir)[-1]

    def diff_time(self, prev_time):
        day=int(prev_time[0:2])
        month=int(prev_time[2:4])
        year=int(prev_time[4:8])
        hour=int(prev_time[9:11])
        minutes=int(prev_time[11:13])

        now_time = round(time.time())

        last_backup = datetime.datetime(year, month, day, hour, minutes)
        last_backup = round(time.mktime(last_backup.timetuple()))
        diff=now_time-last_backup

        if diff > 60:
            return True

    def backup_f(self):
        backup_path=self.backup_dir+self.find_last_backup()+'/'
        count=0
        for i in self.list_dir(self.storage_dir):
            path=backup_path+i
            if self.get_md5_from_file(self.storage_dir+i) != self.get_md5_from_file(path):
                count+=1
                print(i+ ' backuped')
                shutil.copyfile(self.storage_dir+i, path)
        self.total_file_counter+=count


    def backup_d(self):
        now_time = time.strftime("%d%m%Y_%H%M")
        if self.diff_time(self.find_last_backup()):
            count=0
            for i in self.list_dir(self.storage_dir):
                if self.get_md5_from_file(self.storage_dir+i) != self.get_md5_from_file(self.backup_dir+self.find_last_backup()+ '/'+i):
                    count+=1
                    print(i+ ' backuped')

            if count > 0:
                self.total_file_counter+=count
                print('folder backup')
                shutil.copytree(self.storage_dir, self.backup_dir+now_time)


b=Backup('./mob/', './mob2/')

while True:
    b.backup_d()
    b.backup_f()

    print(b.total_file_counter)
    time.sleep(10)



