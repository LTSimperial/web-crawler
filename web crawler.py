import os


#create folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory "+directory)
        os.makedirs(directory)

#
def create_data_file(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,base_url)


#create a new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

create_data_file('happy','https://www.baidu.com')
