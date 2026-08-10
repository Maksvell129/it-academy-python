# Напишите рекурсивную функцию find_file(folder, target_filename), которая ищет полный путь к
# целевому файлу в словаре-дереве и возвращает строку с путем или None.

def find_file(folder : dict, target_filename: str) -> str | None:
    current_path = ""

    for obj in folder:
        if isinstance(folder[obj], dict):
            current_path = find_file(folder[obj], target_filename)

            if current_path:
                return f"{current_path}/{obj}"

        elif obj == target_filename:
            return f'{current_path}/{obj}'

file_system = {
    "project_notes1.txt": "content",
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
