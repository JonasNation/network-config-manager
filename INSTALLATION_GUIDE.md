\# Network Configuration Manager

\## Complete Setup and Installation Guide



\*\*Version:\*\* 1.0  

\*\*Project:\*\* Network Engineering Portfolio Project  

\*\*Author:\*\* Jonas Nation

\*\*Date:\*\* September 2025



---



\## Table of Contents



1\. \[Introduction](#introduction)

2\. \[Prerequisites](#prerequisites)

3\. \[Development Environment Setup](#development-environment-setup)

4\. \[Project Installation](#project-installation)

5\. \[Configuration](#configuration)

6\. \[Testing Environment Setup](#testing-environment-setup)

7\. \[Usage Instructions](#usage-instructions)

8\. \[GitHub Integration](#github-integration)

9\. \[Troubleshooting](#troubleshooting)

10\. \[Advanced Configuration](#advanced-configuration)



---



\## 1. Introduction



The Network Configuration Manager is a Python-based automation tool designed for network engineers to manage device configurations, perform connectivity testing, and automate backup operations. This manual provides step-by-step instructions for installation, configuration, and deployment.



\### Features

\- SSH connectivity testing to network devices

\- Automated configuration backup with timestamping

\- Multi-device support (Cisco IOS, IOS-XE, Juniper, Arista)

\- YAML-based device inventory management

\- Command-line interface with multiple operations

\- Professional logging and error handling



---



\## 2. Prerequisites



\### System Requirements

\- \*\*Operating System:\*\* Windows 10/11, macOS, or Linux

\- \*\*Python:\*\* Version 3.8 or higher

\- \*\*Network Access:\*\* SSH connectivity to target devices

\- \*\*Storage:\*\* Minimum 100MB available space



\### Required Knowledge

\- Basic command-line interface usage

\- Understanding of SSH and network protocols

\- Basic Python concepts (helpful but not required)



\### Hardware Requirements

\- Computer with network connectivity

\- Access to network devices or simulation environment



---



\## 3. Development Environment Setup



\### Step 3.1: Verify Python Installation



\*\*On Windows:\*\*

```cmd

python --version

```



\*\*On macOS/Linux:\*\*

```bash

python3 --version

```



\*\*Expected Output:\*\* `Python 3.8.x` or higher



\### Step 3.2: Create Project Directory



\*\*Windows Command Prompt:\*\*

```cmd

mkdir network-config-manager

cd network-config-manager

```



\*\*macOS/Linux Terminal:\*\*

```bash

mkdir network-config-manager

cd network-config-manager

```



\### Step 3.3: Create Python Virtual Environment



\*\*Windows:\*\*

```cmd

python -m venv venv

venv\\Scripts\\activate

```



\*\*macOS/Linux:\*\*

```bash

python3 -m venv venv

source venv/bin/activate

```



\*\*Verification:\*\* Your command prompt should show `(venv)` at the beginning.



\### Step 3.4: Create Project Structure



\*\*Windows:\*\*

```cmd

mkdir src configs backups logs

mkdir configs\\templates

```



\*\*macOS/Linux:\*\*

```bash

mkdir src configs backups logs

mkdir configs/templates

```



---



\## 4. Project Installation



\### Step 4.1: Download Project from GitHub



\*\*Option A: Clone Repository\*\*

```bash

git clone https://github.com/YOUR\_USERNAME/network-config-manager.git

cd network-config-manager

```



\*\*Option B: Download ZIP\*\*

1\. Visit the GitHub repository

2\. Click "Code" → "Download ZIP"

3\. Extract to your desired location

4\. Navigate to extracted folder



\### Step 4.2: Install Required Dependencies



\*\*Activate virtual environment (if not already active):\*\*

```bash

\# Windows

venv\\Scripts\\activate



\# macOS/Linux  

source venv/bin/activate

```



\*\*Install packages:\*\*

```bash

pip install -r requirements.txt

```



\*\*Manual installation (if requirements.txt unavailable):\*\*

```bash

pip install netmiko==4.3.0 PyYAML==6.0.1 rich==13.7.1

```



\### Step 4.3: Verify Installation



\*\*Test import functionality:\*\*

```bash

python -c "import netmiko; print('Netmiko installed successfully')"

python -c "import yaml; print('PyYAML installed successfully')"

```



---



\## 5. Configuration



\### Step 5.1: Device Inventory Setup



\*\*Edit the device configuration file:\*\*

```bash

\# Windows

notepad configs\\devices.yaml



\# macOS/Linux

nano configs/devices.yaml

```



\*\*Basic configuration template:\*\*

```yaml

\# Network Device Inventory

devices:

&nbsp; - name: "router-01"        # update to your device name

&nbsp;   host: "192.168.1.10"     # update to your used ip

&nbsp;   device\_type: "cisco\_ios" # update to based on your device

&nbsp;   username: "admin"

&nbsp;   description: "Main distribution router"

&nbsp;   

&nbsp; - name: "switch-01"

&nbsp;   host: "192.168.1.20"

&nbsp;   device\_type: "cisco\_ios"

&nbsp;   username: "admin"

&nbsp;   description: "Access layer switch"

```



\### Step 5.2: Supported Device Types



| Device Type | Description | Example Models |

|-------------|-------------|----------------|

| cisco\_ios | Cisco IOS devices | 2960, 3560, ISR routers |

| cisco\_xe | Cisco IOS-XE devices | CSR1000v, ISR4000 |

| juniper | Juniper JunOS devices | SRX, EX series |

| arista\_eos | Arista EOS devices | 7050, 7280 series |



\### Step 5.3: Security Considerations



\*\*For production environments:\*\*

\- Use SSH keys instead of passwords

\- Implement encrypted credential storage

\- Configure proper access controls

\- Use dedicated service accounts



---



\## 6. Testing Environment Setup



\### Option A: Using Cisco Modeling Labs (CML) -- I used CML, use what ever environment you are comfortable with



\#### Step 6.1: Create Test Topology

1\. Open CML interface

2\. Create new lab: "Network Config Manager Test"

3\. Add devices:

&nbsp;  - CSR1000v router

&nbsp;  - IOSv switch

&nbsp;  - External Connector

&nbsp;  - Unmanaged Switch

4\. Start devices



\#### Step 6.2: Configure Device SSH Access



\*\*Router Configuration:\*\*

```cisco

enable

configure terminal

interface GigabitEthernet1

ip address 10.0.0.10 255.255.255.0

no shutdown

exit



hostname Router1

ip domain-name lab.local

crypto key generate rsa modulus 1024

username admin privilege 15 secret admin

line vty 0 4

login local

transport input ssh

exit

ip ssh version 2

end

write memory

```



\*\*Switch Configuration:\*\*

```cisco

enable

configure terminal

interface Vlan1

ip address 10.0.0.20 255.255.255.0

no shutdown

exit



hostname Switch1

ip domain-name lab.local

crypto key generate rsa modulus 1024

username admin privilege 15 secret admin

line vty 0 15

login local

transport input ssh

exit

ip ssh version 2

end

write memory

```



\### Option B: Using Cisco DevNet Sandbox



1\. Visit: https://devnetsandbox.cisco.com/

2\. Create free account

3\. Access "Always On" sandboxes

4\. Note provided IP addresses and credentials

5\. Update devices.yaml with sandbox information



---



\## 7. Usage Instructions



\### Step 7.1: Basic Commands



\*\*Display help information:\*\*

```bash

python main.py --help

```



\*\*List all configured devices:\*\*

```bash

python main.py --list

```



\### Step 7.2: Connectivity Testing



\*\*Test specific device:\*\*

```bash

python main.py --test --device router-01

```



\*\*Expected output:\*\*

```

Network Configuration Manager v1.0

==================================================

Testing connection to: router-01

Attempting to connect to 10.0.0.10...

✅ Connection successful!

Device response preview: Cisco IOS XE Software, Version 17.03.04a...

```



\### Step 7.3: Configuration Backup



\*\*Backup single device:\*\*

```bash

python main.py --backup --device router-01

```



\*\*Backup all devices:\*\*

```bash

python main.py --backup --all

```



\*\*Expected output:\*\*

```

Connecting to router-01...

Retrieving configuration...

✅ Backup completed: backups/router-01\_20250920\_143022.txt

```



\### Step 7.4: View Backup Files



\*\*Windows:\*\*

```cmd

dir backups

```



\*\*macOS/Linux:\*\*

```bash

ls -la backups/

```



---



\## 8. GitHub Integration



\### Step 8.1: Initialize Git Repository



```bash

git init

git add .

git commit -m "Initial commit: Network Configuration Manager"

```



\### Step 8.2: Create GitHub Repository



1\. Go to https://github.com

2\. Sign in to your account

3\. Click "+" → "New repository"

4\. Repository name: `network-config-manager`

5\. Description: "Python-based network device configuration management tool"

6\. Set to Public

7\. Click "Create repository"



\### Step 8.3: Connect Local Repository to GitHub



```bash

git remote add origin https://github.com/YOUR\_USERNAME/network-config-manager.git

git branch -M main

```



\### Step 8.4: Create Personal Access Token



1\. GitHub → Settings → Developer settings

2\. Personal access tokens → Tokens (classic)

3\. Generate new token → Generate new token (classic)

4\. Note: "Network Config Manager"

5\. Select scope: "repo"

6\. Generate token

7\. \*\*Copy token immediately\*\*



\### Step 8.5: Push to GitHub



```bash

git push -u origin main

```



\*\*When prompted:\*\*

\- Username: Your GitHub username

\- Password: Paste the personal access token



---



\## 9. Troubleshooting



\### Common Issues and Solutions



\#### Issue: "python is not recognized"

\*\*Solution:\*\*

\- Windows: Use `py` instead of `python`

\- Ensure Python is added to system PATH

\- Reinstall Python with "Add to PATH" option



\#### Issue: "Authentication failed"

\*\*Causes and solutions:\*\*

\- \*\*Wrong credentials:\*\* Verify username/password in device configuration

\- \*\*SSH not enabled:\*\* Configure SSH on target device

\- \*\*Network connectivity:\*\* Test with `ping` command first



\#### Issue: "Connection timeout"

\*\*Solutions:\*\*

\- Verify device IP address is correct

\- Check network connectivity

\- Ensure SSH is enabled on target device

\- Verify firewall settings



\#### Issue: "Module not found" errors

\*\*Solutions:\*\*

```bash

\# Reactivate virtual environment

venv\\Scripts\\activate  # Windows

source venv/bin/activate  # macOS/Linux



\# Reinstall dependencies

pip install -r requirements.txt

```



\#### Issue: SSH compatibility errors

\*\*For older IOS devices:\*\*

```bash

\# Use legacy SSH options

ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa admin@device\_ip

```



\### Debug Mode



\*\*Enable detailed logging:\*\*

```python

\# Add to device\_connector.py

logging.basicConfig(level=logging.DEBUG)

```



---



\## 10. Advanced Configuration



\### Step 10.1: Secure Credential Storage



\*\*Create credentials file:\*\*

```yaml

\# configs/credentials.yaml (add to .gitignore)

devices:

&nbsp; router-01:

&nbsp;   password: "secure\_password"

&nbsp; switch-01:

&nbsp;   password: "another\_password"

```



\### Step 10.2: Scheduled Backups



\*\*Windows Task Scheduler:\*\*

1\. Open Task Scheduler

2\. Create Basic Task

3\. Program: `python`

4\. Arguments: `C:\\path\\to\\network-config-manager\\main.py --backup --all`



\*\*Linux/macOS Cron:\*\*

```bash

\# Edit crontab

crontab -e



\# Add daily backup at 2 AM

0 2 \* \* \* cd /path/to/network-config-manager \&\& python main.py --backup --all

```



\### Step 10.3: Configuration Templates



\*\*Create template files in `configs/templates/`:\*\*

```

\# configs/templates/basic\_security.txt

service password-encryption

no ip http server

line vty 0 4

transport input ssh

```



---



\## Appendix A: File Structure



```

network-config-manager/

├── src/

│   ├── \_\_init\_\_.py

│   ├── device\_connector.py

│   ├── config\_reader.py

│   └── backup\_handler.py

├── configs/

│   ├── devices.yaml

│   └── templates/

├── backups/

├── logs/

├── images/

├── main.py

├── requirements.txt

├── README.md

└── .gitignore

```



\## Appendix B: Command Reference



| Command | Description |

|---------|-------------|

| `python main.py --help` | Show help information |

| `python main.py --list` | List all devices |

| `python main.py --test --device <name>` | Test device connectivity |

| `python main.py --backup --device <name>` | Backup single device |

| `python main.py --backup --all` | Backup all devices |



---



\## Support and Contributing



For issues, questions, or contributions:

\- Create issues on GitHub repository

\- Submit pull requests for improvements

\- Contact: \[jonas.nation@yahoo.com]



\*\*License:\*\* Educational/Portfolio use



---



\*This manual was created as part of a network engineering portfolio project demonstrating Python automation skills and professional documentation practices.\*

