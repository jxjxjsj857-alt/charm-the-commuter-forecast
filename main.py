"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist to /output/entry.txt.

The forecast keeps the register of a real broadcast forecast -- city named,
weather the whole point, one concrete detail -- and bends it just enough to
make a bored commuter smile: in Drowsywick the rain is real, the bus is
late, and the only sensible advice is to lower your expectations.
"""

import os

FORECAST = (
    "In Drowsywick, expect light rain and 12°C, with a 90% chance your bus "
    "is late — pack an umbrella and lower your expectations accordingly."
)
# 137 characters of the 140 allowed: every word earns its place, and the
# forecast stays a forecast -- city, weather, one concrete commuter detail.


def main() -> None:
    assert 1 <= len(FORECAST) <= 140, f"forecast is {len(FORECAST)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
