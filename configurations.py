import usb_hid
import time
import random

from abstract_classes import AbstractConfiguration, AbstractMacro
from empty_classes import EmptyConfiguration, EmptyMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

## CONFIGURATIONS ##

class Terminal(AbstractConfiguration):
	def getName():
		return 'Terminal'
	def getColor():
		return (0, 255, 0)
	def getMacros():
		return [
			Ls, 
			Pwd,
			Home
		]

class Zoom(AbstractConfiguration):
	def getName():
		return 'Zoom'
	def getColor():
		return (80, 140, 246)
	def getMacros():
		return [
			ToggleMicrophoneZoom,
			EmptyMacro,
			ToggleVideoZoom,
			EmptyMacro,
			ToggleScreenShareZoom,
			EmptyMacro,
			EmptyMacro,
			EmptyMacro,
			LeaveMeetingZoom
		]

class OBS(AbstractConfiguration):
	def getName():
		return 'OBS'
	def getColor():
		return (0, 0, 255)
	def getMacros():
		return [
			SelectScene1, 
			SelectScene2,
			SelectScene3,
			MuteOn,
			MuteOff
		]

class Obsidian(AbstractConfiguration):
	def getName():
		return 'Obsidian'
	def getColor():
		return (51, 51, 255)
	def getMacros():
		return [
			AddNewLog
		]

class Git(AbstractConfiguration):
	def getName():
		return 'GIT'
	def getColor():
		return (247, 78, 39)
	def getMacros():
		return [
			MergeDevelop,
			MergeMaster,
			GitPush
		]

class VSCode(AbstractConfiguration):
	def getName():
		return 'VSCode'
	def getColor():
		return (232, 49, 123)
	def getMacros():
		return [
			RunBuild,
			Refactor,
			Rename,
			OpenInTerminal
		]



## COMMANDS ##

class ToggleMicrophoneZoom(AbstractMacro):
	def getMacroName():
		return "Toggle microphone"
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)

class ToggleVideoZoom(AbstractMacro):
	def getMacroName():
		return "Toggle video"
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)

class ToggleScreenShareZoom(AbstractMacro):
	def getMacroName():
		return "Toggle screen share"
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.S)

class LeaveMeetingZoom(AbstractMacro):
	def getMacroName():
		return "Close call"
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.W)

class OpenInTerminal(AbstractMacro):
	def getMacroName():
		return 'Open in terminal'
	def getMacro():
		keyboard.send(Keycode.ALT, Keycode.T)

class Rename(AbstractMacro):
	def getMacroName():
		return 'Rename'
	def getMacro():
		keyboard.send(Keycode.SHIFT, Keycode.F6)

class Refactor(AbstractMacro):
	def getMacroName():
		return 'Refactor'
	def getMacro():
		keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.R)

class RunBuild(AbstractMacro):
	def getMacroName():
		return 'Run Build'
	def getMacro():
		keyboard.send(Keycode.SHIFT, Keycode.F5)

class Ls(AbstractMacro):
	def getMacroName():
		return 'ls -al'
	def getMacro():
		layout.write("ls ")
		keyboard.send(Keycode.KEYPAD_MINUS)
		layout.write("al")
		keyboard.send(Keycode.ENTER)

class Pwd(AbstractMacro):
	def getMacroName():
		return 'pwd'
	def getMacro():
		layout.write("pwd")
		keyboard.send(Keycode.ENTER)

class Home(AbstractMacro):
	def getMacroName():
		return 'Home'
	def getMacro():
		layout.write("cd ")
		keyboard.send(Keycode.ENTER)

class ToggleMicrophone(AbstractMacro):
	def getMacroName():
		return 'Toggle Microphone'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.D)

class ToggleWebcam(AbstractMacro):
	def getMacroName():
		return 'Toggle Webcam'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.E)

class SelectScene1(AbstractMacro):
	def getMacroName():
		return 'Scene 1'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.ONE)

class SelectScene2(AbstractMacro):
	def getMacroName():
		return 'Scene 2'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.TWO)

class SelectScene3(AbstractMacro):
	def getMacroName():
		return 'Scene 3'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.THREE)

class MuteOn(AbstractMacro):
	def getMacroName():
		return 'Mute'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.FOUR)

class MuteOff(AbstractMacro):
	def getMacroName():
		return 'Unmute'
	def getMacro():
		keyboard.send(Keycode.LEFT_ALT, Keycode.FIVE)

class AddNewLog(AbstractMacro):
	def getMacroName():
		return 'New Log'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.P)
		layout.write("Insert template")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)
		layout.write("New log")
		time.sleep(0.1)
		keyboard.send(Keycode.ENTER)

class MergeDevelop(AbstractMacro):
	def getMacroName():
		return "Merge develop into master"
	def getMacro():
		layout.write("git checkout master")
		keyboard.send(Keycode.ENTER)
		time.sleep(0.5)
		layout.write("git merge develop")
		keyboard.send(Keycode.ENTER)

class MergeMaster(AbstractMacro):
	def getMacroName():
		return "Merge master into develop"
	def getMacro():
		layout.write("git checkout develop")
		keyboard.send(Keycode.ENTER)
		time.sleep(0.5)
		layout.write("git merge master")
		keyboard.send(Keycode.ENTER)

class GitPush(AbstractMacro):
	def getMacroName():
		return "Push"
	def getMacro():
		layout.write("git push")
		keyboard.send(Keycode.ENTER)
		

# Map your configurations inside this array
configurations_map = [Zoom, Terminal, Obsidian, VSCode, Git]	
