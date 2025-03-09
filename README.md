# 🏆 Folder Synchronization Challenge (Job Application)

## 📌 About this Challenge
This project was developed as part of a **Junior Developer in QA job application challenge**. The objective is to implement a **one-way folder synchronization tool** that keeps a replica folder identical to a source folder, ensuring updates at a specified interval.

The solution was implemented in **Python** without using third-party synchronization libraries, demonstrating my ability to design efficient algorithms for file handling.

## 🚀 Key Features
- **One-way synchronization**: The replica folder is always updated to match the source folder.
- **Automated periodic execution**: Runs at a configurable interval.
- **Detailed logging**: All operations (creation, modification, deletion) are recorded in a log file and printed to the console.
- **Customizable via command-line arguments**: Allows dynamic configuration.
- **Error handling**: Ensures stable execution without unexpected crashes.

## 📂 Technical Approach
- **Python's built-in libraries (`os`, `shutil`, `filecmp`)** were used to manage file operations efficiently.
- **`filecmp.dircmp()`** is used to compare directory structures and detect differences.
- **Recursive traversal** ensures all subdirectories are also synchronized.
- **Logging (`logging` module)** provides detailed tracking of actions performed.
- **A loop with `time.sleep()`** maintains periodic execution.

## ▶️ How to Run the Script
To execute the script, run the following command:

```sh
python sync.py "<source_folder>" "<replica_folder>" <interval_seconds> "<log_file_path>"
```

### **Example Usage**:
```sh
python sync.py "C:\Users\User\Desktop\Source" "C:\Users\User\Desktop\Replica" 30 "C:\Users\User\Desktop\sync.log"
```
This will:
- Synchronize `Source` → `Replica` every **30 seconds**.
- Log all operations to `sync.log`.

## 🔍 Testing Instructions
- **Add a new file** to the source folder → It should be copied to the replica folder.
- **Modify an existing file** in the source folder → The updated version should overwrite the file in the replica.
- **Delete a file** from the source folder → The same file should be removed from the replica.
- **Check the log file (`sync.log`)** to verify the recorded operations.

## 📄 Example Log Output
```log
2025-03-08 22:29:04 - INFO - Copied: C:\Users\User\Desktop\Source\file.txt -> C:\Users\User\Desktop\Replica\file.txt
```

## 👨‍💻 Author
Developed by **Yuran Eduardo**!
