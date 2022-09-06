$iplist = Get-Content 'C:\Users\800xaInstaller\OneDrive - ABB\Documents\Ping Monitoring\PowerShell\ip_list.txt' #Get the IP Addresses[content of the file] from the Input File and store it in the variable "$iplist"
Clear-Content 'C:\Users\800xaInstaller\OneDrive - ABB\Documents\Ping Monitoring\PowerShell\ipoutput.txt' #Delete the Old Output File

foreach($ip in $iplist){ #For Loop, this will allow us to find the ping status of the IP Addresses independently
    
    $pingtest = Test-Connection -ComputerName $ip -Quiet -Count 1 -ErrorAction SilentlyContinue 
    #Test-Connection: Command/cmdlet will ping the IP Address
    #-ComputerName $ip: States the IP Address to ping which in this case is stored in the variable "$ip"
    #-Quiet: Returns the Boolean value [$True if Ping is Successful and $False if Ping is not Successful]
    #-Count 1: Will ping the IP Address only once
    #-ErrorAction SilentlyContinue: If the ping is not successful, instead of returning errors, it will return that the IP Address is offline as the output
    if($pingtest){ #If Ping Status is Successful
         Add-Content 'C:\Users\800xaInstaller\OneDrive - ABB\Documents\Ping Monitoring\PowerShell\ipoutput.txt' "UP $ip Ping Successful," -NoNewline #Append the Ping Status information to the Output File on the same line [no line breaks], the reason why we Append to the Output File is becasue we are adding Ping Status of each IP Addresses instead of overwriting the Ping Status at each iteration of the For Loop which will delete and replace the Ping Status of the current IP Address in the iteration by the Next IP Address in the interation, and this would result in wrong Output File with missing ping status of the IP Addresses 
         Write-Host("UP $ip Ping Successful") #Outputting the Ping Status on Terminal which in this case is Ping is Successful
     }
     else{
         Add-Content 'C:\Users\800xaInstaller\OneDrive - ABB\Documents\Ping Monitoring\PowerShell\ipoutput.txt' "DOWN $ip Ping Unsuccessful," -NoNewline #Append the Ping Status information to the Output File on the same line [no line breaks], the reason why we Append to the Output File is becasue we are adding Ping Status of each IP Addresses instead of overwriting the Ping Status at each iteration of the For Loop which will delete and replace the Ping Status of the current IP Address in the iteration by the Next IP Address in the iteration, and this would result in wrong Output File with missing ping status of the IP Addresses 
         Write-Host("DOWN $ip Ping Unsuccessful") #Outputting the Ping Status on Terminal which in this case is Ping is Unsuccessful
     }
     
}