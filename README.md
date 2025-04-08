## Kids_reminder_timer_program
### Personalized Alarm with Text-to-Speech and Sound

This project allows you to set up a personalized alarm with both text-to-speech (TTS) messages and a sound file that plays when the alarm goes off. The script lets you choose from predefined alarm messages or enter a custom message. You can also set the time for the alarm and specify how many times the alarm should repeat.

### Prerequisites

Before running the script, make sure you have installed the necessary modules. You can install them using `pip`:

```bash
pip install pyttsx3 datetime playsound
```

### 📈 Features
1.**Choice of Alarm Message:** Choose from several predefined alarm messages or enter a custom text.

2.**Alarm Repetition:** Specify the number of times the alarm message should repeat.

3.**Set Alarm Time:** Enter the alarm time in HH:MM:SS AM/PM format.

4.**Sound Notification:** An alarm sound (audio file) can be played when the alarm goes off. The audio file is specified in the code.

### 📂 How to Use
**1. Run the Script**
Execute the Python script containing the alarm code. You can run it from a terminal or an IDE (e.g., VSCode, PyCharm, or Jupyter Notebook).

**2. Select the Alarm Message**
Once the script is executed, you will be prompted to choose an alarm message from the following options:

1: It's time to play the violin

2: It's time to do the homework

3: It's time to go to school

4: Personalize your alarm message

Enter the number corresponding to your choice.

**3. Enter the Number of Repetitions**
After selecting the message, enter the number of times you want the alarm message to repeat. The alarm will play this many times.

**4. Set the Alarm Time**
Enter the time for the alarm in HH:MM:SS AM/PM format. For example: 07:00:00 AM.

**5. Alarm Goes Off**
When the specified time arrives, the alarm message will be spoken aloud using the text-to-speech engine, and the sound file will play. The number of repetitions will be followed, then the program will stop.

### 🔑 License

This project is open source and available under the MIT License. See the LICENSE file for more details.
