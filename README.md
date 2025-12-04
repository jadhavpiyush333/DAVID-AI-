# DAVID - Dynamic Artificial Virtual Intelligence Device

DAVID is a Python-based voice-activated AI assistant that can perform various tasks including opening applications, searching the web, playing music, telling jokes, providing news updates, and much more through voice commands.

## 🚀 Features

- **Voice Recognition**: Listens and responds to voice commands using speech recognition
- **Text-to-Speech**: Provides audio feedback for all operations
- **Application Control**: Opens and closes applications like Notepad, Chrome, VS Code, XAMPP, Adobe Reader
- **Web Automation**: 
  - Opens websites (YouTube, Google, Wikipedia, Stack Overflow)
  - Searches Google and Wikipedia
  - Plays songs on YouTube
- **System Operations**: 
  - Window management (minimize, switch, scroll)
  - System shutdown functionality
  - Time and date information
- **Entertainment**: Tells jokes using pyjokes library
- **Communication**: Sends WhatsApp messages
- **Information Retrieval**: 
  - Gets news from Times of India
  - Retrieves IP address
  - Wikipedia search integration
- **Calculations**: WolframAlpha integration for mathematical calculations

## 📋 Prerequisites

### System Requirements
- Python 3.7 or higher
- Windows OS (due to Windows-specific libraries)
- Microphone for voice input
- Internet connection

### Required Python Libraries
-pip install pyttsx3
-pip install SpeechRecognition
-pip install wikipedia
-pip install pywhatkit
-pip install pyjokes
-pip install wolframalpha
-pip install requests
-pip install pyautogui
-pip install opencv-python
-pip install selenium
-pip install twilio
-pip install ecapture
-pip install beautifulsoup4
-pip install pywin32
-pip install feedparser



## 🔧 Installation

1. **Clone the repository**:
     git clone https://github.com/jadhavpiyush333/DAVID-AI.git
     cd DAVID-AI


2. **Install required dependencies**:
     -pip install -r requirements.txt

   
