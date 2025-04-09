# Многофункциональный портовый сканер


Профессиональный инструмент для анализа TCP-портов с расширенными возможностями идентификации сервисов

## 📌 Назначение
- Анализ безопасности локальных сетей
- Тестирование конфигурации фаерволов
- Диагностика сетевых служб и оборудования
  
## 🛠️ Установка

### 🖥️ Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Dimatop228/portscan.git
cd portscan
pip3 install -r requirements.txt
python portscan.py
```
### 📱 Termux
```bash
apt update && apt upgrade -y
apt install python3 python3-pip git -y
git clone https://github.com/Dimatop228/portscan.git
cd portscan
pip3 install -r requirements.txt
python portscan.py
```
## 🚀 Ключевые особенности

### 📚 Расширенная база портов (400+ сервисов)
```python
PORT_SERVICES = {
    80: "HTTP",
    22: "SSH",
    3306: "MySQL",
    25565: "Minecraft",
    1883: "MQTT",
    2375: "Docker",
    # ... и другие
}
```
# Multi-Purpose Port Scanner


Professional TCP port analysis tool with advanced service identification capabilities

## 📌 Purpose
- Local network security auditing
- Firewall configuration testing
- Network service diagnostics

## 🛠️ Installation

### 🖥️ Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Dimatop228/portscan.git
cd portscan
pip3 install -r requirements.txt
python portscan.py
```
### 📱 Termux
```bash
apt update && apt upgrade -y
apt install python3 python3-pip git -y
git clone https://github.com/Dimatop228/portscan.git
cd portscan
pip3 install -r requirements.txt
python portscan.py
```

## 🚀 Key Features

### 📚 Extended Port Database (400+ services)
```python
PORT_SERVICES = {
    80: "HTTP",
    22: "SSH",
    3306: "MySQL",
    25565: "Minecraft",
    1883: "MQTT",
    2375: "Docker",
    # ... and others
}
```
