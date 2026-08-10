def find_file(folder, target_filename):
    current_path = ""

    for obj in folder.keys():
        if isinstance(folder[obj], dict):

            current_path = find_file(folder[obj], target_filename)

            if current_path:
                return f"/{obj}{current_path}"

        elif obj == target_filename:
            return f"{current_path}/{obj}"



file_system = {
    "documents": {
        "work": {
            "project_notes.txt": "content",
            "budget.xlsx": "content"
        },
        "personal": {
            "passport.pdf": "content"
        }
    },
    "photos": {
        "vacation.jpg": "content"
    }
}


print(find_file(file_system, "passport.pdf"))