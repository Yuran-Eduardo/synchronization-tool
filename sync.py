import os
import shutil
import time
import argparse
import logging
from filecmp import dircmp


def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def sync_folders(source, replica):
    if not os.path.exists(replica):
        os.makedirs(replica)
        logging.info(f"Created replica folder: {replica}")
    
    compare_folders(source, replica)

def compare_folders(source, replica):
    comparison = dircmp(source, replica)
    
    # Copy new and modified files
    for file in comparison.left_only:
        source_path = os.path.join(source, file)
        replica_path = os.path.join(replica, file)
        if os.path.isdir(source_path):
            shutil.copytree(source_path, replica_path)
        else:
            shutil.copy2(source_path, replica_path)
        logging.info(f"Copied: {source_path} -> {replica_path}")
    
    for file in comparison.diff_files:
        source_path = os.path.join(source, file)
        replica_path = os.path.join(replica, file)
        shutil.copy2(source_path, replica_path)
        logging.info(f"Updated: {source_path} -> {replica_path}")
    
    # Remove files/folders that are only in the replica
    for file in comparison.right_only:
        replica_path = os.path.join(replica, file)
        if os.path.isdir(replica_path):
            shutil.rmtree(replica_path)
        else:
            os.remove(replica_path)
        logging.info(f"Removed: {replica_path}")
    
    # Recursively sync subdirectories
    for common_dir in comparison.common_dirs:
        compare_folders(os.path.join(source, common_dir), os.path.join(replica, common_dir))

def main():
    parser = argparse.ArgumentParser(description="Folder Synchronization Tool")
    parser.add_argument("source", help="Path to source folder")
    parser.add_argument("replica", help="Path to replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval (seconds)")
    parser.add_argument("log_file", help="Path to log file")
    args = parser.parse_args()

    setup_logging(args.log_file)
    logging.info("Starting synchronization process...")
    
    while True:
        sync_folders(args.source, args.replica)
        logging.info(f"Synchronization completed. Sleeping for {args.interval} seconds.")
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
