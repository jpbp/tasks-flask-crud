from flask import Flask,request
from models.taks import Taks
app = Flask(__name__)

#CRUD
#Create, Read, Update and Delete
#Tabela: Tarefas


tasks = []

@app.route('/tasks',methods=['POST'])
def create_task():
    ids = 0
    data = request.get_json()
    print(data)
    for title,description in data.items():    
        task = Taks(ids,title,description)
        ids+=1
        tasks.append(task.to_dict())
    print(tasks)
    return tasks

if __name__ == "__main__":
    app.run(debug=True)
    
#Aula 69