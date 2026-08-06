users_db = {
    "hacker_pro": {"role": "user", "warnings": 3, "status": "active"},
    "admin_main": {"role": "admin", "warnings": 0, "status": "active"},
    "shadow_bot": {"role": "guest", "warnings": 5, "status": "active"},
}

active_users = set()

for username, users_data in users_db.items():
    if users_data["warnings"] > 3:
        users_data["status"] = "blocked"
    else:
        active_users.add(username)

print(active_users)

