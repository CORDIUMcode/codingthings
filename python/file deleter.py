import os


#define function 
def delete_hidden_files(directory_path): 
    try:
        
        #check to see if path exists 
        if not os.path.exists(directory_path):
            print(f"Error: The specified directory does not exist.")
            return
        
        #and is a directory
        if not os.path.isdir(directory_path):
            print(f"Error: The specified path '{directory_path} is not a directory")
            return
        
        #get list of files in directory
        files_list = os.listdir(directory_path)

        #delete files with hidden file symbols
        for filename in files_list:
            if filename.startswith(".") or filename.startswith("._"):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")


        print("Deletion of file with specified symbols completed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    #specify directory
    directory_path = r"C:\Users\Owner\OneDrive\Desktop\Essentials\art\cordium"

    #call function with hidden filke variable
    delete_hidden_files(directory_path)

