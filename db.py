from flask import Flask, request
from module import NASASQL
import newcraw

app = Flask(__name__)


@app.route('/')
def parase_request():
    page = request.args.get('timestamp')
    craw = newcraw.newcraw()


    if str(len(str(page))) != 0:
        sateSQL = []
        
        SQL1 = NASASQL.NASASQL(1234)
        SQL1.connect_SQL()
        SQL1.insert_SQL("1601711620","hi","12.081128","12.081128","12.081128")
        SQL1.insert_SQL("1601711621","hi","12.081128","12.081128","12.081128")
        SQL1.insert_SQL("1601711623","hi","12.081128","12.081128","12.081128")
        SQL1.insert_SQL("1601711624","hi","12.081128","12.081128","12.081128")
        sateSQL.append(SQL1)
       
        for i in sateSQL:
            result = i.select_SQL("1601711623")
            print(result)
            return result

if __name__ == '__main__':
    app.run(debug=True, host="10.121.190.24", port=81)
