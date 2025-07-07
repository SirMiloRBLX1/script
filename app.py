from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store verified users in memory {discord_id: True}
verified_users = {}

@app.route("/<user_id>")
def dashboard(user_id):
    if verified_users.get(user_id):
        return render_template("dashboard.html", user_id=user_id)
    else:
        return redirect(url_for("verify", user_id=user_id))

@app.route("/verify/<user_id>", methods=["GET", "POST"])
def verify(user_id):
    if request.method == "POST":
        verified_users[user_id] = True
        return redirect(url_for("dashboard", user_id=user_id))
    return render_template("verify.html", user_id=user_id)

@app.route("/api/check_verified/<user_id>")
def check_verified(user_id):
    # API for bot to check verification status
    return {"verified": verified_users.get(user_id, False)}

if __name__ == "__main__":
    app.run(debug=True)
