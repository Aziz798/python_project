from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send
from flask_app import app,socketio
from flask_app.models.message import Message
rooms = {}

@app.route("/message/<int:sender_id>/<int:house_id>/<int:receiver_id>")
def message(sender_id,house_id,receiver_id):
    data={
        'sender_id':sender_id,
        'house_id':house_id,
        'receiver_id':receiver_id
    }
    messages=Message.show_one_conversation(data)
    return render_template('chat_room.html',messages=messages)



# @app.route("/", methods=["POST", "GET"])
# def home():
#     session.clear()
#     if request.method == "POST":
#         name = request.form.get("name")
#         code = request.form.get("code")
#         join = request.form.get("join", False)
#         create = request.form.get("create", False)

#         if not name:
#             return render_template("home.html", error="Please enter a name.", code=code, name=name)

#         if join != False and not code:
#             return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        
#         room = code
#         if create != False:
#             room = generate_unique_code(4)
#             rooms[room] = {"members": 0, "messages": [{ "name": "aziz","message": "Hi"},{ "name": "mouj;","message": "Hello"},{ "name": "aziz","message": "How can I help you?"},{ "name": "mouj;","message": "I want to rent the house."}]}
#         elif code not in rooms:
#             return render_template("home.html", error="Room does not exist.", code=code, name=name)
        
#         session["room"] = room
#         session["name"] = name
#         return redirect(url_for("room"))

#     return render_template("home.html")

# @app.route("/room")
# def room():
#     room = session.get("room")
#     if room is None or session.get("name") is None or room not in rooms:
#         return redirect(url_for("home"))

#     return render_template("room.html", code=room, messages=rooms[room]["messages"])

# @socketio.on("message")
# def message(data):
#     print("🔥🔥🔥🔥", session, "🔥🔥🔥🔥")
#     room = session.get("room")
#     print(data, "🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈")

#     if room not in rooms:
#         return 
    
#     content = {
#         "name": session.get("name"),
#         "message": data["data"]
#     }
#     send(content, to=room)
#     rooms[room]["messages"].append(content)
#     print(rooms[room]["messages"], "🎈🔥🎈🔥🎈🔥🎈")
#     print(f"{session.get('name')} said: {data['data']}")

# @socketio.on("connect")
# def connect(auth):
#     room = session.get("room")
#     name = session.get("name")
#     if not room or not name:
#         return
#     if room not in rooms:
#         leave_room(room)
#         return
    
#     join_room(room)
#     send({"name": name, "message": "has entered the room"}, to=room)
#     rooms[room]["members"] += 1
#     print(f"{name} joined room {room}")

# @socketio.on("disconnect")
# def disconnect():
#     room = session.get("room")
#     name = session.get("name")
#     leave_room(room)

#     if room in rooms:
#         rooms[room]["members"] -= 1
#         if rooms[room]["members"] <= 0:
#             del rooms[room]
    
#     send({"name": name, "message": "has left the room"}, to=room)
#     print(f"{name} has left the room {room}")