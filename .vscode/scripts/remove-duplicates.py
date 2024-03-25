import os

def scan_and_list_duplicates(directory):
	duplicates = {}

	try:
		for root, dirs, files in os.walk(directory):
			for file in files:
				if file.endswith(".svg"):
					file_path = os.path.join(root, file)
					with open(file_path, 'rb') as f:
						file_content = f.read()

						if file_content is None:
							raise ValueError("file_content is null")

						for other_file_path in duplicates.get(file_content, []):
							if other_file_path is None:
								raise ValueError("other_file_path is null")

							print(f"Duplicate found: {file_path} and {other_file_path}")
							# Uncomment the line below to remove duplicates
							# os.remove(other_file_path)

						if file_content not in duplicates:
							duplicates[file_content] = []

						duplicates[file_content].append(file_path)
	except Exception as e:
		import traceback
		traceback.print_exc()

	return duplicates


directory_to_scan = os.path.join(os.getcwd(), "src\\svg\\Button Art")
scan_and_list_duplicates(directory_to_scan)