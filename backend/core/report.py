from backend.database.mongodb_sync import fs

file_path = "path/to/your/file.txt"
with open(file_path, "rb") as file:
    file_id = fs.put(file, filename="file.txt")
