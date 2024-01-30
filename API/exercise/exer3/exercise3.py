import pandas as pd
import uuid
from flask import Flask, abort
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='TODO FLASK APP',
          description='Python API Exercise',
          )
ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.String(readonly=True, description='UUID generated identifier'),
    'task': fields.String(required=True, description='Task details')
})

file = './todo.csv'
try:
    df_data = pd.read_csv(file, index_col=0)
except FileNotFoundError:
    df_data = pd.DataFrame()
    df_data.to_csv(file)


class TodoDAO:
    def __init__(self):
        self.counter = 0
        self.todos = pd.read_csv(file, index_col=0)

    def get(self, id):
        todo = self.todos.loc[self.todos['id'] == id]
        print(todo)
        return todo if not todo.empty else abort(404, description="Todo {} doesn't exist".format(id))

    def create(self, data):
        id = str(uuid.uuid4())
        task = data["task"]
        todo = {"id": [id], "task": [task]}

        old_todo = pd.read_csv(file, index_col=0)
        new_todo = pd.DataFrame(todo)

        df = pd.concat([old_todo, new_todo], ignore_index=True)
        # add index=False for
        df.to_csv(file)
        self.todos = df

        return new_todo.to_dict("records")

    def update(self, id, data):
        self.todos.loc[self.todos['id'] == id, 'task'] = data['task']
        # add write to csv
        todo = self.get(id)
        self.todos.to_csv(file)
        return todo.to_dict('records')

    def delete(self, id):
        todo = self.get(id)
        deleted = todo.to_dict('records')
        self.todos.drop(todo.index, inplace=True)
        self.todos.to_csv(file)
        print(deleted)
        return deleted

    def get_first_five(self):
        todos = self.todos.head(5)
        return todos.to_dict('records') if not todos.empty else abort(404, description="No todos yet")

    def get_last_five(self):
        todos = self.todos.tail(5)
        return todos.to_dict('records') if not todos.empty else abort(404, description="No todos yet")


DAO = TodoDAO()
print("wow")
# DAO.create({'task': "hello world"})


@ns.route('/')
class TodoList(Resource):
    '''List all todos and create todo'''

    @ns.response(200, "Sucessfully found todos")
    def get(self):
        '''List all tasks'''
        todos = []
        for name, row in DAO.todos.iterrows():
            todos.append({'id': row['id'], 'task': row['task']})
        return todos, 200

    @ns.response(201, "Sucessfully created todos")
    @ns.expect(todo)
    def post(self):
        '''Create a new task'''
        print(DAO.create(api.payload))
        return 201


@ns.route('/<string:id>')
@ns.response(404, 'Todo not found')
@ns.doc(params={"id": "TODO ID<UUID>"})
class Todo(Resource):
    '''Get, update, delete todo with id'''
    @ns.doc('get_todo')
    @ns.expect(todo)
    @ns.response(200, "Sucessfully found todos")
    def get(self, id):
        '''Get Todo'''
        return DAO.get(id).to_dict("records"), 200

    @ns.doc('delete_todo')
    @ns.response(200, 'Todo deleted')
    def delete(self, id):
        '''Delete Todo'''

        return {"message": "Item Deleted",
                "Item": DAO.delete(id)[0]}, 200

    @ns.expect(todo)
    @ns.response(200, "Sucessfully updated todos")
    def put(self, id):
        '''Update todo'''
        return DAO.update(id, api.payload), 200


@ns.route('/first')
@ns.response(404, 'Todo not found')
class ListFive(Resource):
    '''Show list of ends'''

    def get(self):
        '''gets first 5 todos'''
        todos = DAO.get_first_five()
        return todos, 200


@ns.route('/last')
@ns.response(404, 'Todo not found')
class ListFive(Resource):
    '''gets last 5 todos'''

    def get(self):
        '''Fetch a given resource'''
        todos = DAO.get_last_five()
        return todos, 200


@app.errorhandler(FileNotFoundError)
def internal_error(error):
    return {"Message": "CSV file was not instantiated. Please restart the app", "error": str(error)}


@app.errorhandler(500)
def internal_error(error):
    return {"message": "Ohno"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
