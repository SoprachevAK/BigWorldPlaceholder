from typing import Any, Callable, Tuple # noqa: F401
from Avatar import PlayerAvatar # noqa: F401

class WGUrlResponse:
  responseCode = None  # type: int
  body = None  # type: str

class KeyEvent:
  # ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'character', 'cursorPosition', 'isAltDown', 'isCtrlDown', 'isKeyDown', 'isKeyUp', 'isModifierDown', 'isMouseButton', 'isRepeatedEvent', 'isShiftDown', 'key', 'modifiers', 'repeatCount']

  character = None  # type: str
  cursorPosition = None  # type: Tuple[float, float]
  key = None  # type: int
  modifiers = None  # type: int
  repeatCount = None  # type: int
  
  def isAltDown(self):
    return False
  
  def isCtrlDown(self):
    return False
  
  def isKeyDown(self):
    return False
  
  def isKeyUp(self):
    return False
  
  def isModifierDown(self):
    return False
  
  def isMouseButton(self):
    return False
  
  def isRepeatedEvent(self):
    return False
  
  def isShiftDown(self):
    return False
  


def entity(entityID):
  # type: (int) -> Any
  return None

def player():
  # type: () -> PlayerAvatar
  return None

def callback(time, callback):
  # type: (int, Callable[[], Any]) -> None
  return None

def cancelCallback(id):
  # type: (int) -> None
  return None

def fetchURL(url, callback, headers, method='GET', postData=None):
  # type: (str, Callable[[WGUrlResponse], Any], dict, str, str) -> None
  pass