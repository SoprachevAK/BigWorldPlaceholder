class BigWorld():
  entities = {}

  class Player:
    def __init__(self):
      self.arenaTypeID = None
      self.connectionMgr = None
      self.team = None
      self.gunRotator = None
      self.autoAimVehicle = None
      self._PlayerAvatar__aimingInfo = None
      self.vehicle = None
      self.vehicleTypeDescriptor = None  # type: BigWorld.Player.VehicleTypeDescriptor
      self.playerVehicleID = None  # type: int
      self.name = None  # type: str

    arena = None  # type: BigWorld.Player.Arena
    arenaUniqueID = None

    class Arena:
      def __init__(self):
        self.periodLength = None
        self.periodEndTime = None
        self.period = None
        self.bonusType = None
        self.vehicles = {}

      arenaType = None  # type: BigWorld.Player.Arena.ArenaType

      class ArenaType:
        geometry = None  # type: str

    class VehicleTypeDescriptor:
      def __init__(self):
        self.shot = None
        self.turret = None
        self.hull = None
        self.gun = None  # type: BigWorld.Player.VehicleTypeDescriptor.Gun
        self.level = None
        self.type = None  # type: BigWorld.Player.VehicleTypeDescriptor.Type

      class Type:
        def __init__(self):
          self.tags = None

      class Gun:
        def __init__(self):
          self.shots = None
          self.shotDispersionAngle = None
          self.name = None

    def getOwnVehiclePosition(self):
      return None

    def enableServerAim(self, enable):
      pass

    def getOwnVehicleSpeeds(self):
      pass

  class Entity:
    typeDescriptor = None  # type:BigWorld.Entity.TypeDescriptor

    class TypeDescriptor:
      name = None  # type: str


entities = None


def player():
  # type: () -> BigWorld.Player
  return None


def serverTime():
  return None


def LatencyInfo():
  return None


def callback(time, callback):
  return None


def component():
  return None


def getFPS():
  return [0, 1]


def wg_openWebBrowser(url):
  pass
