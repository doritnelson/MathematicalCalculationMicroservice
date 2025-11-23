import os
import time
import random
import json
from calculation import calculate


#Watches for changes on file and processes requests
class FileWatcher:
    def __init__(self,filename):
    #initializes watcher class for a specific file
        self.filename = filename
        self.last_modified_time = self.get_file_modification_time()
        self.results = []
        self.requests = []

    def get_file_modification_time(self):
    #retrieves last time the file has been modified
        return os.stat(self.filename).st_mtime

    def load_requests(self):
    #loads request from the file designated
        with open(self.filename, "r") as file:
            self.requests = json.load(file)

    def write_results(self):
    #writes requests into the file designated
        json_str = json.dumps(self.results, indent=4)
        with open(self.filename, "w") as f:
            f.write(json_str)
        self.results = []

    def process_requests(self):
        #Goes through the requests and processes each
        for request in self.requests["request"]:
            error = "None"
            try:
                result = calculate(request)
                #if a request fails then the action was not on list of option
                if not (result):
                    error = "Action not in list of available functions"
            except:
                #if a request fails then the input was not correctly formatted
                error = "Incomplete action - error thrown"
            self.results.append({"completed": not (result == False), "result": result, "error": error})

    def watch(self):
        #checks if file has been modified then attempts to process requests
        current_modified_time = self.get_file_modification_time()
        if current_modified_time != self.last_modified_time:
            self.last_modified_time = current_modified_time
            try:
                self.load_requests()
                self.process_requests()
                self.write_results()
            except:
                #if it fails then it likely saw its own file modification
                print("Request complete")

if __name__ == "__main__":
    watcher = FileWatcher("calculation.txt")
    while(True):
        time.sleep(1)
        watcher.watch()

