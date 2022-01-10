from abstract_classes import AbstractConfiguration, AbstractMacro
from empty_classes import EmptyConfiguration, EmptyMacro
from adafruit_hid.keycode import Keycode

## CONFIGURATION ##

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
