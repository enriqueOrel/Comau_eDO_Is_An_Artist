with open("filepath.txt", "r",encoding = 'utf-8') as file1, open("filepath.txt", "w",encoding = 'utf-8') as file2 :
    # Looping through file1
    for line in file1:
        if line.startswith('P'): # Condition for matching
            file2.writelines(line)

 
name_program = 'prog_1'  # Change program name here <--

with open("filepath.txt", "r", encoding = 'utf-8') as file2, open(f"filepath/{name_program}.txt", "w") as file3:
    x_old = 0  # initialize variables x_old 
    y_old = 0 #Initialize variables y_old
    pixel_size = 1 # Number of pixels as in the robot_paint script
    approach = 100 # Alzata
    tolerance = 3 # Tollerance between points. Higher values of pixel_size higher the tolerance

# Code start here:  
#-------------------------------------------------------------------------------------------------------------
    file3.writelines(f'PROGRAM {name_program} PROG_ARM = 1\n')
    file3.writelines('BEGIN\n')
    file3.writelines('CYCLE\n')
    file3.writelines('  $ORNT_TYPE := RS_WORLD\n') 
    file3.writelines('  $MOVE_TYPE := JOINT\n') 
    file3.writelines('  $JNT_MTURN := TRUE\n')
    file3.writelines('  $CNFG_CARE := TRUE\n') 
    file3.writelines('  $TURN_CARE := TRUE\n')  
    file3.writelines('  $SING_CARE := FALSE\n')
    file3.writelines('  $TERM_TYPE := NOSETTLE\n') 
    file3.writelines('  $FLY_TYPE := FLY_CART\n')
    file3.writelines('  $FLY_TRAJ := FLY_PASS\n')
    file3.writelines('  $FLY_DIST := -1.0\n') 
    file3.writelines('  $STRESS_PER := 65\n') 
    file3.writelines("  $UFRAME := POS(0, 0, 0, 0.0, 0.0, 0.0, '')\n")  
    file3.writelines("  $TOOL := POS(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, '')\n") 
    file3.writelines(f"  MOVE JOINT TO POS(0, 0, {approach}, 0, 180.0, 0)\n")

    for linesb in file2: # Loop through lines

    #---------------------------------------------------------------------------
        Index_Pos = int(linesb.find('('))  # coordinates afther pos(
        Index_X = int(linesb.find(',')) # find the positions of first X
        Index_Y = int(linesb.find(',', Index_X+1)) # find the position of Y
        Index_Z = int(linesb.find(',', Index_Y+1)) # find the position of Z

    #---------------------------------------------------------------------------
        x_y = linesb[Index_Pos:Index_Y+1] # coordinates of X, Y
        x_y_z = linesb[Index_Pos:Index_Z-1 ]   # coordinates of X, Y, Z  

    # ---------------------------------------------------------------------------
        x = float(linesb[Index_Pos+1:Index_X]) # Only Y coordinates
        y  = float(linesb[Index_X+1: Index_Y]) # Only X coordinates
    
    #--------------------------------------------------------------------------------------------------------
        dist = ((x - x_old)**2 + (y - y_old)**2)**(1 / 2.0) # distance of points X, Y

        if dist > pixel_size + tolerance :

            # Simple post-processing from coordinare in X, Y & Z in PDL2 language 

            string1 = f"  MOVE LINEAR TO POS({x_old}, {y_old}, {approach}, 0, 180.0, 0, 'T1:0 T2:0 T3:0')"  
            string3 = f"  MOVE LINEAR TO POS({x}, {y}, {approach}, 0, 180.0, 0, 'T1:0 T2:0 T3:0')"
            file3.writelines('\r\n') # New line 
            file3.writelines(string1) # Write in the file  the approach 
            file3.writelines('\r\n') # New line 
            file3.writelines(string3) # Write in the line the 
        
        string2 = f"  MOVE LINEAR TO POS{x_y_z}, 0, 180.0, 0, 'T1:0 T2:0 T3:0')"

        x_old = x
        y_old = y
        file3.writelines('\r\n')
        file3.writelines(string2)

    file3.writelines('\r\n')
    file3.writelines(f'END {name_program} ')
#------------------------------------------------------------------------------------------------------------
