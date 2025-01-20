Step 1. Create a New Project Directory
Open your terminal or command prompt and execute the following commands:


cd Desktop
mkdir lofi_converter
cd lofi_converter

Step 2. Create a Virtual Environment
Next, set up a Python virtual environment within the project folder:


python -m venv venv

3. Activate the Virtual Environment
Activate the virtual environment to isolate your project dependencies:

For Windows:


.\venv\Scripts\activate
For Mac/Linux, use:


source venv/bin/activate

4. Install Dependencies
With the virtual environment activated, install the necessary dependencies by running:


pip install librosa soundfile numpy pedalboard

5. Verify Installed Packages
To confirm that the necessary packages are installed, you can list all installed packages by running:

pip list

6. Open the Project in VS Code
Now that your environment is set up, you can open the project folder in Visual Studio Code:


code .

Now select "lofi_converter" folder from deskstop and paste "Songs.py files "
as same level as venu and run code you will see a input_songs folder with 3 output folder are created

Just add song in input_folder and run songs.py code it will automaticzlly generated 3 version of songs