#!/bin/bash
BACKUP_LIST=(~/.mozilla ~/Documents/LinuxAdvancement ~/Documents/LinuxPapers
~/Documents/Misc ~/Documents/English ~/Documents/scripts ~/Documents/ST ~/Documents/Timesheets ~/Documents/PR_Docs)
COLLECT_AT="/tmp/drop"
FILE_NAME="bkp_$(date +'%b%d_%Y').tar.gz"

if [[ ! -d $COLLECT_AT ]];then
  mkdir -p $COLLECT_AT
  echo "Created a dropcopy at $COLLECT_AT"
fi

total=${#BACKUP_LIST[@]} # array length
failed=0 # No. of failed operations

for file in "${BACKUP_LIST[@]}";do
 if [[ -d $file ]]; then
  rsync -zrqh $file $COLLECT_AT
  echo "Copied."
 else
  echo "Could not copy $file."
  failed=$(( $failed + 1 ))
 fi
done

echo "Creating an archive at $COLLECT_AT."
tar -czf /tmp/$FILE_NAME $COLLECT_AT/

if [[ -f "$COLLECT_AT/$FILE_NAME" ]];then
 echo "Done."
fi 

echo "Failed to copy $failed out of $total."
