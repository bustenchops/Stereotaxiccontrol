import RPi.GPIO as GPIO
import time

# Define GPIO pins
limit_switches = [22, 13, 19]

# GPIO setup
GPIO.setmode(GPIO.BCM)
for pin in limit_switches:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Limit switch test started. Press CTRL+C to exit.")

try:
    while True:
        for pin in limit_switches:
            if GPIO.input(pin) == GPIO.LOW:
                print(f"Limit switch on GPIO {pin} is PRESSED.")
            else:
                print(f"Limit switch on GPIO {pin} is RELEASED.")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Test stopped by user.")
finally:
    GPIO.cleanup()