3. **Configure API keys**:
   - Get a WolframAlpha API key from [WolframAlpha API](https://products.wolframalpha.com/api/)
   - Get a News API key from [NewsAPI](https://newsapi.org/)
   - Update the API keys in the code:
     ```
     app_id = "YOUR_WOLFRAMALPHA_API_KEY"
     # Update News API URL with your key
     ```

4. **Update file paths**:
   - Modify application paths in the code to match your system configuration
   - Example paths to update:
     - Notepad path
     - Chrome path
     - VS Code path
     - Adobe Reader path
     - XAMPP path

5. **Configure WhatsApp (Optional)**:
   - Update the phone number in the "send message" command
   - Set up Twilio credentials if needed

## 💻 Usage

1. **Run the program**:
     -python David.py

   
2. DAVID will greet you based on the time of day:
   - Good Morning (6 AM - 12 PM)
   - Good Afternoon (12 PM - 4 PM)
   - Good Evening (4 PM - 8 PM)
   - Good Night (9 PM - 6 AM)

3. Speak your commands clearly after hearing **"Listening..."**

### Example Voice Commands

#### Application Commands
- "Open Notepad"
- "Open Chrome"
- "Open VS Code"
- "Open Adobe Reader"
- "Close [application name]"
- "Shut down"

#### Web Commands
- "Open YouTube"
- "Open Google"
- "Open Wikipedia"
- "Search [your query]"
- "Play [song name] on YouTube"

#### Information Commands
- "What's the time"
- "What is my IP address"
- "Tell me a joke"
- "Get news"
- "Wikipedia [topic]"
- "Calculate [mathematical expression]"

#### System Commands
- "Minimize"
- "Switch application"
- "Scroll up/down"
- "Exit"
- "Stop listening" (pauses listening for specified time)

#### Communication
- "Send message" (sends WhatsApp message)

#### AI Information
- "David means" or "meaning of David" (explains the AI's name)

## ⚙️ Configuration

### Voice Settings
Modify the voice in the initialization section:
   -engine = pyttsx3.init('sapi5')
  -voices = engine.getProperty('voices')
  -engine.setProperty('voices', voices.id) # Change index for different voice

  
### Customizing Application Paths
Update paths in the code to match your system:
       -Example
          -elif "open notepad" in query:
          -path = "C:\Windows\Notepad.exe" # Update this path
          -os.startfile(path)



### API Configuration
Replace placeholder API keys with your actual keys:
- WolframAlpha API (for calculations)
- News API (for news updates)
- Twilio credentials (for WhatsApp messages)

## 📁 Project Structure (Recommended for Future Development)

DAVID-AI/
├── README.md
├── requirements.txt
├── David.py (current main file)
├── config.py (for API keys and paths - to be created)
├── src/
│ ├── voice/
│ │ ├── speech.py (text-to-speech functions)
│ │ └── recognition.py (speech recognition)
│ ├── commands/
│ │ ├── applications.py (app control)
│ │ ├── web_operations.py (web automation)
│ │ └── system_operations.py (system controls)
│ └── utilities/
│ ├── time_utils.py (time and greetings)
│ └── api_handlers.py (API integrations)
└── tests/



## 📦 requirements.txt

Create a `requirements.txt` file with:
pyttsx3==2.90
SpeechRecognition==3.10.0
wikipedia==1.4.0
pywhatkit==5.4
pyjokes==0.6.0
wolframalpha==5.0.0
requests==2.31.0
pyautogui==0.9.54
opencv-python==4.8.1
selenium==4.15.0
twilio==8.10.0
ecapture==0.1.8
beautifulsoup4==4.12.2
pywin32==306
feedparser==6.0.10



## ⚠️ Known Issues

- Some features are incomplete or commented out in the code
- Hardcoded file paths need to be customized for each system
- News API URL contains formatting issues and needs proper API key
- Voice recognition timeout may need adjustment based on microphone quality
- Some import statements reference unused libraries
- Chrome automation requires proper path configuration
- Music playback on Wynk is incomplete

## 🔮 Future Enhancements

- [ ] Add GUI interface with Tkinter or PyQt
- [ ] Implement email functionality
- [ ] Add more natural language processing capabilities
- [ ] Create separate configuration file for paths and API keys
- [ ] Improve error handling and logging
- [ ] Add conversation memory and context awareness
- [ ] Support for multiple languages
- [ ] Add face recognition using OpenCV
- [ ] Implement reminder and alarm features
- [ ] Add weather forecast integration
- [ ] Create mobile app companion
- [ ] Add machine learning for personalized responses

## 🐛 Troubleshooting

### Microphone Not Working
- Check microphone permissions in Windows settings
- Adjust `r.pause_threshold` value in `takecommand()` function
- Test microphone with other applications

### Voice Recognition Errors
- Speak clearly and avoid background noise
- Adjust the `duration` parameter in `r.record()` function
- Check internet connection (Google Speech API requires internet)

### Application Paths Not Found
- Verify application installation paths
- Update paths in code to match your system configuration
- Use absolute paths instead of relative paths

### API Key Errors
- Verify API keys are valid and active
- Check API usage limits
- Ensure proper formatting of API URLs

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Speech recognition powered by Google Speech API
- Text-to-speech using pyttsx3 library
- WolframAlpha for computational intelligence
- Various Python libraries and their contributors
- Open source community for inspiration and support

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 📞 Contact & Support

- Create an issue for bug reports or feature requests
- Star ⭐ the repository if you find it helpful
- Follow for updates on new features

## ⚡ Quick Start Example

After installation, simply run:
python David.py

DAVID will greet you and wait for commands
Try saying: "Tell me a joke" or "What's the time"



## 🔒 Security Note

- Never commit API keys to public repositories
- Use environment variables for sensitive data
- Keep your `config.py` in `.gitignore`

## 📝 Changelog

### Version 1.0 (Current - Incomplete)
- Initial release with basic voice commands
- Application control features
- Web automation capabilities
- System operation commands
- API integrations for news, calculations, and IP lookup

---

**Note**: This is an incomplete project under active development. Some features may not work as expected. Contributions and suggestions are highly appreciated!

---

⭐ **Star this repository if you find it useful!** ⭐
