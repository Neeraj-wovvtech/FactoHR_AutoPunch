# FactoHR Scheduler  

Automate FactoHR login, punch-in, and logout using Selenium for **Chrome** and **Firefox**.  
Supports **secure credential encryption** and **automatic WebDriver selection**.  

---

## **Features**  
✅ Supports **both Chrome and Firefox** WebDrivers  
✅ **Secure credential encryption** (AES-based storage in `.env`)  
✅ **Automated scheduling** via `main.py`  
✅ **Headless mode** for silent execution  

---

## **1. Setup Instructions**  

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/Neeraj-wovvtech/FactoHR_AutoPunch.git
cd FactoHR_AutoPunch
```

### **Step 2: Create and Activate Virtual Environment**  
```sh
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**  
```sh
pip install -r requirements.txt
```

---

## **2. Download WebDriver**  

Since WebDriver **is not included**, download and place it in the `webdrivers/` folder.  

### ** ChromeDriver (For Chrome)**  
- **Find your Chrome version**:  
  - Open **Chrome** → Go to `chrome://settings/help` → Note the version.  
- **Download ChromeDriver**:  
  - [ChromeDriver Download](https://googlechromelabs.github.io/chrome-for-testing/)  
- **Extract and place it inside `webdrivers/`**  

### ** GeckoDriver (For Firefox)**  
- **Download GeckoDriver**:  
  - [GeckoDriver Download](https://github.com/mozilla/geckodriver/releases)  
- **Extract and place it inside `webdrivers/`**  

---

## **3. Configure the Script**  

### **Step 1: Run `main.py` (First-Time Setup)**  
```sh
python main.py
```
- This will **prompt for your FactoHR URL, username, and password**.  
- Credentials will be **securely stored in `.env`**.  

---

## **4. Automating Execution (Scheduling)**  

### **Windows Task Scheduler**  
1. Open **Task Scheduler** (`Win + R → taskschd.msc`)  
2. Click **Create Basic Task**  
3. **Trigger:** Select `Daily`  
4. **Action:** Select `Start a Program`  
   - **Program:** `python.exe`  
   - **Arguments:** `"C:\path\to\FactoHR_AutoPunch\src\main.py"`  
5. Click **Finish**  

### **Replit Deployment (For Cloud Execution)**  
- Use [Replit Always-On](https://replit.com/) to schedule execution in the cloud.  

---

## **5. Running Scripts Manually**  
```sh
python src/autoLogin.py    # To manually punch in
python src/autoLogout.py   # To manually log out
```

---

## **6. Project Structure**  
```
FactoHR_AutoPunch
├── .gitignore
├── README.md
├── requirements.txt
├── src
│   ├── autoLogin.py        # Unified login script
│   ├── autoLogout.py       # Unified logout script
│   ├── decrypt.py          # Securely decrypt credentials
│   ├── encrypt.py          # Encrypt credentials on first run
│   ├── main.py             # Handles scheduling & execution
└── webdrivers
    ├── chromedriver.exe    # Chrome WebDriver (User must download)
    ├── geckodriver.exe     # Firefox WebDriver (User must download)
```

---

## **7. Notes**  
- WebDriver **must be manually downloaded** and placed inside `webdrivers/`.  
- **Do not share your `.env` file**, as it contains encrypted credentials.  

---