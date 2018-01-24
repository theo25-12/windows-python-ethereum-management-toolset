The mass account generator does not automatically write out to a file.
This is because if a difficult vanity address is being searched for then you may want to kill the script after a certain amount of time.

The windows tools:
start.bat :  starts the vanity account generator and logs the outputs in output.txt.
extract_addr.ps1 : copies output.txt to addr.txt and removes any blank lines and all lines containing private keys.


get_balance_multi.py is restricted to 20 accounts at a time due to etherscan api limitations.
the NumOfLines variable is used to set the number of addresses to read * 20.

example:
	if NumOfLines is set to 10. It will read 200(10*20) addresses 20 at a time.