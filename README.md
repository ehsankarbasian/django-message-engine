# DjangoMessenger  
A flexible and extensible multi-channel messaging engine for Django.

DjangoMessenger is a powerful message-building and message-sending framework for Django, designed using principles from Clean Architecture and Hexagonal Architecture.  
It fully decouples **message building** from **message delivery** and allows developers to send messages over multiple channels such as:

- SMS  
- Email  
- Telegram  
- Push  
- Any custom channel via user-defined senders  

---

## 🎯 Key Features

### ✔ Full separation between message creation and message delivery  
Message content is generated through **Builder Interfaces** and delivered through **Sender Interfaces** that are completely independent.

### ✔ Rich Metadata Item System  
Supports declarative UI components like:

- Button  
- Form  
- Input  
- Checkbox  
- Radio  
- Submit  

Each sender is responsible for rendering these UI elements in its own format (HTML, Telegram markup, plain SMS text, etc.).

### ✔ Plug-in Oriented Architecture  
Developers can easily extend the system by adding:

- Custom Builders  
- Custom Senders  
- Custom Metadata Items  
- Custom Permissions  

### ✔ Powerful Permission Layer  
Before building or sending a message, permissions can be checked:

- Verified  
- NotVerified  
- AllowAny  
- Custom user-defined permissions  

### ✔ Private Internal Database Layer  
A Django app containing private models manages:

- Channel configuration  
- Activation status  
- Verification state  
- Other internal metadata  

This database layer is not directly exposed to the end user.

---

## 🏗 Architecture Overview

The system is structured into several components:

### **1. Main Component**  
Contains Facade and Factory for orchestrating message creation and delivery.

### **2. Business Logic Component**  
Includes the Builder Interface and its concrete implementations.

### **3. Sender Setup Component**  
Includes the Sender Interface and various sender implementations (SMS, Email, Telegram, ...).

### **4. Metadata Setup Component**  
Manages buttons, forms, inputs and other metadata items, with specific rendering behavior per sender.

### **5. Permission Component**  
Controls whether a message can be built or delivered.

---

## 📦 Installation

(Coming soon on PyPI)

```bash
pip install djangomessenger
```

Add to Django:

```python
INSTALLED_APPS = [
    ...
    "message_engine",
]
```

---

## 🚀 Basic Usage Example

```python
from djangomessenger import facade

facade.send(
    user=user,
    message_type="welcome",
    channel="sms",
    data={"username": "alex"},
)
```

---

## 🧩 Writing a Custom Sender

```python
class MyCustomSender(SenderInterface):
    def render_button(self, item):
        ...

    def send(self, payload):
        ...
```

Register the sender:

```python
register_sender("mychannel", MyCustomSender)
```

---

## 📄 License
MIT License

---

## 🤝 Contributing
Pull requests and issues are welcome.
