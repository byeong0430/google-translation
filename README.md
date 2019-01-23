# google-translation
Python script to translate English to a selected language using Google Translation API. The following sections in your `docx` file are translated:
- Header
- Footer
- Paragraph
- Table

#### Tech Stack
`python`

# Basic Set Up
1. Make sure the following python modules are installed:
- `requests`
- `json`
- `docx`
- `google-cloud-translate`

If any of the modules are not installed, use the following command line to install them:
```
pip (or pip3) install <module name>
```
Example
```
pip install requests
or
pip3 install requests
```

2. In order to run `translation.py`, you must first enable the Cloud Translation API and download a private key as JSON for authentication. Click [here](https://cloud.google.com/translate/docs/quickstart-client-libraries#client-libraries-install-python) and `SET UP A PROJECT` Button to see the instruction. Click [here](https://cloud.google.com/translate/pricing) to see the **API pricing**

3. Add the API key in `env/` directory 

4. Set the environment variable called `GOOGLE_APPLICATION_CREDENTIALS`. The instruction on Google Cloud doc doesn't appear to work on Windows. Instead, use the following command line on cmd:
```
setx GOOGLE_APPLICATION_CREDENTIALS "<full path of json key>"
```
Example
```
setx GOOGLE_APPLICATION_CREDENTIALS "C:\Users\username\Downloads\[FILE_NAME].json"
```

5. Make sure you have the following set up correctly:
- `input/` and `output/` folders are in the same directory with `translation.py`
- There is only 1 `docx` (**not** `doc`) file inside `input/` directory (all other files will be ignored)

# Compiling into EXE
1. You must first install `pyinstaller` python module using the following command line:
```
pip (or pip3) install pyinstaller
```
If you cannot use the command line, try this:
```
easy_install pyinstaller
```

2. Navigate to the folder containing `translation.py` and run the following command line:
```
pyinstaller -F translation.py
```

3. You will see new `build/` and `dist/` folders. Go to `dist/`

4. Add `input/` and `output/` folders in the same directory with `translation.exe`

5. Make sure you have 1 `docx` file inside `input/`, and double-click on `translation.exe` to run the script