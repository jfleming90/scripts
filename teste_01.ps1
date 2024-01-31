function Show-Menu
{
     param (
           [string]$Title = ‘Kesseret v.8008135’
     )
     cls
     Write-Host “================ $Title ================”
    
     Write-Host “1: Press ‘1’ for Institutionalize Freedom.”
     Write-Host “2: Press ‘2’ for Promote Capitalism.”
     Write-Host “3: Press ‘3’ for DEMOCRACY.. FUCK YEA.”
     Write-Host “Q: Press ‘Q’ to quit.”
}
do
{
     Show-Menu
     $input = Read-Host “Please make a selection”
     switch ($input)
     {
           ‘1’ {
                cls
                ‘HEY FUCKERS GET IN THE GULAG’
           } ‘2’ {
                cls
                ‘PROMOTE THE CHOW LINE IN THE GULAG’
           } ‘3’ {
                cls
                ‘OFF TO THE GULAG WITH YOU!’
           } ‘q’ {
                'You don't quit the Gulag.. the Gulag quits you'
           }
     }
     pause
}
until ($input -eq ‘q’)
