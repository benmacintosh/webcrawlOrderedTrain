
with pix2pix/tensorflow, and spyder


then this is powershell script to run




# given img folder x, files aXXX1, make dataset of img1to2,.. n-1ton
#make sure imgs correct data if from webscreenshots
anaconda activate tensorflow, the npowershell

new-item seq_a -itemtype directory
new-item seq_b -itemtype directory
Copy-item -Force -Recurse -Verbose x -Destination seq_a
Copy-item -Force -Recurse -Verbose x -Destination seq_b

#hand delete first and last
#then rename files so match up


python tools/process.py --input_dir seq_a --b_dir seq_b --operation combine --output_dir seq_c


#add new pair to training folder, updates train and tests on last img, then repeats till finished

new-item seq_c_new -itemtype directory

$sourcefiles = get-childitem "C:\Users\benma\Desktop\scripts\pix2pix-tensorflow\seq_c" -Recurse | where {$_.extension -eq ".PNG"}
foreach ($file in $sourcefiles)
{
	Copy-Item C:\Users\benma\Desktop\scripts\pix2pix-tensorflow\seq_c\$file -Destination seq_c_new

	python pix2pix.py --mode train --output_dir seq_train --max_epochs 12 --input_dir seq_c_new --which_direction AtoB --checkpoint seq_train

	python pix2pix.py --mode test --output_dir seq_out --input_dir x --checkpoint seq_train
}

	#need to take just the corrspeonding/latest img in x
	#and intialise a checkpoint for first?

	#(GCI|?{!$_.PSIsContainer}).Count


python pix2pix.py --mode test --output_dir seq_outtest --input_dir x --checkpoint seq_traintest







#for /R Documents\OtherFiles\BatTest\ %%f in (
# *.aspx, *.xml, *.asax, *.asmx, *.config, *.Master
#) do echo %%~nxf|findstr /x /L /i /g:"myexcludefile.txt" >nul&if errorlevel 1 copy %%f Documents\OtherFiles\DestinationTest\
