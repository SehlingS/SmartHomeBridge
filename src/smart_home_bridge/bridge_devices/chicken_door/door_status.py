from dataclasses import dataclass

from smart_home_bridge.bridge_devices.chicken_door.chicken_door import door_position


@dataclass(frozen=True)
class door_status:
    position: door_position
    fault: str | None = None
    light_level: int | None = None
    battery_level: int | None = None
    power_source: str | None = None
    wifi_strength: int | None = None
    connected: bool | None = None
    last_open_time: str | None = None
    last_close_time: str | None = None


def wifi_signal_percent(dbm: int | None) -> int | None:
    if dbm is None:
        return None
    if dbm >= -50:
        return 100
    if dbm <= -100:
        return 0
    return round(2 * (dbm + 100))
