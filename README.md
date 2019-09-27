INSTRUCTIONS:
1. Run the script on python 2.7+.
2. Ensure to install boto3 which is an Aws SDK for python.
3. Configure AWS to set up credentials for AWS account. 
3. The CSV file converted to Json should be readable.
 
NOTE:
	Add an extra column for the ami ids for each server on the spreadsheet before running the script. Otherwise the code will throw an error.


PREREQUISITES:
	Ubuntu
	For Python3
		1. Install python3-pip
			$ sudo apt-get install python3-pip 
					
	For Python2
		1. Install python-pip
			$ sudo apt-get install python-pip
	
	For Boto3
		
			$ pip install boto3
 	Configuration
 		    $ aws configure
 		    	AWS Access Key ID [*******************]: 
 		    	AWS Secret Access Key [********************]:
 		    	Default region name: 
 		    	Default output format:


Testing:
	For a functional operation:

		Command: 
			./tag_instances.py

		Output:
			
		    	tagging i-06b68afdcbd3e0266

				Applying adc203-elwb.cfs.its.tld on i-06b68afdcbd3e0266
				Applying dev on i-06b68afdcbd3e0266
				Applying adc203 on i-06b68afdcbd3e0266
				Applying a@b.com on i-06b68afdcbd3e0266
				Applying its on i-06b68afdcbd3e0266
				Applying adc203-elwb.cfs.its.tld on i-06b68afdcbd3e0266
				Applying ITS on i-06b68afdcbd3e0266
				Applying web on i-06b68afdcbd3e0266
				Applying EDU on i-06b68afdcbd3e0266
				Applying ami-33fefd53 on i-06b68afdcbd3e0266
				Done

				tagging ......