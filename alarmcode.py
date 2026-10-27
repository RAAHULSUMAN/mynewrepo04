from datetime import datetime
import time
import winsound  # Used for Windows beep. For macOS/Linux, see the note below.


def set_alarm(alarm_time_str):
  print(f"Alarm set for {alarm_time_str}. Waiting...")

  while True:
    # Get the current time in HH:MM:SS format
    current_time = datetime.now().strftime("%H:%M:%S")

    # Check if the current time matches the alarm time
    if current_time == alarm_time_str:
      print("\n⏰ WAKE UP! ALARM RINGING! ⏰")

      # Beep sound (Frequency: 2500Hz, Duration: 1000ms = 1 second)
      # Repeats 5 times
      for _ in range(5):
        try:
          winsound.Beep(2500, 1000)
        except RuntimeError:
          # Fallback if winsound is not available
          print("\a")  # ASCII bell character
          time.sleep(1)

      break

    # Wait 1 second before checking again to save CPU usage
    time.sleep(1)


if __name__ == "__main__":
  # Example: Set your alarm time in 24-hour format (HH:MM:SS)
  # Change "07:30:00" to whatever time you want
  alarm_time = input("Enter alarm time in 24-hour format (HH:MM:SS): ")
  set_alarm(alarm_time)
