# 1. Create a file and call it lyrics.txt (it does not need to have any content)

lyrics_file = open("lyrics.txt", "w")
lyrics_file.close()

# 2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.

write_to_songs_file = open("songs.docx", "w")
write_to_songs_file.write("\nHey \n")
write_to_songs_file.write("It is working")
write_to_songs_file.write(" - ish..")

write_to_songs_file.close()

# 3. open and read the content and write it to your terminal window. * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

read_songs_file = open("songs.docx", "r")
print(read_songs_file.read())

read_songs_file.close()

read_songs_file = open('songs.docx', 'r')

lines_from_file = read_songs_file.readline()
while lines_from_file:
    print(lines_from_file)
    lines_from_file = read_songs_file.readline()

read_songs_file.close()

# with open("songs.docx") as read_songs_file:
# lines_from_file = read_songs_file.readline()
# print(lines_from_file)
# line = read_songs_file.readline()


read_songs_file = open('songs.docx', 'r').readlines()
for lines_from_file in read_songs_file:
    print(lines_from_file)
