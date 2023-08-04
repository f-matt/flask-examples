from flask import jsonify, request
from sqlalchemy import text
from main import app, db

@app.route("/foos")
def get_foos():
    with db.get_engine(bind_key="second").connect() as conn:
        rset = list()
        result = conn.execute(text("SELECT id, description FROM foos"))
        for row in result:
            rset.append({"id":row[0], "description":row[1]})

        return jsonify(rset)
