#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_file_per_line(path):
	with open(path) as file:
		lines = file.readlines()
		#print(lines)
		songs_list = [] # List to store the cleaned song names
		for each_song in lines:
			clear_line = each_song.strip() # # Remove newline characters and extra spaces \n
			if clear_line != "":
				songs_list.append(clear_line)
		#print(songs_list)
		return songs_list # Return the list of song names

#open_file_per_line("Songs name.txt")

def write_song_names_alphabetically(file_path):
    songs = open_file_per_line("Songs name.txt")  # Get the list of song names from the input file
    ordered_songs = sorted(songs) # Sort the list of songs alphabetically
    with open(file_path, 'w', encoding='utf-8') as file: # Open the output file in write mode
        for each_song in ordered_songs:  # Write each song on a new line in the output file
            file.write(each_song + "\n") 

write_song_names_alphabetically("Song Names alphabetically")