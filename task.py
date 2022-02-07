#usr/bin/pyhthon3

class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = False

    def end(self):
        if self.status == False:
            self.status = True

        return
        
