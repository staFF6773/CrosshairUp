@echo off
REM Change to the directory where this script is located
cd /d "%~dp0"

REM ASCII Art
REM                                                                                                  
REM                                                                                                  
REM                                        %@@@@@@@@@@   #@@@@@@#                                   
REM                                  %@@@%%%%%%%%%%%%%%%%#%%%%%%%%%%                                
REM                               %@@%#####*===----==+###*==-==+*###%@@#                            
REM       ====  ===              ####*%%%#+==--------------===-------=++%%@%%%             ===  ===  
REM       ==== ====              #@@@@++=--------------------------------+#%@@#            ========  
REM       =========           %*%%*+=--------------------------------------=*#@%@%         ========  
REM       ========          *#@@++=------------------------------------------+#%@@*          ====    
REM          ===           *@@*+=--------------------------------------------=+*#%@%                  
REM                      *@@**=----------------------------------------=+==----=**#%@@                
REM                      #@@==-------------------------------------------+#+=--=+*#%@@                
REM                     @@*+-----=++=------------------------------------=+*#*==++###%@@%             
REM                     @@+=---=**==--------------------------------------=+###*++###%@@%             
REM                  #@@*+=--=*#++=------------=+==--------=+=-------------=+*#######%@@%            
REM                  #@@+===*#**==-----------=**==---------==+#+=----------==+########%%@@           
REM    === ==        #@@+=++##*+=--=**=----=++#*=------------+#*++---+*+=----+*########%@@     ====== 
REM    ======      %@%##==*##*+===+*##=--==+*##*=------------+###*===+##++=--=+*#######%@@     ====== 
REM      ===       @@@==++##++==**####+===**###*=----===-----+####**=+###*+=-=+*#######%@@      ===== 
REM                @@%==*###+==+######*+==*####*=----=++---==+#####*=+#####+==+*#######%@@            
REM                #@%==###*==**######%#**%%%%%#==---=**==-=+*##%%%###%%%%#*+++*#######%@@            
REM                #@@++##**+*########@@@@@@@@@%++=--=**++==*##%@@@@@@@@@@%#**+*#######%@@            
REM                #@@**##**#######%@@++######+*@%==-=*#**==#%@#=+######+*@%#*+*#######%@@            
REM                %@@%###**##########==++####=+#*++==*###+*#*++===+*##*=+####*########%@@            
REM                  #@@%###########++=====+##==+*##++#######*=======+#*==+*###########%@@            
REM                  #@@%##########*==@@@@@@@@@@@@#########*=*@@@@@@@@@@@%++###########%@@            
REM        ====         @@%########%@@@@%%%%%%%%@%==#####*===*@@%%%%%%%%@@@%###########%@@            
REM      =======        @@%##*==###%@@=-.-%%%%%#--::=+#*======-:.:%%%%%#-+@%###*-=###%@@%    ======   
REM    =========        @@%##*=-=+#%@@==*#%%%%%#--:.::=====-::-=##%%%%%#-+@%#*==-=###%@@%    ======== 
REM    =========        @@%##*=--==*@@::*%####%*.....::-==:::..=#%####%*.=@#==---=###%@@%    ======== 
REM    =========        %#@@#*==++====:..=@@@%:........:::.......-@@@*::====-=+=-=#%@%##     ======== 
REM                      *@@##**==*++=-:::+++=:..................:++*+--===+*+=+**#%@@                 
REM                      *%%%%##+++***++=-::::::...............:::::-==+++**+++*##%%@%                 
REM                        *@@%###****+=--::::::...............:::::-==+++****###%@%                  
REM                        *%%%%####**==:........................:::====++**####%%%#                  
REM              =====       %@@%######*-:::.........:::::.......:--===+#######%@@*     =====         
REM            ========        *@@%######*--::::.....:-==-:....:::=++*#######%@@       ========       
REM            ========          #@%%%@@%####*=-:::::::::::::::-=+#####%@%%%@@         ========       
REM         ===========            #@@##@@#%@@#***+=--------=+***#@@#%@@ @@%           ===========    
REM       =============                #@@@@*++++++++++++++++++++++*@@@@#              =============  
REM       =============              *@@#*++------==++====++=======++*##@%#            =============  
REM          ==========            %@@::=+------======++++===========++=.=@%           ===========    
REM                              #@#:...=+----=======================++=...+@@                         
REM                            *@#::---=******===================+******---:.=@%                       
REM                            *@%--++++=----=++===============+*+-----=+++=:+@%                       
REM                            #@%--=+**-....:**===============+*+.....-**+=-+@@                       
REM                             %###==+=:....:**===============+*+.....:+==*%#%#                       
REM                              @@%====-::::-**===============+**:::::-===#@@#                        
REM                              @@%##======*#%#++============+*%%#*=====+*#@%                         
REM                                %%%*****#@@@@**++========++*#@@@@#****#%#                           
REM                                  +@@@@@@@@@@%#**=======+*#%@@@@@@@@@@%#                            
REM                                     #%@@####@@@@*++==+**@@@@%%%%@%##                               
REM                                    #@@############****######%%%%%@@@                               
REM                                    #@@########################%%%@@@*                              
REM                                  *@@##########################%%%%%%@@@                            
REM                                  *@@##########%%########%%######%%%%@@#                            

REM Run the pyinstaller command with relative paths and specify the output folder
pyinstaller --noconfirm --onefile --windowed --icon "%cd%/icon/icon.ico" ^
           --add-data "%cd%/main.py;." ^
           --add-data "%cd%/monitor_selector.py;." ^
           --add-data "%cd%/crosshair.py;." ^
           --add-data "%cd%/icon;icon/" ^
           --add-data "%cd%/icon/icon.ico;." ^
           --add-data "%cd%/icon/icon.png;." ^
           --distpath "%cd%/dist" ^
           "%cd%/main.py"

echo Build completed. The executable is in the 'dist' folder.
pause