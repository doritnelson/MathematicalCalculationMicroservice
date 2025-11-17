import os
import time
import random
import json

service_list = ["total","average","difference"]


class FileWatcher:
    def __init__(self,filename):
        self.filename = filename
        self.last_modified_time = self.get_file_modification_time()

    def get_file_modification_time(self):
        return os.stat(self.filename).st_mtime

    def watch(self):
        while(True):
            time.sleep(1)
            current_modified_time = self.get_file_modification_time()
            if current_modified_time != self.last_modified_time:
                self.last_modified_time = current_modified_time
                print("file modified")
                with open(self.filename,"r") as file:
                    request = json.load(file)
                    try:
                        results = []
                        calculation_requests = request["request"]
                        for calc in calculation_requests:
                            completed = False
                            error = "None"
                            result = 0
                            try:
                                if calc["action"] == "total":
                                    for num in calc["int_array"]:
                                        result += num
                                    completed = True
                                elif calc["action"] =="average":
                                    for num in calc["int_array"]:
                                        result += num
                                    result = result/len(calc["int_array"])
                                    completed = True
                                elif calc["action"] == "difference":
                                    result = abs(calc["int_array"][1] - calc["int_array"][0])
                                    completed = True
                                if completed == False:
                                    error = "Action not in list of available functions"
                            except:
                                error = "Incomplete action - error thrown"
                            results.append({"completed": completed, "result": result,"error":error})
                        json_str = json.dumps(results, indent=4)
                        with open(self.filename, "w") as f:
                            f.write(json_str)
                    except:
                        print("Request complete")

if __name__ == "__main__":
    watcher = FileWatcher("calculation.txt")
    watcher.watch()

