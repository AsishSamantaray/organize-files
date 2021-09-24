# Get all files from the path (Downloads)
# copy the files based on the extention to there respective folder.

from glob import glob 
import os
from shutil import move

# Enter the path of the folder that you want to organize the files.
base_dir = "C:/Users/asish/Downloads"

# Returns all the files present in the base directory/folder.
files = glob(f"{base_dir}/*") 

for file in files:
	# Return filename from path.
	file_name = file.split("\\")[1];

	# Get the file extention
	split_tup = os.path.splitext(file)
	extention = split_tup[1]

	# Documents
	if extention in ['.pptx', '.xlsx', '.docx', '.txt', '.pdf']:
		dst_dir = f"{base_dir}/Documents"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)

	# Softwares
	if extention in ['.msi', '.exe']:
		dst_dir = f"{base_dir}/Programs"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)

	# Compressed files
	if extention in ['.zip', '.tar', '.rar']:
		dst_dir = f"{base_dir}/Compressed"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)

	# Images
	if extention in [".jpg", ".jpeg", ".gif", ".png"]:
		dst_dir = f"{base_dir}/Images"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)

	# Videos
	if extention in ['.mp4']:
		dst_dir = f"{base_dir}/Videos"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)

	# Programming files
	if extention in ['.sql', '.java', '.py', '.js', '.ts', '.cpp', '.go', '.kt', '.dart', '.yml', '.json', 'xml']:
		dst_dir = f"{base_dir}/Coding"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)

	# Torrent files
	if extention in ['.torrent']:
		dst_dir = f"{base_dir}/Torrents"
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)		
		move(f"{base_dir}/{file_name}", dst_dir)