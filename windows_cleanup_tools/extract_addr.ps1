Get-Content output.txt | Select-String -Pattern Address -Context 1,1 >> addr.txt
(gc addr.txt) | ? {$_.trim() -ne "" } | set-content addr.txt