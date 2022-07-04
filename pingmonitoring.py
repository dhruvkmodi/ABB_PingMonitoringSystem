import os #Importing the OS Module for operating system dependent functionality
import platform #Importing the Platform Module for giving information about platform/system where the code is running. Platform module allows to do that by providing us an API.

OStype = "" #This string variable will be applied to store the OS type [Its connected to the "OS_type() function and the "monitoring_ping" function in the code]


# Deleting old content of  the output file before adding new ping status of all IP addresses to the output file
def delete_content_of_ipoutput():
        
        f = open("ipoutput.txt", "w") # open output file with write permissions ["w" mean overwrite the file so the old content of the file will be deleted and replaced by the new content]
        f.write("") #add whitespace to output file/updates output file with no output
        f.close() #close the output file
        
#Get the OS of where the code is running which in this case is Digital Client VM [Windows]     
def OS_type(): 
        current_os = platform.system().lower() #apply the platform module to get the OS, covert it to lower case and store it in the local variable "current_os"
        if current_os == "windows": #if the "current_os" variable is equal to windows
                return "-n" #return "-n"
        else: #else if it is not windows
                return "-c" #return "-c"

#Getting the ping status of all the IP addresses by opening the input file, pinging each of the IP addresses and than printing ping status to the output file
def monitoring_ping(OStype): #OStype parameter function will be explained later in the code

        with open("ip_list.txt") as file: #open the input file
                dump = file.read() #read the input file and store the string in the variable "dump"
                dump = dump.splitlines() #split the string into a list, where each IP address will be on each seperate line, and store in the "dump" variable but this the dump variable is a list instead of a string
                
        for ip in dump: #for loop to go through each IP address in the list, find out the ping status and store the result in the output file 
                response = os.system(f"ping {OStype} 1 {ip}") #store the ping result of the IP address to a "response" variable which is of int type [The "OStype" part in the command allows the ping command to run properly in the windows environment because the Digital Client VM is a windows type, if the OS is different than "OStype" part in the command will change to correctly run the ping command in that different OS environment]
                if response == 0: #if the response type is equal to zero [reponse is equal to zero means that the ping is successful]
                        DHU = os.popen(f"ping {OStype} 1 {ip}").read() #run the ping command again and store the status in string format in a variable called "DHU" [The reason why we are doing this is because when we run the ping command on windows OS and the ping status is "Destination host unreachable" for an IP Address, it will still show the response as zero [ping being successful] which is wrong]
                        if "Destination host unreachable" in DHU: # check if the string/text "Destination host unreachable" is part of the "DHU" variable 
                                f = open("ipoutput.txt", "a") #open the output file and append ["a" means add to the end of file without overwriting the file so the content that is already part of the file will stay and the new cotent will be added to the end of the file]
                                f.write(f"DOWN {ip} Ping Unsuccessful,") # append to the output file that the ping is not successful
                                f.close # close the file
                                print(f"DOWN {ip} Ping Unsuccessful \n") # when the code executes we will also print in the terminal that ping is not successful
                        else: #if the string/text "Destination host unreachable" is not part of the "DHU" variable
                                f = open("ipoutput.txt", "a") #open the output file and append ["a" means add to the end of file without overwriting the file so the content that is already part of the file will stay and the new cotent will be added to the end of the file]
                                f.write(f"UP {ip} Ping Successful,") #append to the output file that the ping is successful 
                                f.close #close the output file 
                                print(f"UP {ip} Ping Successful \n") #when the code executes we will also print in the terminal that ping is successful
                else: # else response variable is not equal to zero which mean ping is not successful
                        f = open("ipoutput.txt", "a") #open the output file with the append parameter 
                        f.write(f"DOWN {ip} Ping Unsuccessful,") #append to the output file that ping is not successful
                        f.close #close the output file
                        print(f"DOWN {ip} Ping Unsuccessful \n") #when the code executes we will also print in the terminal that ping is not successful


''' 
Calling all the functions in there respective orders for the python script to correctly work [The Python Script will extract IP addresses from the input text file and ping to each of the IP addresses in this list. 
The ping status will be outputted to the output text file (This is also the file that Microsoft Power Automate pulls from OneDrive Business. 
'''
def main():
        
        delete_content_of_ipoutput() #call the function for deleting the old ping status result of all the IP Addressses/fully clearing the output file
        OStype = OS_type() # calling the function for getting the OS of the host machine where the code is running which in this case is the Digital Client VM and storing the result in the "OStype" variable                     
        monitoring_ping(OStype) # adding the OStype as a parameter of the funciton and calling the function to find out the ping status for all the IP addresses which are part of the input file and appending the results to the output file



#Calling the main which contains functions calls of the other functions and this allows the code within all functions including main function to be executed during run time [Note: if calling main() function is deleted the code will not execute]
main()

#Reference
##https://www.youtube.com/watch?v=PTUhiDnYrbs
##https://www.youtube.com/watch?v=gv-25sToNKU
##https://www.delftstack.com/howto/python/python-ping/#ping-server-in-python-using-the-ping3-ping-function
##https://www.youtube.com/watch?v=4C0yTluc8pA
##https://www.adamsmith.haus/python/answers/how-to-ping-an-ip-address-in-python
##https://appdividend.com/2021/01/15/python-os-system-method-example/
##https://www.geeksforgeeks.org/python-os-system-method/
##https://www.delftstack.com/howto/python/python-detect-os/#:~:text=Darwin%27%20for%20macOS-,Detect%20the%20Operating%20System%20Using%20the%20sys%20Module%20in%20Python,system%27s%20name%20on%20our%20device.
##https://developer.mozilla.org/en-US/docs/Glossary/CRLF
##https://note.nkmk.me/en/python-string-line-break/
##https://www.delftstack.com/howto/python/python-print-line-break/
##https://flexiple.com/python-new-line
##https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
##https://www.w3schools.com/python/python_file_write.asp
##https://www.w3schools.com/python/gloss_python_escape_characters.asp
##https://www.codegrepper.com/code-examples/python/python+how+to+erase+a+file+before+writing
##https://www.geeksforgeeks.org/how-to-delete-data-from-file-in-python/
##https://www.geeksforgeeks.org/with-statement-in-python/
##https://www.pythonforbeginners.com/files/with-statement-in-python
##https://www.w3schools.com/python/ref_string_splitlines.asp
##https://www.pythontutorial.net/python-basics/python-read-text-file/
##https://www.delftstack.com/howto/python/python-ping/#:~:text=The%20command%20to%20ping%20a,then%20run%20the%20command%20accordingly.
##https://code.visualstudio.com/docs/python/coding-pack-python


